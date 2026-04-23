import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("sales.csv")

# Show first rows
print("\nFirst rows:")
print(data.head())

# Total sales
total_sales = data["SALES_PRICE"].sum()
print("\nTotal Sales:", total_sales)

# Sales by product
product_sales = data.groupby("AREA")["SALES_PRICE"].sum()

print("\nSales by AREA:")
print(product_sales)

# Create chart
product_sales.plot(kind="bar")

plt.title("house sales by area")
plt.xlabel("area")
plt.ylabel("sales")

plt.show()