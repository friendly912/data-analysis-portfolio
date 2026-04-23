import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("profit.csv")

print("\nProfit Data:")
print(data.head())

# Calculate Profit
data["Profit"] = data["Revenue"] - data["Cost"]

# Total profit
total_profit = data["Profit"].sum()

print("\nTotal Profit:", total_profit)

# Profit by product
product_profit = data.groupby("Product")["Profit"].sum()

print("\nProfit by Product:")
print(product_profit)

average_profit = data["Profit"].mean()
print("\nAverage Profit:", average_profit)

# Find most profitable product
top_product = product_profit.idxmax()

print("\nMost Profitable Product:", top_product)

# Create chart
product_profit.plot(kind="bar")

plt.title("Profit by Product")
plt.xlabel("Product")
plt.ylabel("Profit")

plt.show()