import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================================
# STAGE 1 : LOAD DATASET
# =====================================================

file_name = "Dataset for Data Analytics (1).xlsx"

try:
    df = pd.read_excel(file_name, engine="openpyxl")

    print("="*50)
    print("DATASET LOADED SUCCESSFULLY")
    print("="*50)

    print(f"\nRows : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

except Exception as e:
    print("Error Loading File:", e)
    exit()

# =====================================================
# STAGE 2 : DATA OVERVIEW
# =====================================================

print("\n\nDATASET OVERVIEW")
print("="*50)

print(df.head())

print("\nColumn Information:")
print(df.info())

# =====================================================
# STAGE 3 : MISSING VALUES
# =====================================================

print("\n\nMISSING VALUE ANALYSIS")
print("="*50)

missing = df.isnull().sum()

print(missing)

total_missing = missing.sum()

print(f"\nTotal Missing Values: {total_missing}")

# =====================================================
# STAGE 4 : DUPLICATE CHECK
# =====================================================

duplicates = df.duplicated().sum()

print("\nDuplicate Records:", duplicates)

# =====================================================
# STAGE 5 : DATE CONVERSION
# =====================================================

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

invalid_dates = df["Date"].isnull().sum()

print("\nInvalid Dates:", invalid_dates)

# =====================================================
# STAGE 6 : DESCRIPTIVE STATISTICS
# =====================================================

print("\n\nDESCRIPTIVE STATISTICS")
print("="*50)

numeric_cols = ["Quantity", "UnitPrice", "TotalPrice"]

print(df[numeric_cols].describe())

print("\nMean Values")
print(df[numeric_cols].mean())

print("\nMedian Values")
print(df[numeric_cols].median())

# =====================================================
# STAGE 7 : OUTLIER DETECTION
# =====================================================

print("\n\nOUTLIER DETECTION")
print("="*50)

for col in numeric_cols:

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print(f"{col}: {len(outliers)} Outliers Found")

# =====================================================
# STAGE 8 : ORDER STATUS ANALYSIS
# =====================================================

print("\n\nORDER STATUS DISTRIBUTION")
print("="*50)

print(df["OrderStatus"].value_counts())

# =====================================================
# STAGE 9 : TREND ANALYSIS
# =====================================================

print("\n\nMONTHLY SALES TREND")
print("="*50)

monthly_sales = (
    df.groupby(df["Date"].dt.month)["TotalPrice"]
    .sum()
)

print(monthly_sales)

# =====================================================
# STAGE 10 : CORRELATION ANALYSIS
# =====================================================

print("\n\nCORRELATION MATRIX")
print("="*50)

correlation = df[numeric_cols].corr()

print(correlation)

# =====================================================
# STAGE 11 : BUSINESS METRICS
# =====================================================

print("\n\nBUSINESS SUMMARY")
print("="*50)

print(f"Total Revenue : ${df['TotalPrice'].sum():,.2f}")

print(f"Highest Transaction : ${df['TotalPrice'].max():,.2f}")

print(f"Lowest Transaction : ${df['TotalPrice'].min():,.2f}")

print(f"Average Transaction : ${df['TotalPrice'].mean():,.2f}")

# =====================================================
# STAGE 12 : VISUALIZATION
# =====================================================

# Histogram

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

# Order Status Count

plt.figure(figsize=(8,5))
sns.countplot(x="OrderStatus", data=df)
plt.title("Order Status Distribution")
plt.xticks(rotation=45)
plt.show()

# Monthly Sales Trend

monthly_sales.plot(
    kind="line",
    marker="o",
    figsize=(8,5)
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

# =====================================================
# STAGE 13 : KEY INSIGHTS
# =====================================================

print("\n\nKEY INSIGHTS")
print("="*50)

print(f"1. Total Revenue Generated = ${df['TotalPrice'].sum():,.2f}")

print(f"2. Highest Transaction = ${df['TotalPrice'].max():,.2f}")

print(f"3. Average Transaction = ${df['TotalPrice'].mean():,.2f}")

print(
    f"4. Most Common Order Status = "
    f"{df['OrderStatus'].mode()[0]}"
)

print(
    f"5. Dataset contains "
    f"{len(df)} transaction records."
)

print("\nEDA COMPLETED SUCCESSFULLY")
