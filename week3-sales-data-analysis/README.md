# Week 3: Introduction to Data Analysis — Sales Data Analysis

This project uses pandas to inspect and clean a sales CSV, calculate useful metrics, and write a formatted report.

## Project files

- `sales_analysis.py` — analysis script; writes `analysis_report.md`.
- `sales_data.csv` — the supplied sales dataset.
- `analysis_report.md` — findings calculated from the supplied data.
- `requirements.txt` — pandas dependency.
- `screenshots/sample_report.png` — a visual summary of the report.

## Dataset notes

The assignment brief describes five columns, while the supplied CSV contains seven: `Date`, `Product`, `Quantity`, `Price`, `Customer_ID`, `Region`, and `Total_Sales`. The analysis uses the columns found in the actual file and reports this difference.

## Setup and run

1. Install Python 3 from [python.org](https://www.python.org/downloads/).
2. Open a terminal in this project folder.
3. Install the dependency with `python -m pip install -r requirements.txt`.
4. Run `python sales_analysis.py` (or `python3 sales_analysis.py`).
5. Read the generated `analysis_report.md` in this folder.

The CSV must stay beside `sales_analysis.py` so the script can find it.

## Analysis steps

The script loads the CSV with `pandas.read_csv`, checks the required columns, counts missing values and exact duplicates, parses dates, converts numeric columns, removes rows that cannot support a reliable revenue calculation, labels optional blank customer/region values as `Unknown`, and recalculates line sales as `Quantity × Price`. It then summarizes revenue and units by product and revenue by region.

## Metrics

The report includes total revenue, number of order lines, total units, average order value, average units per order, best-selling product by quantity, top product by revenue, and product/region breakdowns.

## Manual validation examples

- Confirm the report's order count matches the number of usable CSV rows.
- Confirm `Total_Sales` equals `Quantity × Price` for each row; the script recomputes this value before totaling.
- Check that product revenue sums to the report's total revenue.
- If you make a copy of the CSV, blank a quantity or add an exact duplicate row and rerun the script to observe the cleanup counts.

## What I learned

This project practices loading CSV data, checking data quality, cleaning missing or duplicate records, converting data types, calculating summary statistics, and communicating results in a report.
