import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("monthly_sales.csv")

print("\nMonthly Sales Data:")
print(data)

# Total yearly sales
total_sales = data["Sales"].sum()

print("\nTotal Yearly Sales:", total_sales)

# Average monthly sales
average_sales = data["Sales"].mean()

print("\nAverage Monthly Sales:", average_sales)

# Find highest sales month
highest_month = data.loc[data["Sales"].idxmax()]

print("\nHighest Sales Month:")
print(highest_month)

# Create line chart
plt.plot(data["Month"], data["Sales"])

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()