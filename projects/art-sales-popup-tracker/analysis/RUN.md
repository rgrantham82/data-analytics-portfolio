# Python Companion (optional)

If you want to show both Excel *and* Python in your portfolio, use this folder.

## Option A: Run directly on the Excel workbook

Place `Art_Sales_Data_Analysis.xlsx` in the project root and run:

```bash
python analysis/analyze_art_sales.py
```

Outputs will be written to `analysis_outputs/` (CSVs + PNG charts).

## Option B: Export to CSV first

Export the **Outings** sheet to `outings.csv` and the **Sales** sheet to `sales.csv` (same folder as the workbook),
then run the same script. The script will prefer CSVs if they exist.

## Notebook

Open `analysis/Art_Sales_EDA_Companion.ipynb` and run cells top to bottom.
