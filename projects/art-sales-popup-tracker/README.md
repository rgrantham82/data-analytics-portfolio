# Art Sales Pop‑Up Tracker (Excel) — Data Collection + Dashboard

This project is an Excel-based analytics system designed to capture pop‑up / street‑sale activity and automatically summarize results into a simple dashboard. It’s built for real‑world field conditions: fast entry, messy environments, and the need to learn what sells (and why) over repeated outings.

## What’s inside

**Workbook sheets**
- **Outings** — one row per outing (where/when you sold, conditions, costs, qualitative notes).
- **Sales** — one row per transaction line item (price, discount, COGS, payment method, etc.).
- **Dashboard** — auto-calculated KPIs + “Top outings by gross sales.”
- **Lookups** — dropdown lists used for data validation (payment method, product category, weather, etc.).
- **README** — in-workbook quick instructions.

## Key questions this tracker answers

- Which venues/spots generate the best *gross sales* and *net profit*?
- What’s the average gross per outing and transactions per outing?
- Which payment methods and product categories dominate?
- What objections show up most often, and what responses work?
- What’s the true profitability once fees, travel, supplies, and discounts are included?

## Data model (high level)

- **Outings** is the “parent” table keyed by `Outing_ID`.
- **Sales** is the “child” table keyed by `Outing_ID` (and optionally `Sale_ID`).
- Formulas aggregate Sales → Outings (transactions, gross, tax, profit), then Outings → Dashboard.

This mirrors a simple star schema: *FactSales* linked to *DimOuting*.

## Notable features

- **Dropdown validation lists** to reduce typos and improve analysis consistency.
- **Auto-calculated fields** for duration, day-of-week, subtotals, totals, and profit.
- **Net profit rollups** at the outing level including fees/travel/supplies.
- **Qualitative fields** (objections, what worked, what to change) to connect numbers to behavior.

## How to use (quick)

1. Add an outing in **Outings** (create a unique `Outing_ID`).
2. Log each transaction line in **Sales** and select the same `Outing_ID`.
3. The **Dashboard** updates automatically.

## Skills demonstrated

- KPI definition and metric design (gross vs net, transactions, discounting, COGS).
- Spreadsheet engineering (structured tables, data validation, formulas, rollups).
- Data modeling mindset (relational structure inside a spreadsheet).
- “Analytics UX” (making field entry fast and analysis reliable).

## Next improvements (planned)

- Pivot/Power Query refresh pipeline for deeper slicing (by venue, category, weekday, season).
- Automated charts (trend lines, venue rankings, payment mix, profit waterfall).
- Export to CSV + Python notebook for EDA and forecasting.

## Screenshots

Add screenshots in `/assets/` and embed them here once captured.

## File

- `Art_Sales_Data_Analysis.xlsx`


## Python companion

If you want to demonstrate Excel + Python together, see `/analysis/`.
