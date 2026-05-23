#!/usr/bin/env bash
set -euo pipefail

# Preferred dynamic update path:
# 1. Query PubMed for Dereje Jima author records.
# 2. Write a newest-first BibTeX file.
# 3. Import the BibTeX into Hugo Academic publication pages.
#
# Optional NCBI settings:
#   export NCBI_EMAIL="you@example.com"
#   export NCBI_API_KEY="..."

# Use like this
# ./process_bib_file.sh

# Option, better for NCBI
# export NCBI_EMAIL="ddjima2014@gmail.com"
# ./process_bib_file.sh

python3 scripts/update_pubmed_publications.py "$@"
