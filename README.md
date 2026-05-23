# [Dereje Jima Personal Website](https://www.ddjima.com)

This repository contains the source code and content for Dereje Jima's personal academic website. The site highlights research interests, professional experience, selected and full publication lists, recent news, honors, and contact information.

The website is available at `https://www.ddjima.com/`.

## Deployment

The production site is deployed with Netlify from this repository and published at `https://www.ddjima.com/`.

Add the live Netlify status badge here after copying the badge Markdown from Netlify Site settings > Build & deploy > Status badges. The badge URL contains a Netlify API badge ID that is not stored in this repository.

## Publication Updates

Publications are refreshed from PubMed with the local helper:

```bash
./process_bib_file.sh
```

The updater writes `cite_pubmed_sorted.bib`, imports the filtered records into `content/publication/`, restores the curated featured publication cards, and prunes stale PubMed imports that are no longer in the filtered result set. The expected current PubMed record count is `76`.

After refreshing publications, verify the site and the full publication count:

```bash
npm run build
npm run verify:publications
```

Older manual BibTeX helpers such as `cite_2025.bib`, `cite_2025_sorted.bib`, and `sort_bib.py` are legacy fallback files. The normal update path should be the PubMed updater unless intentionally reverting to manual import.
