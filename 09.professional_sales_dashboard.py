import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("SampleSuperstore.csv")

# Fix date format
data["Order Date"] = pd.to_datetime(
    data["Order Date"],
    dayfirst=True
)

# Create new column: Month
data["Month"] = data["Order Date"].dt.to_period("M")

# Monthly Sales
monthly_sales = data.groupby("Month")["Sales"].sum()

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

# Create Professional Dashboard
plt.figure(figsize=(14,10))

# Chart 1 — Category
plt.subplot(2,2,1)
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

# Chart 2 — Region
plt.subplot(2,2,2)
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

# Chart 3 — Monthly Trend
plt.subplot(2,2,3)
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Chart 4 — Top Products
plt.subplot(2,2,4)
top_products.plot(kind="bar")
plt.title("Top 5 Products")
plt.xlabel("Product")
plt.ylabel("Sales")

# Adjust layout
plt.tight_layout()

# Save professional dashboard
plt.savefig("09.professional_sales_dashboard.png")

plt.show()

print("Dashboard created successfully!")