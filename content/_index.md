---
# Leave the homepage title empty to use the site title
title: "Dereje Jima Personal Website"
logo: "/media/logo.png"
date: 2024-12-17
type: landing

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
      title: "📚 My Research"
      subtitle: ""
      text: |-
        My research is focused on bioinformatics and computational biology, emphasizing high-throughput biological data analysis to integrate complex datasets and drive impactful discoveries. My expertise includes developing bioinformatics tools, performing advanced data analysis, and employing statistical modeling with applications in genomics, epigenomics, cancer genomics, immunology, and infectious diseases. As a Bioinformatics Liaison at the Center for Human Health and the Environment (CHHE), I collaborate with researchers across diverse disciplines, ensuring the effective integration of bioinformatics into a wide range of projects. My role involves contributing to bioinformatics initiatives, strategic research planning, and fostering collaborative efforts to address complex biological questions. Additionally, I guide and mentor PhD students, helping them navigate intricate bioinformatics challenges and develop essential research skills. I am committed to advancing scientific discovery and nurturing the next generation of researchers by creating cutting-edge tools and cultivating a dynamic, interdisciplinary research environment. My work aims to spark interest in the multidisciplinary nature of bioinformatics and its transformative potential for modern science.

        Please reach out to collaborate 😃
    design:
      columns: "1"
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
      title: "📚 Full Publication List"
      text: |-
        You can view my complete list of peer-reviewed publications in the Full Publication List page.

        [View Full Publication List](full_publication_list/)
    design:
      columns: "1"
  - block: collection
    id: talks
    content:
      title: Recent & Upcoming Talks
      filters:
        folders:
          - event
    design:
      view: article-grid
      show_cite: false
      columns: 1
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
        tag: ""
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
      view: date-title-summary
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
