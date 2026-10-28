"""Analyze the supplied sales CSV and write a readable Markdown report."""

from pathlib import Path

import pandas as pd


PROJECT_DIR = Path(__file__).resolve().parent
DATA_FILE = PROJECT_DIR / "sales_data.csv"
REPORT_FILE = PROJECT_DIR / "analysis_report.md"
REQUIRED_COLUMNS = {"Date", "Product", "Quantity", "Price", "Total_Sales"}
NUMERIC_COLUMNS = ["Quantity", "Price", "Total_Sales"]


def load_and_clean_data(file_path):
    """Load the CSV, standardize fields, remove unusable rows, and derive sales."""
    data = pd.read_csv(file_path)
    rows_loaded = len(data)

    missing_before = data.isna().sum()
    duplicates_removed = int(data.duplicated().sum())
    data = data.drop_duplicates().copy()

    missing_columns = REQUIRED_COLUMNS - set(data.columns)
    if missing_columns:
        raise ValueError(
            "The CSV is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )

    data["Product"] = data["Product"].astype("string").str.strip()
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    for column in NUMERIC_COLUMNS:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    # These fields are needed to calculate a trustworthy revenue value.
    required_values = ["Date", "Product", "Quantity", "Price"]
    rows_before_required_cleanup = len(data)
    data = data.dropna(subset=required_values).copy()
    data = data[data["Product"].ne("")].copy()
    rows_removed = rows_before_required_cleanup - len(data)

    # Optional descriptive fields do not affect sales totals, so label blanks.
    for column in ["Customer_ID", "Region"]:
        if column in data.columns:
            data[column] = data[column].fillna("Unknown").astype("string").str.strip()
            data.loc[data[column].eq(""), column] = "Unknown"

    # Quantity × price is the single source of truth for calculated revenue.
    data["Calculated_Sales"] = data["Quantity"] * data["Price"]
    original_total = data["Total_Sales"]
    sales_mismatches = int(
        (original_total.notna() & original_total.ne(data["Calculated_Sales"])).sum()
    )
    data["Total_Sales"] = data["Calculated_Sales"]

    cleaning = {
        "rows_loaded": rows_loaded,
        "duplicates_removed": duplicates_removed,
        "rows_removed_for_missing_or_invalid_required_values": rows_removed,
        "missing_values_before_cleaning": {
            str(column): int(count) for column, count in missing_before.items()
        },
        "sales_value_mismatches_corrected": sales_mismatches,
    }
    return data, cleaning


def build_report(data, cleaning, source_name):
    """Create a Markdown report with dataset checks and sales metrics."""
    total_revenue = float(data["Total_Sales"].sum())
    total_units = float(data["Quantity"].sum())
    order_count = int(len(data))
    average_order_value = total_revenue / order_count if order_count else 0
    average_units_per_order = total_units / order_count if order_count else 0
    best_by_units = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
    best_by_revenue = data.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
    region_revenue = (
        data.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
        if "Region" in data.columns
        else pd.Series(dtype="float64")
    )
    missing_after = int(data.isna().sum().sum())
    date_start = data["Date"].min().date() if order_count else "N/A"
    date_end = data["Date"].max().date() if order_count else "N/A"

    lines = [
        "# Sales Data Analysis Report",
        "",
        f"**Source:** `{source_name}`  ",
        f"**Analysis period:** {date_start} to {date_end}",
        "",
        "## Dataset overview",
        "",
        f"- Records loaded: {cleaning['rows_loaded']}",
        f"- Records analyzed: {order_count}",
        f"- Columns in source file: {len(data.columns) - 1} source columns",
        f"- Duplicate rows removed: {cleaning['duplicates_removed']}",
        "- Rows removed for missing or invalid date/product/quantity/price: "
        f"{cleaning['rows_removed_for_missing_or_invalid_required_values']}",
        f"- Missing cells after cleaning: {missing_after}",
        f"- Sales totals corrected using Quantity × Price: "
        f"{cleaning['sales_value_mismatches_corrected']}",
        "",
        "The assignment brief describes a five-column dataset. The supplied CSV "
        f"contains {len(data.columns) - 1} original columns: "
        + ", ".join(column for column in data.columns if column != "Calculated_Sales")
        + ". The analysis uses the columns that are actually present.",
        "",
        "## Key metrics",
        "",
        f"- **Total revenue:** ₹{total_revenue:,.2f}",
        f"- **Orders analyzed:** {order_count:,}",
        f"- **Units sold:** {total_units:,.0f}",
        f"- **Average order value:** ₹{average_order_value:,.2f}",
        f"- **Average units per order:** {average_units_per_order:,.2f}",
        f"- **Best-selling product by units:** {best_by_units.index[0]} "
        f"({best_by_units.iloc[0]:,.0f} units)" if not best_by_units.empty else "- **Best-selling product by units:** N/A",
        f"- **Top product by revenue:** {best_by_revenue.index[0]} "
        f"(₹{best_by_revenue.iloc[0]:,.2f})" if not best_by_revenue.empty else "- **Top product by revenue:** N/A",
        "",
        "## Revenue by product",
        "",
        "| Product | Units sold | Revenue |",
        "| --- | ---: | ---: |",
    ]
    # Add the cleaned schema and a small preview to make exploration visible.
    overview_index = lines.index("## Key metrics")
    schema_and_preview = [
        "### Columns and cleaned data types",
        "",
        "| Column | Data type |",
        "| --- | --- |",
    ]
    for column in data.columns:
        if column != "Calculated_Sales":
            schema_and_preview.append(f"| `{column}` | `{data[column].dtype}` |")
    schema_and_preview += [
        "",
        "### First five records",
        "",
        "| Date | Product | Quantity | Price | Total sales |",
        "| --- | --- | ---: | ---: | ---: |",
    ]
    for _, row in data.head(5).iterrows():
        schema_and_preview.append(
            f"| {row['Date'].date()} | {row['Product']} | {row['Quantity']:,.0f} | "
            f"₹{row['Price']:,.2f} | ₹{row['Total_Sales']:,.2f} |"
        )
    schema_and_preview.append("")
    lines[overview_index:overview_index] = schema_and_preview

    for product, revenue in best_by_revenue.items():
        units = best_by_units.get(product, 0)
        lines.append(f"| {product} | {units:,.0f} | ₹{revenue:,.2f} |")

    if not region_revenue.empty:
        lines += ["", "## Revenue by region", "", "| Region | Revenue |", "| --- | ---: |"]
        for region, revenue in region_revenue.items():
            lines.append(f"| {region} | ₹{revenue:,.2f} |")

    lines += [
        "",
        "## Cleaning and analysis method",
        "",
        "1. Read the CSV with pandas and inspect its columns, data types, missing values, and duplicate rows.",
        "2. Remove exact duplicate records; parse dates; convert quantity, price, and reported sales to numeric values.",
        "3. Exclude rows without a valid date, product, quantity, or price because they cannot support a reliable line-item revenue calculation. Fill blank customer or region labels with `Unknown` when those columns exist.",
        "4. Recalculate line-item sales as `Quantity × Price` and use that result for revenue metrics.",
        "5. Summarize revenue and units by product, then sort to identify leaders.",
        "",
        "## Findings",
        "",
        f"The dataset contains {order_count} usable sales records and {total_units:,.0f} units. "
        f"Total calculated revenue is ₹{total_revenue:,.2f}. "
        + (f"{best_by_units.index[0]} leads by quantity with {best_by_units.iloc[0]:,.0f} units. " if not best_by_units.empty else "")
        + (f"{best_by_revenue.index[0]} leads by revenue at ₹{best_by_revenue.iloc[0]:,.2f}." if not best_by_revenue.empty else ""),
        "",
        "## Limitations",
        "",
        "The report treats each row as one order line. Currency is shown in rupees to match the assignment example; the CSV itself does not include a currency column. No claim is made about profit because costs are not provided.",
        "",
    ]
    return "\n".join(lines)


def main():
    """Load the project CSV and save the analysis report beside this script."""
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Could not find the dataset: {DATA_FILE}")

    data, cleaning = load_and_clean_data(DATA_FILE)
    report = build_report(data, cleaning, DATA_FILE.name)
    REPORT_FILE.write_text(report, encoding="utf-8")
    print(f"Analysis complete. Report saved to: {REPORT_FILE.name}")


if __name__ == "__main__":
    main()
