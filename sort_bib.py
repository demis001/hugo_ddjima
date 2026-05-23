import re

# Legacy manual BibTeX sorter. The normal publication update path is now:
#   ./process_bib_file.sh
# which fetches filtered PubMed records and imports them into Hugo Blox.

# File paths
input_path = 'cite_2025.bib'  # Replace with your input file path
output_path = 'cite_2025_sorted.bib'  # Replace with your desired output file path

# Read the input BibTeX file
with open(input_path, 'r') as file:
    content = file.read()

# Extract individual entries
entries = re.split(r'@\w+{', content)[1:]  # Split by BibTeX entry start
entries = [f"@{entry}" for entry in entries]  # Add the @ prefix back

# Extract year from each entry
def extract_year(entry):
    match = re.search(r'year\s*=\s*[{"](\d{4})[}"]', entry, re.IGNORECASE)
    return int(match.group(1)) if match else 0

# Sort entries by year in descending order
sorted_entries = sorted(entries, key=extract_year, reverse=True)

# Write the sorted entries to a new file
with open(output_path, 'w') as file:
    file.write("\n".join(sorted_entries))

output_path
