import pandas as pd
import plotly.express as px

# Load dataset
data = pd.read_csv("SampleSuperstore.csv")

# Fix date format
data["Order Date"] = pd.to_datetime(
    data["Order Date"],
    dayfirst=True
)

# Month column
data["Month"] = data["Order Date"].dt.to_period("M").astype(str)

# Sales by Category
fig1 = px.bar(
    data,
    x="Category",
    y="Sales",
    color="Region",
    title="Sales by Category"
)

# Monthly Sales
monthly = data.groupby("Month")["Sales"].sum().reset_index()

fig2 = px.line(
    monthly,
    x="Month",
    y="Sales",
    title="Monthly Sales Trend"
)

# Save dashboard pages
fig1.write_html("dashboard_category.html")
fig2.write_html("dashboard_monthly.html")

fig1.show()
fig2.show()

print("Professional dashboard pages created!")