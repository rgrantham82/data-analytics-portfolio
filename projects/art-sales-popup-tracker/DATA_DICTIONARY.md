# Data Dictionary — Art Sales Pop‑Up Tracker

This workbook is organized as two main tables:

- **Outings** (one row per outing)
- **Sales** (one row per sale line item)

## Outings sheet

Required fields are marked with *.

| Field | Meaning | Type / Example |
|---|---|---|
| Outing_ID* | Unique ID for the outing used to link Sales | `2026-01-30-Drag` |
| Date* | Date of outing | `2026-01-30` |
| Start_Time / End_Time | Optional time window | `14:00` |
| Duration_hrs (auto) | End - Start in hours | number |
| Day_of_Week (auto) | Day name from Date | text |
| City | City | `Austin` |
| Venue/Spot name* | Spot name | `UT Drag (Guadalupe)` |
| Area/Address | More precise location | text |
| Event_Type | Street pop-up / market / etc. | dropdown |
| Indoor/Outdoor | Indoor / Outdoor / Mixed | dropdown |
| Weather | Sunny / Cloudy / etc. | dropdown |
| Temp_F (optional) | Temperature | number |
| Foot_Traffic (1-5) | Subjective rating | 1–5 |
| Audience_Fit (1-5) | Subjective fit | 1–5 |
| Setup notes | Notes about setup | text |
| Inventory_Brought (#) | Count brought | number |
| Inventory_Sold (auto) | From Sales Qty by Outing_ID | number |
| Transactions (auto) | Count of transactions | number |
| Gross_Sales (auto) | Sum of totals before costs | currency |
| Discounts (manual) | Manual discount total (if needed) | currency |
| Tax_Collected (auto) | From Sales Tax | currency |
| Fees (booth/table) | Fixed fees | currency |
| Travel/Parking | Costs | currency |
| Supplies | Costs | currency |
| Net_Profit (auto) | Gross – costs – discounts + tax rules (as implemented) | currency |
| Top pieces / what sold | Qual notes | text |
| Top objections / friction | Qual notes | text |
| What worked | Qual notes | text |
| What to change next time | Qual notes | text |

## Sales sheet

Required fields are marked with *.

| Field | Meaning | Type / Example |
|---|---|---|
| Sale_ID | Optional unique identifier | `S-0001` |
| Date* | Sale date | `2026-01-30` |
| Outing_ID* | Links to Outings | `2026-01-30-Drag` |
| Time | Optional timestamp | `15:22` |
| Payment_Method | Cash/Card/Venmo/etc. | dropdown |
| Customer_Type | Student / Regular / etc. | text/dropdown |
| Followup? (Y/N) | Lead capture | Y/N |
| Product_Category | Original/Print/etc. | dropdown |
| Product_Name/Series | e.g., Magnolia Canticle | text |
| Size | e.g., 8x10 | text |
| Qty | Quantity | number |
| Unit_Price | Price per unit | currency |
| Discount_per_unit | Discount per unit | currency |
| COGS_per_unit (optional) | Cost basis per unit | currency |
| Subtotal (auto) | Qty*(Unit_Price-Discount) | currency |
| Tax | Sales tax | currency |
| Total (auto) | Subtotal + Tax | currency |
| Customer_Email (optional) | Lead email | text |
| Notes | Notes | text |
| Profit (auto) | (Unit_Price-Discount-COGS)*Qty (tax handling varies) | currency |

## Notes on analysis quality

- Use dropdowns whenever possible to prevent “Cashapp” vs “Cash App” style category splits.
- Keep Outing_ID consistent (same spelling in Outings and Sales).
- If you don’t track COGS, leave it blank — profit can be added later.
