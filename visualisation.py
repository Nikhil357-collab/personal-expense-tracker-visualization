import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("images", exist_ok=True)

df = pd.read_csv("data/cleaned_expenses.csv")

# CATEGORY ANALYSIS
category_analysis = (
    df.groupby("category")["amount"]
    .sum()
)

# MONTHLY ANALYSIS
monthly_analysis = (
    df.groupby("month")["amount"]
    .sum()
)

# PAYMENT ANALYSIS
payment_analysis = (
    df.groupby("payment_method")["amount"]
    .sum()
)

# DAILY TREND
daily_trend = (
    df.groupby("date")["amount"]
    .sum()
)

sns.set(style="whitegrid")

# CATEGORY BAR CHART
plt.figure(figsize=(10, 6))

category_analysis.plot(kind="bar")

plt.title("Category-wise Expense Analysis")

plt.xlabel("Category")

plt.ylabel("Amount")

plt.tight_layout()

plt.savefig("images/category_bar_chart.png")

plt.close()

# MONTHLY LINE CHART
plt.figure(figsize=(10, 6))

monthly_analysis.plot(marker="o")

plt.title("Monthly Spending Trend")

plt.xlabel("Month")

plt.ylabel("Amount")

plt.tight_layout()

plt.savefig("images/monthly_spending_line_chart.png")

plt.close()

# PAYMENT METHOD PIE CHART
plt.figure(figsize=(8, 8))

payment_analysis.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Payment Method Analysis")

plt.tight_layout()

plt.savefig("images/payment_method_pie_chart.png")

plt.close()

# DAILY TREND CHART
plt.figure(figsize=(12, 6))

daily_trend.plot()

plt.title("Daily Spending Trend")

plt.xlabel("Date")

plt.ylabel("Amount")

plt.tight_layout()

plt.savefig("images/daily_spending_trend.png")

plt.close()

print("All charts generated successfully!")