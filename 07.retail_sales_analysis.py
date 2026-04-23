import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("SampleSuperstore.csv")

print("\nDataset Preview:")
print(data.head())

# Total Sales
total_sales = data["Sales"].sum()

print("\nTotal Sales:", total_sales)

# Sales by Category
category_sales = data.groupby("Category")["Sales"].sum()

print("\nSales by Category:")
print(category_sales)

# Top 5 Products
top_products = data.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(5)

print("\nTop 5 Products:")
print(top_products)

# Sales by Region
region_sales = data.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

# Region chart
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.show()