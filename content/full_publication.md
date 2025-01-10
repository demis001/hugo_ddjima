---
title: "Full Publications"
date: 2023-10-24
type: landing  # Use the same type as 'Experience'

design:
  spacing: '5rem'
  view: custom-view

layout: list

# Page sections
sections:
  - block: collection
    content:
      title: Full Publications
      filters:
        folders:
          - full_publication  # Ensure this points to the correct folder
        exclude_featured: false  # Include all publications
      order: desc  # Sort by descending date
    design:
      view: citation
---

