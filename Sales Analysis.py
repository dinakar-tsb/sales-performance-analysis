import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Sales_Analytics.csv")
print(df.shape)

#Numbers of orders by state
plt.figure()
sns.countplot(y = "State", data=df)
plt.title("Numbers of orders by state")
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
state_sales = df.groupby("State")["Sales"].sum().sort_values(ascending=False)
print(state_sales)

plt.figure(figsize=(8,6))
state_sales.plot(kind="bar")
plt.title("Total sales by state")
plt.xlabel("State")
plt.ylabel("Total Sales")
plt.xticks(rotation = 40)
plt.show()

#Region wise sales comparison
region_Sales = df.groupby("Region")["Sales"].sum()
print(region_Sales)

plt.figure()
sns.barplot(x="Region", y = "Sales",data= df)
plt.title("Total sales by region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# Product and profit analysis

#Calculate total sales by product
product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
)
print(product_sales)

plt.figure()
sns.barplot(
    x = product_sales.index,
    y = product_sales.values
)
plt.title("Total sales by product")
plt.xlabel("Product")
plt.ylabel("Total_sales")
plt.xticks(rotation = 30)
plt.show()

#Profit analysis by Product
#calcualate total profit by product
product_profit = (df.groupby("Product")["Profit"].sum()
                  .sort_values(ascending=False)
)
print(product_profit)

plt.figure()
sns.barplot(x = product_profit.index, y = product_profit.values)
plt.title("Total profit by product")
plt.xlabel("Product")
plt.ylabel("Total Profit")
plt.xticks(rotation = 40)
plt.show()

#Discount vs Profit Analysis
plt.figure()
sns.regplot(x = "Discount_%", y = "Profit", data=df , scatter_kws={"alpha":0.3})
plt.title("Discount vs Profit")
plt.xlabel("Discount Percentage")
plt.ylabel("Profit")
plt.show()