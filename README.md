# Data Analytics Portfolio — Robert Grantham

Live site: https://rgrantham82.github.io/data-analytics-portfolio/

This repository powers my personal data analytics portfolio website (GitHub Pages + Jekyll) and hosts selected project artifacts (Excel dashboards, notebooks, scripts, screenshots) used in case studies.

---

## What you'll find here

### 🌐 Portfolio website (Jekyll)
- **Home:** `index.md`
- **About:** `about.md`
- **Projects:** `projects.md` (project grid + search/filter UI)
- **Contact:** `contact.md`
- **Project data:** `_data/projects.yml` — drives the cards, tags, and filter buttons on the Projects page
- **Theme/layout:** `_layouts/`, `_includes/`, `assets/css/`, `assets/js/`

The site uses the `pages-themes/architect` remote theme, with a custom `_layouts/default.html`
and `_includes/head-custom.html` layered on top.

### 📁 Projects (work samples + artifacts)
Project materials live under `projects/` — one folder per project (datasets, dashboards, notebooks, scripts, docs).

---

## Featured projects

Below are a few examples of the kinds of work in this portfolio. For the full list, see the Projects page on the live site.

### 1) Art Sales Pop-Up Tracker (Excel + Python companion EDA)
**Folder:** `projects/art-sales-popup-tracker/`

An Excel-based workflow for tracking pop-up / street-sale performance (sales, costs, objections, venue performance), plus a lightweight Python EDA companion for exporting KPIs and charts.

What's included:
- Excel workbook: `Art_Sales_Data_Analysis.xlsx`
- Project documentation: `README.md`, `DATA_DICTIONARY.md`
- Python analysis companion: `analysis/analyze_art_sales.py`
- Notebook version: `analysis/Art_Sales_EDA_Companion.ipynb`
- Requirements: `analysis/requirements.txt`

---

## How to run the site locally

### Prerequisites
- Ruby (recent version recommended)
- Bundler (`gem install bundler`)
- Git

### Install and serve
```bash
git clone https://github.com/rgrantham82/data-analytics-portfolio.git
cd data-analytics-portfolio

bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000/data-analytics-portfolio/ — note the `baseurl`,
which the site needs in order to resolve assets the same way it does on GitHub Pages.

---

## Adding a project

1. Drop a screenshot in `assets/images/`.
2. Add an entry to `_data/projects.yml`:

   ```yaml
   - title: Project Title
     subtitle: Short framing line
     description: >
       Two or three sentences on the problem, the approach, and the result.
     image: /assets/images/your-screenshot.png
     link: https://github.com/rgrantham82/your-repo
     link_text: View Project
     tags: SQL, Forecasting
   ```

3. That's it — the card, its tags, and the matching filter button on the Projects
   page are all generated from this file. The `image` key is optional; a project
   without one renders as a text-only card.
