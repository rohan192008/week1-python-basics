"""Analyze the sample sales data and create charts plus a Markdown report."""
from pathlib import Path
import sys

import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "sales_data.csv"
CHART_DIR = ROOT / "visualizations"
REPORT_FILE = ROOT / "report" / "analysis_report.md"
REQUIRED = {"Date", "Product", "Quantity", "Price", "Customer_ID", "Region", "Total_Sales"}


def load_and_clean(path: Path) -> pd.DataFrame:
    """Load the CSV, validate columns, clean values, and return usable records."""
    if not path.is_file():
        raise FileNotFoundError(f"Could not find the dataset: {path}")
    data = pd.read_csv(path)
    missing_columns = REQUIRED - set(data.columns)
    if missing_columns:
        raise ValueError(f"CSV is missing required columns: {', '.join(sorted(missing_columns))}")
    if data.empty:
        raise ValueError("The CSV has a header but no sales rows.")

    data = data.drop_duplicates().copy()
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    for column in ("Quantity", "Price", "Total_Sales"):
        data[column] = pd.to_numeric(data[column], errors="coerce")
    data["Product"] = data["Product"].astype("string").str.strip()
    data["Region"] = data["Region"].astype("string").str.strip().fillna("Unknown")
    data = data.dropna(subset=["Date", "Product", "Quantity", "Price"])
    data = data[(data["Product"] != "") & (data["Quantity"] >= 0) & (data["Price"] >= 0)]
    # Recalculate sales so the analysis is consistent even if the supplied total is wrong.
    data["Total_Sales"] = data["Quantity"] * data["Price"]
    if data.empty:
        raise ValueError("No valid sales rows remain after cleaning.")
    return data


def make_charts(data: pd.DataFrame) -> dict:
    """Create a product bar chart, monthly line chart, and regional pie chart."""
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    plt.style.use("seaborn-v0_8-whitegrid")
    colors = ["#2563EB", "#0F766E", "#F59E0B", "#9333EA", "#DC2626"]

    by_product = data.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(9, 5.2))
    bars = ax.bar(by_product.index, by_product.values, color=colors[:len(by_product)])
    ax.set(title="Revenue by Product", ylabel="Revenue (₹)", xlabel="Product")
    ax.ticklabel_format(axis="y", style="plain")
    ax.bar_label(bars, labels=[f"₹{v:,.0f}" for v in by_product.values], padding=4, fontsize=8)
    fig.tight_layout()
    fig.savefig(CHART_DIR / "product_revenue.png", dpi=160, bbox_inches="tight")
    plt.close(fig)

    by_month = data.set_index("Date").resample("MS")["Total_Sales"].sum()
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.plot(by_month.index, by_month.values, marker="o", linewidth=2.8, color="#2563EB")
    ax.fill_between(by_month.index, by_month.values, alpha=0.12, color="#2563EB")
    ax.set(title="Monthly Revenue Trend", ylabel="Revenue (₹)", xlabel="Month")
    ax.ticklabel_format(axis="y", style="plain")
    ax.set_xticks(by_month.index, [d.strftime("%b %Y") for d in by_month.index])
    fig.tight_layout()
    fig.savefig(CHART_DIR / "monthly_revenue.png", dpi=160, bbox_inches="tight")
    plt.close(fig)

    by_region = data.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.pie(by_region.values, labels=by_region.index, autopct="%1.1f%%", startangle=90,
           colors=["#2563EB", "#0F766E", "#F59E0B", "#9333EA", "#DC2626"],
           wedgeprops={"edgecolor": "white", "linewidth": 1.5})
    ax.set_title("Revenue Share by Region")
    fig.tight_layout()
    fig.savefig(CHART_DIR / "regional_revenue.png", dpi=160, bbox_inches="tight")
    plt.close(fig)
    return {"product": by_product, "month": by_month, "region": by_region}


def write_report(data: pd.DataFrame, groups: dict, original_rows: int) -> None:
    revenue = data["Total_Sales"].sum()
    units = data["Quantity"].sum()
    customers = data["Customer_ID"].nunique()
    average = revenue / len(data)
    best_product = groups["product"].index[0]
    best_region = groups["region"].index[0]
    peak_month = groups["month"].idxmax().strftime("%B %Y")
    rows_removed = original_rows - len(data)
    lines = [
        "# Sales Data Analysis Report", "",
        "## Project overview", "",
        "This project analyzes the supplied e-commerce sales CSV with pandas, cleans and validates the records, calculates useful metrics, and creates charts with Matplotlib.", "",
        "## Dataset and cleaning", "",
        f"- Valid sales records analyzed: **{len(data)}** (input rows: {original_rows}; removed during cleaning: {rows_removed}).",
        f"- Date range: **{data['Date'].min():%d %b %Y} – {data['Date'].max():%d %b %Y}**.",
        "- Required columns and numeric values are validated. Duplicate rows are removed; invalid dates, missing products, and negative quantities or prices are excluded.",
        "- Revenue is recalculated as `Quantity × Price` so totals are consistent.", "",
        "## Key metrics", "",
        f"- Total revenue: **₹{revenue:,.2f}**",
        f"- Units sold: **{units:,.0f}**",
        f"- Average revenue per record: **₹{average:,.2f}**",
        f"- Distinct customers: **{customers:,}**",
        f"- Top product by revenue: **{best_product}** (₹{groups['product'].iloc[0]:,.2f})",
        f"- Highest revenue region: **{best_region}** (₹{groups['region'].iloc[0]:,.2f})",
        f"- Highest revenue month: **{peak_month}** (₹{groups['month'].max():,.2f})", "",
        "## Visualizations", "",
        "![Revenue by product](../visualizations/product_revenue.png)", "",
        "![Monthly revenue trend](../visualizations/monthly_revenue.png)", "",
        "![Revenue share by region](../visualizations/regional_revenue.png)", "",
        "## Insights", "",
        f"1. **{best_product}** is the largest revenue contributor; its total is ₹{groups['product'].iloc[0]:,.2f}.",
        f"2. **{peak_month}** is the strongest month by revenue. Monthly totals can be affected by the partial first or last month in the dataset.",
        f"3. **{best_region}** leads regional revenue at ₹{groups['region'].iloc[0]:,.2f}; the pie chart shows how sales are distributed across regions.", "",
        "## How to run", "",
        "From this project folder, install dependencies with `python -m pip install -r requirements.txt`, then run `python main.py`. The script regenerates all three PNG charts and this report.", "",
        "## Learning reflection", "",
        "I practiced loading CSV files with pandas, checking data quality, grouping and summarizing records, and communicating patterns with bar, line, and pie charts. I also used functions and clear validation errors to make the program easier to reuse.", "",
    ]
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    try:
        raw = pd.read_csv(DATA_FILE)
        original_rows = len(raw)
        data = load_and_clean(DATA_FILE)
        groups = make_charts(data)
        write_report(data, groups, original_rows)
        print("Sales analysis complete!")
        print(f"Valid records: {len(data)}")
        print(f"Total revenue: ₹{data['Total_Sales'].sum():,.2f}")
        print(f"Top product: {groups['product'].index[0]}")
        print(f"Charts saved in: {CHART_DIR}")
        print(f"Report saved to: {REPORT_FILE}")
        return 0
    except (OSError, ValueError, pd.errors.ParserError) as error:
        print(f"Unable to complete the analysis: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
