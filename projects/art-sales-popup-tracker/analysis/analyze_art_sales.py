"""Art Sales Pop‑Up Tracker — Python EDA Companion

Run from the folder that contains:
- Art_Sales_Data_Analysis.xlsx  (preferred) OR
- outings.csv and sales.csv

Outputs:
- analysis_outputs/kpis.csv
- analysis_outputs/outing_summary.csv
- analysis_outputs/*.png charts
"""

import os
import re
import pandas as pd
import matplotlib.pyplot as plt

PROJECT_DIR = os.path.abspath('.')
EXCEL_PATH = os.path.join(PROJECT_DIR, 'Art_Sales_Data_Analysis.xlsx')
OUTINGS_CSV = os.path.join(PROJECT_DIR, 'outings.csv')
SALES_CSV = os.path.join(PROJECT_DIR, 'sales.csv')

def _snake(col: str) -> str:
    col = str(col).replace('*','').strip()
    col = re.sub(r"\(auto\)|\(optional\)", "", col, flags=re.I).strip()
    col = re.sub(r"[^0-9a-zA-Z]+", "_", col)
    col = re.sub(r"_+", "_", col).strip('_').lower()
    return col

def load_data():
    if os.path.exists(OUTINGS_CSV) and os.path.exists(SALES_CSV):
        outings = pd.read_csv(OUTINGS_CSV)
        sales = pd.read_csv(SALES_CSV)
    elif os.path.exists(EXCEL_PATH):
        outings = pd.read_excel(EXCEL_PATH, sheet_name='Outings')
        sales = pd.read_excel(EXCEL_PATH, sheet_name='Sales')
    else:
        raise FileNotFoundError('Missing outings.csv/sales.csv and Art_Sales_Data_Analysis.xlsx')

    outings.columns = [_snake(c) for c in outings.columns]
    sales.columns = [_snake(c) for c in sales.columns]

    if 'date' in outings.columns:
        outings['date'] = pd.to_datetime(outings['date'], errors='coerce')
    if 'date' in sales.columns:
        sales['date'] = pd.to_datetime(sales['date'], errors='coerce')

    for col in ['gross_sales', 'net_profit', 'fees', 'travel_parking', 'supplies', 'tax_collected', 'discounts', 'duration_hrs']:
        if col in outings.columns:
            outings[col] = pd.to_numeric(outings[col], errors='coerce')

    for col in ['qty','unit_price','discount_per_unit','cogs_per_unit','subtotal','tax','total','profit']:
        if col in sales.columns:
            sales[col] = pd.to_numeric(sales[col], errors='coerce')

    return outings, sales

def compute_kpis(outings: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    kpis = {}
    kpis['outings_count'] = outings['outing_id'].nunique() if 'outing_id' in outings.columns else len(outings)
    kpis['transactions_count'] = int(sales['sale_id'].nunique()) if 'sale_id' in sales.columns and sales['sale_id'].notna().any() else int(len(sales))
    kpis['gross_sales_total'] = float(outings['gross_sales'].sum()) if 'gross_sales' in outings.columns else float(sales['total'].sum())
    if 'net_profit' in outings.columns:
        kpis['net_profit_total'] = float(outings['net_profit'].sum())
    elif 'profit' in sales.columns:
        kpis['net_profit_total'] = float(sales['profit'].sum())
    else:
        kpis['net_profit_total'] = float('nan')

    if 'duration_hrs' in outings.columns:
        total_hours = outings['duration_hrs'].sum(skipna=True)
        kpis['total_hours'] = float(total_hours) if pd.notna(total_hours) else float('nan')
        kpis['gross_per_hour'] = kpis['gross_sales_total'] / total_hours if total_hours and total_hours > 0 else float('nan')
        kpis['profit_per_hour'] = kpis['net_profit_total'] / total_hours if total_hours and total_hours > 0 else float('nan')
    else:
        kpis['total_hours'] = float('nan')
        kpis['gross_per_hour'] = float('nan')
        kpis['profit_per_hour'] = float('nan')

    kpis['avg_gross_per_outing'] = kpis['gross_sales_total'] / kpis['outings_count'] if kpis['outings_count'] else float('nan')
    kpis['avg_profit_per_outing'] = kpis['net_profit_total'] / kpis['outings_count'] if kpis['outings_count'] else float('nan')
    return pd.DataFrame([kpis])

def outing_summary(outings: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    out = outings.copy()
    if 'gross_sales' not in out.columns and 'total' in sales.columns:
        roll = sales.groupby('outing_id', dropna=False).agg(
            gross_sales=('total','sum'),
            tax_collected=('tax','sum') if 'tax' in sales.columns else ('total','size'),
            items_sold=('qty','sum') if 'qty' in sales.columns else ('total','size'),
            line_items=('total','size')
        ).reset_index()
        out = out.merge(roll, on='outing_id', how='left')

    if 'net_profit' not in out.columns and 'profit' in sales.columns:
        prof = sales.groupby('outing_id', dropna=False)['profit'].sum().reset_index().rename(columns={'profit':'net_profit'})
        out = out.merge(prof, on='outing_id', how='left')

    if 'venue_spot_name' in out.columns:
        out['venue_spot_name'] = out['venue_spot_name'].astype(str).str.strip()

    if 'date' in out.columns:
        out = out.sort_values('date')

    return out

def save_charts(out_summary: pd.DataFrame, sales: pd.DataFrame, outdir: str):
    os.makedirs(outdir, exist_ok=True)

    if 'venue_spot_name' in out_summary.columns and 'gross_sales' in out_summary.columns:
        top = (out_summary.groupby('venue_spot_name', dropna=False)['gross_sales']
               .sum().sort_values(ascending=False).head(10))
        ax = top.plot(kind='bar')
        ax.set_title('Top Venues by Gross Sales')
        ax.set_xlabel('Venue')
        ax.set_ylabel('Gross Sales')
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, 'top_venues_gross_sales.png'), dpi=200)
        plt.close()

    if 'date' in out_summary.columns and 'gross_sales' in out_summary.columns:
        trend = out_summary.dropna(subset=['date']).groupby('date')['gross_sales'].sum().sort_index()
        ax = trend.plot(kind='line', marker='o')
        ax.set_title('Gross Sales Over Time')
        ax.set_xlabel('Date')
        ax.set_ylabel('Gross Sales')
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, 'gross_sales_over_time.png'), dpi=200)
        plt.close()

    if 'payment_method' in sales.columns:
        pm = sales['payment_method'].fillna('Unknown').astype(str).str.strip()
        pm_counts = pm.value_counts().head(10)
        ax = pm_counts.plot(kind='bar')
        ax.set_title('Payment Method Counts (Top 10)')
        ax.set_xlabel('Payment Method')
        ax.set_ylabel('Count')
        plt.tight_layout()
        plt.savefig(os.path.join(outdir, 'payment_method_counts.png'), dpi=200)
        plt.close()

def main():
    outings, sales = load_data()
    kpis = compute_kpis(outings, sales)
    out_sum = outing_summary(outings, sales)

    outdir = os.path.join(PROJECT_DIR, 'analysis_outputs')
    os.makedirs(outdir, exist_ok=True)

    kpis.to_csv(os.path.join(outdir, 'kpis.csv'), index=False)
    out_sum.to_csv(os.path.join(outdir, 'outing_summary.csv'), index=False)

    save_charts(out_sum, sales, outdir)
    print('Done. Outputs in:', outdir)

if __name__ == '__main__':
    main()
