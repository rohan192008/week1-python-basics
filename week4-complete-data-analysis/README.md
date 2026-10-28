# Week 4: Complete Data Analysis Project

## E-commerce sales analysis

This beginner-friendly project uses the supplied sales CSV to load, validate, clean, analyze, and visualize real records. It produces revenue metrics, three chart types, and a written report.

## Project contents

- `main.py` — analysis pipeline and chart/report generation
- `data/sales_data.csv` — supplied dataset
- `visualizations/` — generated product bar, monthly line, and regional pie charts
- `report/analysis_report.md` — findings, methodology, and learning reflection
- `requirements.txt` — Python libraries
- `test_cases.txt` — manual validation examples

## Setup and run

1. Install Python 3.10 or newer from [python.org](https://www.python.org/downloads/). On Windows, enable **Add Python to PATH** in the installer.
2. Open a terminal in this project folder.
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Run the analysis: `python main.py`
5. Open `report/analysis_report.md` and the PNG files in `visualizations/`.

The input CSV must be at `data/sales_data.csv`. Running the script recreates the charts and report.

## What I learned

I learned how Python programs run from top to bottom, how functions organize reusable steps, and how pandas reads CSV data and groups it for calculations. I practiced data validation and cleaning, then used Matplotlib bar, line, and pie charts to explain product, monthly, and regional patterns.

## Analysis design

The script checks required columns, parses dates and numbers, removes duplicate or invalid records, and recomputes revenue as quantity multiplied by price. It then groups sales by product, month, and region. The report highlights the top product, peak month, leading region, total revenue, units sold, average record revenue, and customer count.

## Validation

See `test_cases.txt` for expected checks and sample dataset totals. The report records the cleaned row count and explains cleaning decisions.
