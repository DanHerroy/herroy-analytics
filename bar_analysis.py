import pandas as pd

# Simulated bar sales data
data = {
    "product": ["Beer", "Beer", "Wine", "Whisky", "Wine", "Beer"],
    "day": ["Mon", "Tue", "Tue", "Wed", "Thu", "Thu"],
    "revenue": [120, 150, 200, 300, 180, 130]
}

df = pd.DataFrame(data)

print("Full Data:")
print(df)

# Total revenue
total_revenue = df["revenue"].sum()
print("\nTotal Revenue:", total_revenue)

# Revenue by product
by_product = df.groupby("product")["revenue"].sum()
print("\nRevenue by Product:")
print(by_product)

# Best selling product
best_product = by_product.idxmax()
print("\nBest Product:", best_product)

import matplotlib.pyplot as plt

# Plot revenue by product
by_product.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

plt.show()