import pandas as pd

file_path = "cleaned_superstore.csv"
df = pd.read_csv(file_path)

df["Order Date"] = pd.to_datetime(df["Order Date"])
print(df.head())
total_sales = df["Sales"].sum()
print("Total Sales:", total_sales)
order_totals = df.groupby("Order ID")["Sales"].sum()
average_order_value = order_totals.mean()
print("Average Order Value:", average_order_value)
top_sales = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False)

print("\nTop 10 Products:")
print(top_sales.head(10))
df.groupby("Product Name")["Sales"].sum()
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
print(category_sales)
region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)
print("\nDate Range:")
print("Start Date:", df["Order Date"].min())
print("End Date:", df["Order Date"].max())
df["Year"] = df["Order Date"].dt.year
yearly_sales = df.groupby("Year")["Sales"].sum()
print("\nSales by Year:")
print(yearly_sales)
df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nSales by Month:")
print(monthly_sales)