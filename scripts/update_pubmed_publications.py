#!/usr/bin/env python3
"""Fetch PubMed records for the site owner and import them into Hugo Academic.

This keeps the BibTeX source dynamic, so new PubMed-indexed publications can be
picked up without manually rebuilding cite_2025_sorted.bib.
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


DEFAULT_QUERY = (
    '"Jima DD"[Author] OR "Dereje Jima"[Full Author Name] '
    'OR "Dereje D Jima"[Full Author Name] OR "Jima Dereje"[Full Author Name]'
)
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
OWNER_LAST_NAME = "jima"
OWNER_FORENAMES = {"dereje", "dereje d", "dereje d."}
OWNER_INITIALS = {"dd"}
CURATED_FEATURED_DOIS = {
    "10.1080/15592294.2022.2091815",
    "10.1038/ng.2468",
}


def fetch_url(url: str) -> bytes:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "ddjima-publication-updater/1.0"},
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        return response.read()


def ncbi_params(params: dict[str, str | int]) -> str:
    email = os.environ.get("NCBI_EMAIL")
    api_key = os.environ.get("NCBI_API_KEY")
    params = {
        "tool": "ddjima_publication_updater",
        **params,
    }
    if email:
        params["email"] = email
    if api_key:
        params["api_key"] = api_key
    return urllib.parse.urlencode(params)


def search_pmids(query: str, retmax: int) -> list[str]:
    url = f"{EUTILS}/esearch.fcgi?{ncbi_params({
        'db': 'pubmed',
        'term': query,
        'retmode': 'xml',
        'retmax': retmax,
        'sort': 'pub date',
    })}"
    root = ET.fromstring(fetch_url(url))
    return [node.text for node in root.findall(".//Id") if node.text]


def fetch_pubmed_xml(pmids: list[str]) -> ET.Element:
    if not pmids:
        return ET.Element("PubmedArticleSet")
    url = f"{EUTILS}/efetch.fcgi?{ncbi_params({
        'db': 'pubmed',
        'id': ','.join(pmids),
        'retmode': 'xml',
    })}"
    return ET.fromstring(fetch_url(url))


def text(node: ET.Element | None) -> str:
    if node is None:
        return ""
    return " ".join("".join(node.itertext()).split())


def first_text(article: ET.Element, paths: list[str]) -> str:
    for path in paths:
        value = text(article.find(path))
        if value:
            return value
    return ""


def is_owner_author(author: ET.Element) -> bool:
    last = text(author.find("LastName")).lower()
    fore = text(author.find("ForeName")).lower()
    initials = text(author.find("Initials")).lower()
    if last != OWNER_LAST_NAME:
        return False
    return fore in OWNER_FORENAMES or initials in OWNER_INITIALS


def filter_owner_articles(root: ET.Element) -> ET.Element:
    filtered = ET.Element(root.tag)
    for article in root.findall(".//PubmedArticle"):
        if any(is_owner_author(author) for author in article.findall(".//AuthorList/Author")):
            filtered.append(article)
    return filtered


def publication_year(article: ET.Element) -> str:
    year = first_text(
        article,
        [
            ".//ArticleDate/Year",
            ".//JournalIssue/PubDate/Year",
            ".//PubMedPubDate[@PubStatus='pubmed']/Year",
        ],
    )
    if year:
        return year
    medline_date = first_text(article, [".//JournalIssue/PubDate/MedlineDate"])
    match = re.search(r"(19|20)\d{2}", medline_date)
    return match.group(0) if match else "0000"


def article_authors(article: ET.Element) -> str:
    authors: list[str] = []
    for author in article.findall(".//AuthorList/Author"):
        collective = text(author.find("CollectiveName"))
        if collective:
            authors.append(collective)
            continue
        last = text(author.find("LastName"))
        fore = text(author.find("ForeName")) or text(author.find("Initials"))
        if last and fore:
            authors.append(f"{last}, {fore}")
        elif last:
            authors.append(last)
    return " and ".join(authors)


def bib_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("&", "\\&")
        .replace("%", "\\%")
        .replace("$", "\\$")
        .replace("#", "\\#")
        .replace("_", "\\_")
    )


def citation_key(article: ET.Element, used: set[str]) -> str:
    year = publication_year(article)
    first_author = article.find(".//AuthorList/Author")
    last = text(first_author.find("LastName")) if first_author is not None else "pubmed"
    title = first_text(article, [".//ArticleTitle"])
    first_word = re.sub(r"[^A-Za-z0-9]+", "", title.split()[0].lower()) if title else "article"
    base = re.sub(r"[^A-Za-z0-9]+", "", f"{last.lower()}{year}{first_word}") or "pubmed"
    key = base
    counter = 2
    while key in used:
        key = f"{base}{counter}"
        counter += 1
    used.add(key)
    return key


def article_to_bibtex(article: ET.Element, used_keys: set[str]) -> tuple[int, str]:
    pmid = first_text(article, [".//MedlineCitation/PMID"])
    doi = ""
    for article_id in article.findall(".//ArticleIdList/ArticleId"):
        if article_id.attrib.get("IdType") == "doi":
            doi = text(article_id)
            break

    fields = {
        "title": first_text(article, [".//ArticleTitle"]),
        "author": article_authors(article),
        "journal": first_text(article, [".//Journal/Title"]),
        "volume": first_text(article, [".//JournalIssue/Volume"]),
        "number": first_text(article, [".//JournalIssue/Issue"]),
        "pages": first_text(article, [".//Pagination/MedlinePgn"]),
        "year": publication_year(article),
        "doi": doi,
        "pmid": pmid,
        "url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else "",
    }
    key = citation_key(article, used_keys)
    lines = [f"@article{{{key},"]
    for name, value in fields.items():
        if value:
            lines.append(f"  {name} = {{{bib_escape(value)}}},")
    lines.append("}")
    return int(fields["year"] or 0), "\n".join(lines)


def write_bibtex(root: ET.Element, output: Path) -> int:
    used_keys: set[str] = set()
    entries = [article_to_bibtex(article, used_keys) for article in root.findall(".//PubmedArticle")]
    entries.sort(key=lambda item: item[0], reverse=True)
    output.write_text("\n\n".join(entry for _, entry in entries) + "\n", encoding="utf-8")
    return len(entries)


def current_pmids_from_bibtex(bib_file: Path) -> set[str]:
    if not bib_file.exists():
        return set()
    content = bib_file.read_text(encoding="utf-8")
    return set(re.findall(r"^\s*pmid\s*=\s*\{([^}]+)\}", content, flags=re.MULTILINE))


def run_import(bib_file: Path, destination: Path) -> None:
    academic = shutil.which("academic")
    if not academic:
        print("Wrote BibTeX, but `academic` was not found on PATH. Import manually with:")
        print(f"  academic import {bib_file} {destination}/ --overwrite --compact")
        return
    subprocess.run(
        [academic, "import", str(bib_file), str(destination), "--overwrite", "--compact"],
        check=True,
    )


def normalize_hugoblox_doi(destination: Path) -> int:
    """Move imported top-level DOI fields to the current Hugo Blox field."""
    changed = 0
    pattern = re.compile(r'^doi:\s*["\']?([^"\'\n]+)["\']?\s*$', re.MULTILINE)
    for page in destination.glob("*/index.md"):
        content = page.read_text(encoding="utf-8")
        if "hugoblox:\n  ids:\n    doi:" in content:
            continue
        match = pattern.search(content)
        if not match:
            continue
        doi = match.group(1).strip()
        replacement = f'hugoblox:\n  ids:\n    doi: "{doi}"'
        page.write_text(pattern.sub(replacement, content, count=1), encoding="utf-8")
        changed += 1
    return changed


def remove_stale_imported_publications(destination: Path, bib_file: Path) -> int:
    """Remove previously imported PubMed pages that are no longer in the filtered BibTeX."""
    current_pmids = current_pmids_from_bibtex(bib_file)
    if not current_pmids:
        return 0

    removed = 0
    for page in destination.glob("*/index.md"):
        content = page.read_text(encoding="utf-8")
        if not re.search(r"^publishDate:\s*['\"]2026-", content, flags=re.MULTILINE):
            continue
        match = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)/", content)
        if not match or match.group(1) in current_pmids:
            continue
        shutil.rmtree(page.parent)
        removed += 1
    return removed


def restore_curated_publications(destination: Path) -> int:
    """Keep hand-curated homepage feature flags after Academic rewrites pages."""
    changed = 0
    for page in destination.glob("*/index.md"):
        content = page.read_text(encoding="utf-8")
        if not any(doi in content for doi in CURATED_FEATURED_DOIS):
            continue

        updated = re.sub(r"^featured:\s*false\s*$", "featured: true", content, flags=re.MULTILINE)
        if updated == content and not re.search(r"^featured:\s*", content, flags=re.MULTILINE):
            updated = updated.replace("\n---\n", "\nfeatured: true\n---\n", 1)

        if updated != content:
            page.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Update publication pages from PubMed.")
    parser.add_argument("--query", default=DEFAULT_QUERY, help="PubMed query to fetch.")
    parser.add_argument("--retmax", type=int, default=300, help="Maximum PubMed records to fetch.")
    parser.add_argument("--output", default="cite_pubmed_sorted.bib", help="Output BibTeX path.")
    parser.add_argument("--destination", default="content/publication", help="Academic import destination.")
    parser.add_argument("--skip-import", action="store_true", help="Only write the BibTeX file.")
    parser.add_argument(
        "--allow-empty",
        action="store_true",
        help="Allow overwriting the BibTeX file and importing even when no matching records are found.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    output = Path(args.output)
    destination = Path(args.destination)
    pmids = search_pmids(args.query, args.retmax)
    root = fetch_pubmed_xml(pmids)
    root = filter_owner_articles(root)
    if not root.findall(".//PubmedArticle") and not args.allow_empty:
        print("Found 0 matching PubMed records after author filtering; leaving existing files unchanged.")
        print("Use --allow-empty if you really want to write an empty BibTeX file.")
        return 1
    count = write_bibtex(root, output)
    print(f"Wrote {count} PubMed records to {output}")
    if not args.skip_import:
        run_import(output, destination)
        changed = normalize_hugoblox_doi(destination)
        if changed:
            print(f"Normalized DOI metadata in {changed} imported publication pages")
        removed = remove_stale_imported_publications(destination, output)
        if removed:
            print(f"Removed {removed} stale imported publication pages")
        restored = restore_curated_publications(destination)
        if restored:
            print(f"Restored featured metadata in {restored} curated publication pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
