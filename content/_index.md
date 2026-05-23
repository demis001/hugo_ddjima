---
# Leave the homepage title empty to use the site title
title: "Dereje Jima"
logo: "/media/logo.png"
date: 2024-12-17
type: landing
description: "Dereje Jima is a Senior Research Scholar in bioinformatics and computational biology at North Carolina State University, working on genomics, epigenomics, transcriptomics, environmental health, reproducible workflows, and collaborative data science."
summary: "Dereje Jima is a Senior Research Scholar in bioinformatics and computational biology at North Carolina State University, working on genomics, epigenomics, transcriptomics, environmental health, reproducible workflows, and collaborative data science."

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: stacked-peaks.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false
  - block: markdown
    content:
      title: "Research Focus"
      subtitle: ""
      text: |-
        I work at the intersection of bioinformatics, computational biology, and collaborative environmental health research. My focus is on integrating high-throughput genomic, epigenomic, transcriptomic, and other complex biological datasets to uncover mechanisms that shape human health and disease.

        At the Center for Human Health and the Environment (CHHE), I serve as a bioinformatics liaison for interdisciplinary research teams. I develop reproducible analysis workflows, contribute to study design and statistical modeling, support collaborative research planning, and mentor trainees working through challenging computational biology questions.

        I am especially interested in projects that turn complex data into clear biological insight. Please reach out if you would like to collaborate.
    design:
      columns: "1"
      css_class: research-focus-section
  - block: collection
    id: papers
    content:
      title: Featured Publications
      text: |-
        Highlighted publications selected for their impact and relevance.
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: card
      columns: 2
  - block: collection
    id: recent-publications
    content:
      title: Recent Publications
      text: |-
        A curated list of recent peer-reviewed work. Featured items are excluded so the recent list stays fresh and uncluttered.
      filters:
        folders:
          - publication
        exclude_featured: true
      count: 6
    design:
      view: citation
      show_cite: false
      columns: 1
  - block: markdown
    content:
      title: "Full Publication List"
      text: |-
        View the complete peer-reviewed publication record, including publications beyond the highlighted and recent selections shown above.

        [View Full Publication List](/full_publication/)
    design:
      columns: "1"
  - block: collection
    id: news
    content:
      title: Recent News
      subtitle: ""
      text: ""
      # Page type to display. E.g. post, talk, publication...
      page_type: post
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        author: ""
        category: ""
        tag: "News"
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: article-grid
      columns: 2
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
  - block: cta-card
    demo: false # Only display this section in the Hugo Blox Builder demo site
    content:
      title: 👉 Full Publications in Pubmed
      text: |-
        Explore my publications in Pubmed and keep up with the latest research.
      button:
        text: Link to Pubmed
        url: https://pubmed.ncbi.nlm.nih.gov/?term=Dereje+Jima&sort=date
    design:
      card:
        # Card background color (CSS class)
        css_class: "bg-primary-700"
        css_style: ""
---
