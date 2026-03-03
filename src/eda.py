import pandas as pd

def basic_summary(df):
    print("\n===== BASIC SUMMARY =====")
    print(df.describe())

def category_spending(df):
    print("\n===== SPENDING BY CATEGORY =====")
    return df.groupby("Category")["Amount"].sum().sort_values(ascending=False)

def monthly_spending(df):
    df["Month"] = df["Date"].dt.to_period("M")
    monthly = df.groupby("Month")["Amount"].sum()
    print("\n===== MONTHLY SPENDING =====")
    return monthly

def recurring_merchants(df):
    print("\n===== TOP MERCHANTS =====")
    return df["Merchant"].value_counts().head(10)