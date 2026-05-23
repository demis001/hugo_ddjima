#!/usr/bin/env bash
set -euo pipefail

expected_count="${1:-76}"

if [[ ! -f public/full_publication/index.html ]]; then
  echo "public/full_publication/index.html not found. Run npm run build first." >&2
  exit 1
fi

actual_count="$(rg -o "publication-summary-item" public/full_publication/index.html public/full_publication/page/*/index.html 2>/dev/null | wc -l | tr -d '[:space:]')"

if [[ "$actual_count" != "$expected_count" ]]; then
  echo "Expected ${expected_count} full-publication entries, found ${actual_count}." >&2
  exit 1
fi

echo "Full publication count verified: ${actual_count}"
