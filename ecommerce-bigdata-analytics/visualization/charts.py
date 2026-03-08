import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
data = pd.read_csv("revenue.csv")

# Set style
sns.set(style="whitegrid")

# Create figure layout
plt.figure(figsize=(15,10))

# 1️⃣ Line Chart — Monthly Revenue Trend
plt.subplot(2,3,1)
sns.lineplot(x="month", y="revenue", data=data, marker="o")
plt.title("Monthly Revenue Trend")

# 2️⃣ Bar Chart — Revenue by Month
plt.subplot(2,3,2)
sns.barplot(x="month", y="revenue", data=data)
plt.title("Revenue by Month")

# 3️⃣ Area Chart — Revenue Growth
plt.subplot(2,3,3)
plt.fill_between(data["month"], data["revenue"])
plt.title("Revenue Growth Over Time")
plt.xlabel("Month")
plt.ylabel("Revenue")

# 4️⃣ Histogram — Revenue Distribution
plt.subplot(2,3,4)
sns.histplot(data["revenue"], bins=10)
plt.title("Revenue Distribution")

# 5️⃣ Box Plot — Revenue Spread
plt.subplot(2,3,5)
sns.boxplot(y=data["revenue"])
plt.title("Revenue Spread")

# 6️⃣ Scatter Plot — Revenue Trend
plt.subplot(2,3,6)
sns.scatterplot(x="month", y="revenue", data=data)
plt.title("Revenue Scatter Trend")

# Adjust layout
plt.tight_layout()

# Show all charts
plt.show()