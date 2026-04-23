import pandas as pd

# Load Excel file
data = pd.read_excel("sales_data.xlsx")

print("\nOriginal Excel Data:")
print(data)

# Calculate total sales
total_sales = data["Sales"].sum()

print("\nTotal Sales:", total_sales)

# Sales by product
product_sales = data.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(product_sales)

# Save results to new Excel file
product_sales.to_excel("sales_summary.xlsx")

pivot = pd.pivot_table(
    data,
    values="Sales",
    index="Product",
    aggfunc="sum"
)

pivot.to_excel("pivot_summary.xlsx")

print("\nPivot table created: pivot_summary.xlsx")

print("\nNew Excel file created: sales_summary.xlsx")