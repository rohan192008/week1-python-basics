# Sales Data Analysis Report

**Source:** `sales_data.csv`  
**Analysis period:** 2024-01-01 to 2024-04-09

## Dataset overview

- Records loaded: 100
- Records analyzed: 100
- Columns in source file: 7 source columns
- Duplicate rows removed: 0
- Rows removed for missing or invalid date/product/quantity/price: 0
- Missing cells after cleaning: 0
- Sales totals corrected using Quantity × Price: 0

The assignment brief describes a five-column dataset. The supplied CSV contains 7 original columns: Date, Product, Quantity, Price, Customer_ID, Region, Total_Sales. The analysis uses the columns that are actually present.

### Columns and cleaned data types

| Column | Data type |
| --- | --- |
| `Date` | `datetime64[us]` |
| `Product` | `string` |
| `Quantity` | `int64` |
| `Price` | `int64` |
| `Customer_ID` | `string` |
| `Region` | `string` |
| `Total_Sales` | `int64` |

### First five records

| Date | Product | Quantity | Price | Total sales |
| --- | --- | ---: | ---: | ---: |
| 2024-01-01 | Phone | 7 | ₹37,300.00 | ₹261,100.00 |
| 2024-01-02 | Headphones | 4 | ₹15,406.00 | ₹61,624.00 |
| 2024-01-03 | Phone | 2 | ₹21,746.00 | ₹43,492.00 |
| 2024-01-04 | Headphones | 1 | ₹30,895.00 | ₹30,895.00 |
| 2024-01-05 | Laptop | 8 | ₹39,835.00 | ₹318,680.00 |

## Key metrics

- **Total revenue:** ₹12,365,048.00
- **Orders analyzed:** 100
- **Units sold:** 478
- **Average order value:** ₹123,650.48
- **Average units per order:** 4.78
- **Best-selling product by units:** Laptop (136 units)
- **Top product by revenue:** Laptop (₹3,889,210.00)

## Revenue by product

| Product | Units sold | Revenue |
| --- | ---: | ---: |
| Laptop | 136 | ₹3,889,210.00 |
| Tablet | 127 | ₹2,884,340.00 |
| Phone | 101 | ₹2,859,394.00 |
| Headphones | 48 | ₹1,384,033.00 |
| Monitor | 66 | ₹1,348,071.00 |

## Revenue by region

| Region | Revenue |
| --- | ---: |
| North | ₹3,983,635.00 |
| South | ₹3,737,852.00 |
| East | ₹2,519,639.00 |
| West | ₹2,123,922.00 |

## Cleaning and analysis method

1. Read the CSV with pandas and inspect its columns, data types, missing values, and duplicate rows.
2. Remove exact duplicate records; parse dates; convert quantity, price, and reported sales to numeric values.
3. Exclude rows without a valid date, product, quantity, or price because they cannot support a reliable line-item revenue calculation. Fill blank customer or region labels with `Unknown` when those columns exist.
4. Recalculate line-item sales as `Quantity × Price` and use that result for revenue metrics.
5. Summarize revenue and units by product, then sort to identify leaders.

## Findings

The dataset contains 100 usable sales records and 478 units. Total calculated revenue is ₹12,365,048.00. Laptop leads by quantity with 136 units. Laptop leads by revenue at ₹3,889,210.00.

## Limitations

The report treats each row as one order line. Currency is shown in rupees to match the assignment example; the CSV itself does not include a currency column. No claim is made about profit because costs are not provided.
