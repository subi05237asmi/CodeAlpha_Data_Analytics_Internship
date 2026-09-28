import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# 1. Create data folder
# --------------------------------------------------

data_folder = "data"
os.makedirs(data_folder, exist_ok=True)

csv_file = os.path.join(data_folder, "sales_data.csv")

# --------------------------------------------------
# 2. Generate a sample sales dataset automatically
# --------------------------------------------------

np.random.seed(42)

products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Monitor"]
regions = ["North", "South", "East", "West"]
categories = ["Electronics", "Accessories"]

data = []

for i in range(100):
    product = np.random.choice(products)
    region = np.random.choice(regions)

    if product in ["Laptop", "Mobile", "Monitor"]:
        category = "Electronics"
    else:
        category = "Accessories"

    quantity = np.random.randint(1, 10)

    if product == "Laptop":
        price = np.random.randint(50000, 80000)
    elif product == "Mobile":
        price = np.random.randint(15000, 50000)
    elif product == "Monitor":
        price = np.random.randint(10000, 30000)
    elif product == "Headphones":
        price = np.random.randint(1000, 8000)
    else:
        price = np.random.randint(800, 5000)

    sales = quantity * price

    data.append([
        i + 1,
        product,
        category,
        region,
        quantity,
        price,
        sales
    ])

columns = [
    "Order_ID",
    "Product",
    "Category",
    "Region",
    "Quantity",
    "Unit_Price",
    "Sales"
]

df = pd.DataFrame(data, columns=columns)

# Save dataset automatically
df.to_csv(csv_file, index=False)

print("========================================")
print("Sales dataset created successfully!")
print("========================================")
print(f"Dataset saved at: {csv_file}")

# --------------------------------------------------
# 3. Load the dataset
# --------------------------------------------------

df = pd.read_csv(csv_file)

print("\nFirst 5 records:")
print(df.head())

# --------------------------------------------------
# 4. Dataset information
# --------------------------------------------------

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# --------------------------------------------------
# 5. Check missing values
# --------------------------------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# --------------------------------------------------
# 6. Check duplicate records
# --------------------------------------------------

print("\nDuplicate Records:")
print(df.duplicated().sum())

# --------------------------------------------------
# 7. Statistical summary
# --------------------------------------------------

print("\nStatistical Summary:")
print(df.describe())

# --------------------------------------------------
# 8. Meaningful questions
# --------------------------------------------------

print("\n========================================")
print("EDA QUESTIONS AND INSIGHTS")
print("========================================")

# Question 1: Which product generated the highest sales?
product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("\n1. Sales by Product:")
print(product_sales)

# Question 2: Which region generated the highest sales?
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)

print("\n2. Sales by Region:")
print(region_sales)

# Question 3: Which category generated the highest sales?
category_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\n3. Sales by Category:")
print(category_sales)

# Question 4: What is the average sales value?
average_sales = df["Sales"].mean()

print("\n4. Average Sales:")
print(f"₹{average_sales:,.2f}")

# Question 5: Which product sold the highest quantity?
quantity_by_product = df.groupby("Product")["Quantity"].sum().sort_values(ascending=False)

print("\n5. Quantity Sold by Product:")
print(quantity_by_product)

# --------------------------------------------------
# 9. Detect potential outliers
# --------------------------------------------------

Q1 = df["Sales"].quantile(0.25)
Q3 = df["Sales"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[
    (df["Sales"] < lower_limit) |
    (df["Sales"] > upper_limit)
]

print("\nPotential Sales Outliers:")
print(len(outliers))

# --------------------------------------------------
# 10. Visualizations
# --------------------------------------------------

sns.set_theme(style="whitegrid")

# Product Sales
plt.figure(figsize=(10, 6))
product_sales.plot(kind="bar")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Regional Sales
plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Category Sales
plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

# Sales Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Sales"], kde=True)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
numeric_columns = df.select_dtypes(include=np.number)

sns.heatmap(
    numeric_columns.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\n========================================")
print("EDA COMPLETED SUCCESSFULLY!")
print("========================================")