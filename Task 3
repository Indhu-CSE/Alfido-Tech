import pandas as pd

# -----------------------------
# 1. LOAD DATA
# -----------------------------
df = pd.read_csv('sample_sales.csv')
print("First 5 rows:")
print(df.head())

# -----------------------------
# 2. CLEAN DATA
# -----------------------------
# Remove duplicates
df = df.drop_duplicates()

# Remove null values
df = df.dropna()

# Convert date column to proper format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Remove rows where conversion failed
df = df.dropna(subset=['Date'])

print("\nCleaned Data:")
print(df.head())

# -----------------------------
# 3. FILTERING
# -----------------------------
# Example: filter only January sales
jan_sales = df[df['Date'].dt.month == 1]
print("\nJanuary Sales:")
print(jan_sales)

# -----------------------------
# 4. GROUPING AND ANALYSIS
# -----------------------------
# Total sales by product
sales_by_product = df.groupby('Product')['Amount'].sum()
print("\nTotal Sales by Product:")
print(sales_by_product)

# Average price by product
avg_price = df.groupby('Product')['Amount'].mean()
print("\nAverage Sales Amount:")
print(avg_price)

# Monthly sales summary
monthly_sales = df.groupby(df['Date'].dt.month)['Amount'].sum()
print("\nMonthly Sales:")
print(monthly_sales)

# -----------------------------
# 5. INSIGHTS
# -----------------------------
print("\n----- INSIGHTS -----")
best_product = sales_by_product.idxmax()
best_sales = sales_by_product.max()
print(f"The best-selling product is {best_product} with total sales of {best_sales}.")

best_month = monthly_sales.idxmax()
best_month_sales = monthly_sales.max()
print(f"Highest revenue month: Month {best_month} with total amount {best_month_sales}.")
