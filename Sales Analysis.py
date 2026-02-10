import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Sales_Analytics.csv")
print(df.shape)

#Numbers of orders by state
plt.figure()
ax = sns.countplot(y = "State", data=df)
plt.title("Numbers of orders by state")
for bar in ax.patches:
    ax.text(
        bar.get_width(),
        bar.get_y() + bar.get_height() / 2,
        int(bar.get_width()),
        va = "center",
        ha = "left"
    )
plt.show()

#Monthly sales trend
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.to_period("M")

#Calculate monthly sales
monthly_sales = df.groupby("Month")["Sales"].sum()
print(monthly_sales)

#Plot monthly sales trend
plt.figure()
monthly_sales.plot()
plt.title("Monthly sales trend")
plt.xlabel("Month")
plt.ylabel("Total sales")
plt.show()

#State wise total sales
# State-wise total sales
state_sales = (
    df.groupby("State")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(8)
    .reset_index()
    )

plt.figure(figsize=(10,5))
ax = sns.barplot(x="State", y="Sales", data=state_sales)

for bar in ax.patches:
    value = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        value,
        f"{value/1_000_000:.1f}M",
        ha="center",
        va="bottom"
    )

plt.title("Top 8 States by Total Sales")
plt.ylabel("Sales (in Millions)")
plt.xticks(rotation=30)
plt.show()

#Region wise sales comparison
# total sales by region
region_sales = df.groupby("Region")["Sales"].sum().reset_index()

plt.figure(figsize=(6,4))
ax = sns.barplot(x="Region", y="Sales", data=region_sales)

for bar in ax.patches:
    value = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        value,
        f"{value/1_000_000:.1f}M",
        ha="center",
        va="bottom"
    )

plt.title("Total Sales by Region")
plt.ylabel("Sales (in Millions)")
plt.show()

# Product and profit analysis
#Calculate total sales by product
product_sales = df.groupby("Product")["Sales"].sum()

ax = sns.barplot(x=product_sales.index, y=product_sales.values)

for bar in ax.patches:
    value = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        value,
        f"{value/1_000_000:.1f}M",
        ha="center",
        va="bottom"
    )

plt.title("Total sales by product")
plt.xticks(rotation=30)
plt.ylabel("Sales (in Millions)")
plt.show()

#Profit analysis by Product
#calcualate total profit by product
product_profit = df.groupby("Product")["Profit"].sum()

ax = sns.barplot(x=product_profit.index, y=product_profit.values)

for bar in ax.patches:
    value = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width()/2,
        value,
        f"{value/1_000_000:.1f}M",
        ha="center",
        va="bottom"
    )

plt.title("Total Profit by Product")
plt.xticks(rotation=40)
plt.ylabel("Profit (in Millions)")
plt.show()

#Discount vs Profit Analysis
plt.figure()
sns.regplot(x = "Discount_%", y = "Profit", data=df , scatter_kws={"alpha":0.3})
plt.title("Discount vs Profit")
plt.xlabel("Discount Percentage")
plt.ylabel("Profit")
plt.show()
