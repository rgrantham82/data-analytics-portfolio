"""Art Sales Pop-Up Tracker — Python EDA Companion

Reads either the Excel workbook or exported CSVs and writes KPIs, an
outing-level summary, and a few charts.

Usage:
    python analysis/analyze_art_sales.py [PROJECT_DIR]

PROJECT_DIR defaults to the folder that contains this script's parent
(i.e. the project root), so the script works no matter where you run it from.
It looks for, in order of preference:
  - outings.csv and sales.csv
  - Art_Sales_Data_Analysis.xlsx

Outputs (written to PROJECT_DIR/analysis_outputs/):
  - kpis.csv
  - outing_summary.csv
  - *.png charts
"""

import argparse
import os
import re
import sys

import matplotlib
matplotlib.use("Agg")  # no display in CI / headless shells; must precede pyplot

import matplotlib.pyplot as plt
import pandas as pd

WORKBOOK_NAME = "Art_Sales_Data_Analysis.xlsx"


def resolve_project_dir(explicit: str | None = None) -> str:
    """Locate the project root.

    Previously this was ``os.path.abspath('.')``, which broke whenever the
    script or notebook was launched from the ``analysis/`` folder — the
    workbook lives one level up. Search upward instead.
    """
    if explicit:
        return os.path.abspath(explicit)

    here = os.path.dirname(os.path.abspath(__file__))
    for candidate in (here, os.path.dirname(here), os.getcwd()):
        if os.path.exists(os.path.join(candidate, WORKBOOK_NAME)):
            return candidate
        if all(
            os.path.exists(os.path.join(candidate, name))
            for name in ("outings.csv", "sales.csv")
        ):
            return candidate

    # Nothing found; fall back to the script's parent so the error message
    # below names a sensible path.
    return os.path.dirname(here)


def _snake(col: str) -> str:
    col = str(col).replace("*", "").strip()
    col = re.sub(r"\(auto\)|\(optional\)", "", col, flags=re.I).strip()
    col = re.sub(r"[^0-9a-zA-Z]+", "_", col)
    col = re.sub(r"_+", "_", col).strip("_").lower()
    return col


def load_data(project_dir: str):
    outings_csv = os.path.join(project_dir, "outings.csv")
    sales_csv = os.path.join(project_dir, "sales.csv")
    excel_path = os.path.join(project_dir, WORKBOOK_NAME)

    if os.path.exists(outings_csv) and os.path.exists(sales_csv):
        outings = pd.read_csv(outings_csv)
        sales = pd.read_csv(sales_csv)
    elif os.path.exists(excel_path):
        outings = pd.read_excel(excel_path, sheet_name="Outings")
        sales = pd.read_excel(excel_path, sheet_name="Sales")
    else:
        raise FileNotFoundError(
            f"Looked in {project_dir} for outings.csv + sales.csv or {WORKBOOK_NAME}, "
            "and found neither. Pass the project folder explicitly: "
            "python analysis/analyze_art_sales.py /path/to/art-sales-popup-tracker"
        )

    outings.columns = [_snake(c) for c in outings.columns]
    sales.columns = [_snake(c) for c in sales.columns]

    # Drop the blank template rows that carry formulas but no data
    if "outing_id" in outings.columns:
        outings = outings.dropna(subset=["outing_id"])
    if "outing_id" in sales.columns:
        sales = sales.dropna(subset=["outing_id"])

    for frame in (outings, sales):
        if "date" in frame.columns:
            frame["date"] = pd.to_datetime(frame["date"], errors="coerce")

    outing_numeric = [
        "gross_sales", "net_profit", "fees", "travel_parking",
        "supplies", "tax_collected", "discounts", "duration_hrs",
    ]
    sales_numeric = [
        "qty", "unit_price", "discount_per_unit", "cogs_per_unit",
        "subtotal", "tax", "total", "profit",
    ]
    for col in outing_numeric:
        if col in outings.columns:
            outings[col] = pd.to_numeric(outings[col], errors="coerce")
    for col in sales_numeric:
        if col in sales.columns:
            sales[col] = pd.to_numeric(sales[col], errors="coerce")

    return outings, sales


