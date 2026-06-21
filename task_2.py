import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================================
# DATA LOADING
# ==========================================================

file_name = "Dataset for Data Analytics (1).xlsx"

try:
    df = pd.read_excel(file_name, engine="openpyxl")

    print("=" * 60)
    print("DATASET LOADED SUCCESSFULLY")
    print("=" * 60)

except Exception as e:
    print("Error:", e)
    exit()

# ==========================================================
# DATASET OVERVIEW
# ==========================================================

print("\nDATASET SHAPE")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns.tolist())

print("\nFIRST 5 RECORDS")
print(df.head())

print("\nDATA TYPES")
print(df.dtypes)

# ==========================================================
# DATA CLEANING
# ==========================================================

print("\n" + "=" * 60)
print("DATA CLEANING")
print("=" * 60)

# Missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Handle CouponCode missing values
if "CouponCode" in df.columns:
    df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Duplicate records
duplicates = df.duplicated().sum()
print(f"\nDuplicate Records: {duplicates}")

# Date conversion
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

invalid_dates = df["Date"].isna().sum()
print(f"Invalid Dates: {invalid_dates}")

# ==========================================================
# DESCRIPTIVE STATISTICS
# ==========================================================

print("\n" + "=" * 60)
print("DESCRIPTIVE STATISTICS")
print("=" * 60)

numeric_cols = [
    "Quantity",
    "UnitPrice",
    "ItemsInCart",
    "TotalPrice"
]

print(df[numeric_cols].describe())

print("\nMEAN")
print(df[numeric_cols].mean())

print("\nMEDIAN")
print(df[numeric_cols].median())

# ==========================================================
# OUTLIER DETECTION
# ==========================================================

print("\n" + "=" * 60)
print("OUTLIER DETECTION")
print("=" * 60)

for col in numeric_cols:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - (1.5 * IQR)
    upper = Q3 + (1.5 * IQR)

    outliers = df[
        (df[col] < lower) |
        (df[col] > upper)
    ]

    print(f"{col}: {len(outliers)} outliers")

# ==========================================================
# ORDER STATUS ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("ORDER STATUS ANALYSIS")
print("=" * 60)

print(df["OrderStatus"].value_counts())

# ==========================================================
# PRODUCT ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("TOP PRODUCTS")
print("=" * 60)

print(df["Product"].value_counts().head(10))

# ==========================================================
# PAYMENT METHOD ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("PAYMENT METHODS")
print("=" * 60)

print(df["PaymentMethod"].value_counts())

# ==========================================================
# REFERRAL SOURCE ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("REFERRAL SOURCES")
print("=" * 60)

print(df["ReferralSource"].value_counts())

# ==========================================================
# SALES TREND ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("MONTHLY SALES TREND")
print("=" * 60)

monthly_sales = (
    df.groupby(df["Date"].dt.to_period("M"))
    ["TotalPrice"]
    .sum()
)

print(monthly_sales)

# ==========================================================
# CORRELATION ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("CORRELATION MATRIX")
print("=" * 60)

correlation = df[numeric_cols].corr()

print(correlation)

# ==========================================================
# BUSINESS METRICS
# ==========================================================

print("\n" + "=" * 60)
print("BUSINESS SUMMARY")
print("=" * 60)

total_revenue = df["TotalPrice"].sum()
avg_transaction = df["TotalPrice"].mean()
highest_transaction = df["TotalPrice"].max()
lowest_transaction = df["TotalPrice"].min()

print(f"Total Revenue: ${total_revenue:,.2f}")
print(f"Average Transaction: ${avg_transaction:,.2f}")
print(f"Highest Transaction: ${highest_transaction:,.2f}")
print(f"Lowest Transaction: ${lowest_transaction:,.2f}")

# ==========================================================
# VISUALIZATIONS
# ==========================================================

# Total Price Distribution
plt.figure(figsize=(8,5))
plt.hist(df["TotalPrice"], bins=20)
plt.title("Distribution of Total Price")
plt.xlabel("Total Price")
plt.ylabel("Frequency")
plt.show()

# Boxplot
plt.figure(figsize=(8,5))
sns.boxplot(x=df["TotalPrice"])
plt.title("Outlier Detection - Total Price")
plt.show()

# Order Status
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="OrderStatus")
plt.title("Order Status Distribution")
plt.xticks(rotation=45)
plt.show()

# Top Products
plt.figure(figsize=(10,5))
df["Product"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Products")
plt.ylabel("Number of Orders")
plt.show()

# Payment Methods
plt.figure(figsize=(8,5))
df["PaymentMethod"].value_counts().plot(kind="bar")
plt.title("Payment Methods")
plt.ylabel("Count")
plt.show()

# Referral Sources
plt.figure(figsize=(8,5))
df["ReferralSource"].value_counts().plot(kind="bar")
plt.title("Referral Sources")
plt.ylabel("Count")
plt.show()

# Monthly Revenue Trend
monthly_sales.plot(
    figsize=(10,5),
    marker="o"
)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.grid(True)
plt.show()

# Correlation Heatmap
plt.figure(figsize=(6,5))

sns.heatmap(
    correlation,
    annot=True,
    cmap="Blues"
)

plt.title("Correlation Heatmap")
plt.show()

# ==========================================================
# FINAL INSIGHTS
# ==========================================================

print("\n" + "=" * 60)
print("KEY INSIGHTS")
print("=" * 60)

print(f"Total Revenue Generated: ${total_revenue:,.2f}")
print(f"Average Transaction Value: ${avg_transaction:,.2f}")

print(
    f"Most Common Order Status: "
    f"{df['OrderStatus'].mode()[0]}"
)

print(
    f"Most Sold Product: "
    f"{df['Product'].mode()[0]}"
)

print(
    f"Most Used Payment Method: "
    f"{df['PaymentMethod'].mode()[0]}"
)

print(
    f"Top Referral Source: "
    f"{df['ReferralSource'].mode()[0]}"
)

print("\nEDA COMPLETED SUCCESSFULLY")
