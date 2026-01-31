# Data Analytics Portfolio — Robert Grantham

Live site: https://rgrantham82.github.io/data-analytics-portfolio/

This repository powers my personal data analytics portfolio website (GitHub Pages + Jekyll) and hosts selected project artifacts (Excel dashboards, notebooks, scripts, screenshots) used in case studies.

---

## What you’ll find here

### 🌐 Portfolio website (Jekyll)
- **Home:** `index.md`
- **About:** `about.md`
- **Projects:** `projects.md` (project grid + search/filter UI)
- **Contact:** `contact.md`
- **Theme/layout:** `_layouts/`, `_includes/`, `assets/css/`, `assets/js/`

### 📁 Projects (work samples + artifacts)
Project materials live under:
- `projects/` — per-project folders (datasets, dashboards, notebooks, scripts, docs)

> Tip: The website’s Projects page is driven by project metadata (typically in `_data/projects.yml` if you’re using the data-driven grid approach).

---

## Featured projects

Below are a few examples of the kinds of work in this portfolio. For the full list, see the Projects page on the live site.

### 1) Art Sales Pop-Up Tracker (Excel + Python companion EDA)
**Folder:** `projects/art-sales-popup-tracker/`

An Excel-based workflow for tracking pop-up / street-sale performance (sales, costs, objections, venue performance), plus a lightweight Python EDA companion for exporting KPIs and charts.

What’s included:
- Excel workbook: `Art_Sales_Data_Analysis.xlsx`
- Project documentation: `README.md`, `DATA_DICTIONARY.md`
- Python analysis companion: `analysis/analyze_art_sales.py`
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
