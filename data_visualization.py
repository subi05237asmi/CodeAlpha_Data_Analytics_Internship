import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------------------------
# 1. Create data folder
# --------------------------------------------------

os.makedirs("data", exist_ok=True)

csv_file = "data/sales_visualization_data.csv"

# --------------------------------------------------
# 2. Generate dataset automatically
# --------------------------------------------------

np.random.seed(42)

products = ["Laptop", "Mobile", "Monitor", "Headphones", "Keyboard"]
regions = ["North", "South", "East", "West"]

data = []

for i in range(100):

    product = np.random.choice(products)
    region = np.random.choice(regions)

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

    quantity = np.random.randint(1, 10)
    sales = price * quantity

    data.append([
        i + 1,
        product,
        region,
        quantity,
        price,
        sales
    ])

df = pd.DataFrame(
    data,
    columns=[
        "Order_ID",
        "Product",
        "Region",
        "Quantity",
        "Unit_Price",
        "Sales"
    ]
)

# Save CSV
df.to_csv(csv_file, index=False)

print("Dataset created successfully!")
print(f"Saved to: {csv_file}")

# --------------------------------------------------
# 3. Load dataset
# --------------------------------------------------

df = pd.read_csv(csv_file)

print("\nFirst 5 records:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nDataset information:")
print(df.info())

# --------------------------------------------------
# 4. Basic statistics
# --------------------------------------------------

print("\nStatistical Summary:")
print(df.describe())

# --------------------------------------------------
# 5. Product-wise sales
# --------------------------------------------------

product_sales = df.groupby("Product")["Sales"].sum()

print("\nSales by Product:")
print(product_sales)

# --------------------------------------------------
# 6. Region-wise sales
# --------------------------------------------------

region_sales = df.groupby("Region")["Sales"].sum()

print("\nSales by Region:")
print(region_sales)

# --------------------------------------------------
# 7. Visualization settings
# --------------------------------------------------

sns.set_theme(style="whitegrid")

# --------------------------------------------------
# Chart 1: Sales by Product
# --------------------------------------------------

plt.figure(figsize=(9, 6))

product_sales.plot(kind="bar")

plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# --------------------------------------------------
# Chart 2: Sales by Region
# --------------------------------------------------

plt.figure(figsize=(8, 5))

region_sales.plot(kind="bar")

plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()

# --------------------------------------------------
# Chart 3: Sales Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(df["Sales"], kde=True)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()

# --------------------------------------------------
# Chart 4: Quantity vs Sales
# --------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="Quantity",
    y="Sales"
)

plt.title("Quantity vs Sales")
plt.xlabel("Quantity")
plt.ylabel("Sales")

plt.tight_layout()
plt.show()

# --------------------------------------------------
# Chart 5: Correlation Heatmap
# --------------------------------------------------

plt.figure(figsize=(8, 6))

numeric_data = df.select_dtypes(include=np.number)

sns.heatmap(
    numeric_data.corr(),
    annot=True,
    fmt=".2f",
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()

print("\n========================================")
print("DATA VISUALIZATION COMPLETED SUCCESSFULLY!")
print("========================================")