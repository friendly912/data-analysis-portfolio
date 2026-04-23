import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Load dataset
data = pd.read_csv("SampleSuperstore.csv")

data["Order Date"] = pd.to_datetime(
    data["Order Date"],
    dayfirst=True
)

data["Month"] = data["Order Date"].dt.to_period("M").astype(str)

category_sales = data.groupby("Category")["Sales"].sum().reset_index()
region_sales = data.groupby("Region")["Sales"].sum().reset_index()
monthly_sales = data.groupby("Month")["Sales"].sum().reset_index()

top_products = (
    data.groupby("Product Name")["Sales"]
    .sum()
    .reset_index()
    .sort_values(by="Sales", ascending=False)
    .head(5)
)

# Create subplots
fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=(
        "Sales by Category",
        "Sales by Region",
        "Monthly Sales Trend",
        "Top Products"
    )
)

# Category
fig.add_trace(
    go.Bar(
        x=category_sales["Category"],
        y=category_sales["Sales"]
    ),
    row=1, col=1
)

# Region
fig.add_trace(
    go.Bar(
        x=region_sales["Region"],
        y=region_sales["Sales"]
    ),
    row=1, col=2
)

# Monthly
fig.add_trace(
    go.Scatter(
        x=monthly_sales["Month"],
        y=monthly_sales["Sales"]
    ),
    row=2, col=1
)

# Top Products
fig.add_trace(
    go.Bar(
        x=top_products["Product Name"],
        y=top_products["Sales"]
    ),
    row=2, col=2
)

fig.update_layout(
    height=800,
    title_text="Interactive Sales Dashboard"
)

# Save dashboard
fig.write_html("interactive_sales_dashboard.html")

fig.show()