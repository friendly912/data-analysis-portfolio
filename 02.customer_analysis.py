import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv("customers.csv")

# Show first rows
print("\nCustomer Data:")
print(data.head())

# Total purchase by customer
customer_total = data.groupby("Customer")["Purchase"].sum()

print("\nTotal Purchase by Customer:")
print(customer_total)

# Find top customer
top_customer = customer_total.idxmax()

print("\nTop Customer:", top_customer)

# Purchase by city
city_total = data.groupby("City")["Purchase"].sum()

print("\nTotal Purchase by City:")
print(city_total)

average_purchase = data["Purchase"].mean()
print("\nAverage Purchase:", average_purchase)

# Create chart
customer_total.plot(kind="bar")

plt.title("Total Purchase by Customer")
plt.xlabel("Customer")
plt.ylabel("Purchase")

plt.show()