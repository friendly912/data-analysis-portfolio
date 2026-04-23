import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("SampleSuperstore.csv")

# Convert Order Date
data["Order Date"] = pd.to_datetime(
    data["Order Date"],
    dayfirst=True
)

# Monthly Sales
monthly_sales = data.groupby(
    data["Order Date"].dt.to_period("M")
)["Sales"].sum()

# Category Sales
category_sales = data.groupby("Category")["Sales"].sum()

# Region Sales
region_sales = data.groupby("Region")["Sales"].sum()

# Top Products
top_products = (
    data.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

# Create Dashboard Layout
plt.figure(figsize=(12,8))

# Chart 1 — Category
plt.subplot(2,2,1)
category_sales.plot(kind="bar")
plt.title("Sales by Category")

# Chart 2 — Region
plt.subplot(2,2,2)
region_sales.plot(kind="bar")
plt.title("Sales by Region")

# Chart 3 — Monthly Trend
plt.subplot(2,2,3)
monthly_sales.plot()
plt.title("Monthly Sales Trend")

# Chart 4 — Top Products
plt.subplot(2,2,4)
top_products.plot(kind="bar")
plt.title("Top 5 Products")

plt.tight_layout()

# Save dashboard image
plt.savefig("08.sales_dashboard.png")

plt.show()