def compute_kpis(outings: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    kpis = {}
    kpis["outings_count"] = (
        int(outings["outing_id"].nunique())
        if "outing_id" in outings.columns
        else len(outings)
    )
    kpis["transactions_count"] = (
        int(sales["sale_id"].nunique())
        if "sale_id" in sales.columns and sales["sale_id"].notna().any()
        else int(len(sales))
    )
    kpis["gross_sales_total"] = (
        float(outings["gross_sales"].sum())
        if "gross_sales" in outings.columns
        else float(sales["total"].sum()) if "total" in sales.columns
        else float("nan")
    )

    if "net_profit" in outings.columns:
        kpis["net_profit_total"] = float(outings["net_profit"].sum())
    elif "profit" in sales.columns:
        kpis["net_profit_total"] = float(sales["profit"].sum())
    else:
        kpis["net_profit_total"] = float("nan")

    total_hours = (
        outings["duration_hrs"].sum(skipna=True)
        if "duration_hrs" in outings.columns
        else None
    )
    if total_hours and total_hours > 0:
        kpis["total_hours"] = float(total_hours)
        kpis["gross_per_hour"] = kpis["gross_sales_total"] / total_hours
        kpis["profit_per_hour"] = kpis["net_profit_total"] / total_hours
    else:
        kpis["total_hours"] = float("nan")
        kpis["gross_per_hour"] = float("nan")
        kpis["profit_per_hour"] = float("nan")

    count = kpis["outings_count"]
    kpis["avg_gross_per_outing"] = kpis["gross_sales_total"] / count if count else float("nan")
    kpis["avg_profit_per_outing"] = kpis["net_profit_total"] / count if count else float("nan")
    return pd.DataFrame([kpis])


def outing_summary(outings: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    out = outings.copy()

    can_join = "outing_id" in out.columns and "outing_id" in sales.columns
    if not can_join:
        return out

    if "gross_sales" not in out.columns and "total" in sales.columns:
        # Build the aggregation spec explicitly. The previous inline
        # `('tax','sum') if 'tax' in ... else ('total','size')` fallback
        # silently produced a *row count* under the name `tax_collected`.
        agg_spec = {"gross_sales": ("total", "sum"), "line_items": ("total", "size")}
        if "tax" in sales.columns:
            agg_spec["tax_collected"] = ("tax", "sum")
        if "qty" in sales.columns:
            agg_spec["items_sold"] = ("qty", "sum")

        roll = sales.groupby("outing_id", dropna=False).agg(**agg_spec).reset_index()
        out = out.merge(roll, on="outing_id", how="left")

    if "net_profit" not in out.columns and "profit" in sales.columns:
        prof = (
            sales.groupby("outing_id", dropna=False)["profit"]
            .sum()
            .reset_index()
            .rename(columns={"profit": "net_profit"})
        )
        out = out.merge(prof, on="outing_id", how="left")

    if "venue_spot_name" in out.columns:
        out["venue_spot_name"] = out["venue_spot_name"].astype(str).str.strip()

    if "date" in out.columns:
        out = out.sort_values("date")

    return out


def _save(fig_path: str):
    plt.tight_layout()
    plt.savefig(fig_path, dpi=200)
    plt.close()


def save_charts(out_summary: pd.DataFrame, sales: pd.DataFrame, outdir: str):
    os.makedirs(outdir, exist_ok=True)

    if {"venue_spot_name", "gross_sales"} <= set(out_summary.columns):
        top = (
            out_summary.groupby("venue_spot_name", dropna=False)["gross_sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
        )
        if not top.empty:
            ax = top.plot(kind="bar")
            ax.set_title("Top Venues by Gross Sales")
            ax.set_xlabel("Venue")
            ax.set_ylabel("Gross Sales")
            _save(os.path.join(outdir, "top_venues_gross_sales.png"))

    if {"date", "gross_sales"} <= set(out_summary.columns):
        trend = (
            out_summary.dropna(subset=["date"])
            .groupby("date")["gross_sales"]
            .sum()
            .sort_index()
        )
        if not trend.empty:
            ax = trend.plot(kind="line", marker="o")
            ax.set_title("Gross Sales Over Time")
            ax.set_xlabel("Date")
            ax.set_ylabel("Gross Sales")
            _save(os.path.join(outdir, "gross_sales_over_time.png"))

    if "payment_method" in sales.columns:
        pm_counts = (
            sales["payment_method"].fillna("Unknown").astype(str).str.strip()
            .value_counts().head(10)
        )
        if not pm_counts.empty:
            ax = pm_counts.plot(kind="bar")
            ax.set_title("Payment Method Counts (Top 10)")
            ax.set_xlabel("Payment Method")
            ax.set_ylabel("Count")
            _save(os.path.join(outdir, "payment_method_counts.png"))


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "project_dir",
        nargs="?",
        default=None,
        help="Folder containing the workbook or the exported CSVs.",
    )
    args = parser.parse_args(argv)

    project_dir = resolve_project_dir(args.project_dir)
    outings, sales = load_data(project_dir)

    if outings.empty and sales.empty:
        print("No rows found — the tracker looks empty. Log an outing first.")
        return 1

    kpis = compute_kpis(outings, sales)
    out_sum = outing_summary(outings, sales)

    outdir = os.path.join(project_dir, "analysis_outputs")
    os.makedirs(outdir, exist_ok=True)

    kpis.to_csv(os.path.join(outdir, "kpis.csv"), index=False)
    out_sum.to_csv(os.path.join(outdir, "outing_summary.csv"), index=False)
    save_charts(out_sum, sales, outdir)

    print(f"Done. {len(outings)} outings, {len(sales)} sales lines.")
    print("Outputs in:", outdir)
    return 0


if __name__ == "__main__":
    sys.exit(main())
