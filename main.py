
# ==========================================
# PERSONAL EXPENSE TRACKER WITH VISUALIZATION
# ==========================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3
from datetime import datetime, timedelta
import random
import os
import streamlit as st
# ==========================================
# CREATE PROJECT FOLDERS
# ==========================================

folders = [
    "data",
    "outputs",
    "reports",
    "images"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# ==========================================
# SYNTHETIC EXPENSE DATASET CREATION
# ==========================================

categories = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Healthcare",
    "Education",
    "Travel"
]

payment_methods = [
    "Cash",
    "UPI",
    "Credit Card",
    "Debit Card"
]

notes = [
    "Lunch",
    "Bus Ticket",
    "Movie",
    "Groceries",
    "Electricity Bill",
    "Medicine",
    "Online Course",
    "Fuel"
]

# Generate synthetic expense data
data = []

start_date = datetime(2025, 1, 1)

for i in range(300):

    random_days = random.randint(0, 180)
    expense_date = start_date + timedelta(days=random_days)

    category = random.choice(categories)

    amount = round(random.uniform(50, 5000), 2)

    payment = random.choice(payment_methods)

    note = random.choice(notes)

  # FESTIVAL / DECEMBER SHOPPING SIMULATION
    if expense_date.month == 12 and category == "Shopping":
        amount += 5000

    data.append([
        expense_date.strftime("%Y-%m-%d"),
        category,
        amount,
        payment,
        note
    ])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "date",
    "category",
    "amount",
    "payment_method",
    "note"
])

# Save synthetic dataset
df.to_csv("Personal-Expense-Tracker-Visualization/data/expenses.csv", index=False)

print("Synthetic dataset created successfully!")



# ==========================================
# LOAD CSV DATA
# ==========================================

df = pd.read_csv("Personal-Expense-Tracker-Visualization/data/expenses.csv")

print("\nFirst 5 Rows:")
print(df.head())

# ==========================================
# DATA CLEANING
# ==========================================

# Remove duplicates
df.drop_duplicates(inplace=True)

# Remove missing values
df.dropna(inplace=True)

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Create additional columns
df["month"] = df["date"].dt.strftime("%Y-%m")
df["day"] = df["date"].dt.day_name()

print("\nData Cleaning Completed!")

# ==========================================
# SQLITE DATABASE STORAGE
# ==========================================

conn = sqlite3.connect("expense_tracker.db")

df.to_sql(
    "expenses",
    conn,
    if_exists="replace",
    index=False
)

print("\nData stored in SQLite database!")

# ==========================================
# CATEGORY-WISE EXPENSE ANALYSIS
# ==========================================

category_analysis = (
    df.groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)

print("\nCategory-wise Expense Analysis:")
print(category_analysis)

# ==========================================
# MONTHLY EXPENSE ANALYSIS
# ==========================================

monthly_analysis = (
    df.groupby("month")["amount"]
    .sum()
)

print("\nMonthly Expense Analysis:")
print(monthly_analysis)

# ==========================================
# PAYMENT METHOD ANALYSIS
# ==========================================

payment_analysis = (
    df.groupby("payment_method")["amount"]
    .sum()
)

print("\nPayment Method Analysis:")
print(payment_analysis)

# ==========================================
# HIGHEST SPENDING CATEGORY
# ==========================================

highest_category = category_analysis.idxmax()
highest_amount = category_analysis.max()

print("\nHighest Spending Category:")
print(f"{highest_category} : ₹{highest_amount:.2f}")

# ==========================================
# AVERAGE DAILY SPENDING
# ==========================================

daily_spending = (
    df.groupby("date")["amount"]
    .sum()
)

average_daily_spending = daily_spending.mean()

print("\nAverage Daily Spending:")
print(f"₹{average_daily_spending:.2f}")

# Generate random values for demonstration
random_amount = random.uniform(50, 5000)
random_category = random.choice(categories)

# ==========================================
# TOTAL MONTHLY SPENDING
# ==========================================

total_monthly_spending = monthly_analysis.sum()

print("\nTotal Monthly Spending:")
print(f"₹{total_monthly_spending:.2f}")

# ==========================================
# VISUALIZATION SETTINGS
# ==========================================

sns.set(style="whitegrid")

# ==========================================
# CATEGORY-WISE BAR CHART
# ==========================================

plt.figure(figsize=(10, 6))

category_analysis.plot(
    kind="bar",
)

plt.title("Category-wise Expense Analysis")
plt.xlabel("Category")
plt.ylabel("Amount Spent")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("images/category_bar_chart.png")

plt.show()

# ==========================================
# MONTHLY SPENDING LINE CHART
# ==========================================

plt.figure(figsize=(10, 6))

monthly_analysis.plot(
    marker="o"
)

plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount Spent")

plt.tight_layout()

plt.savefig("images/monthly_spending_line_chart.png")

plt.show()

# ==========================================
# PAYMENT METHOD PIE CHART
# ==========================================

plt.figure(figsize=(8, 8))

payment_analysis.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title("Payment Method Analysis")

plt.tight_layout()

plt.savefig("images/payment_method_pie_chart.png")

plt.show()

# ==========================================
# DAILY SPENDING TREND
# ==========================================

daily_trend = (
    df.groupby("date")["amount"]
    .sum()
)

plt.figure(figsize=(12, 6))

daily_trend.plot()

plt.title("Daily Spending Trend")
plt.xlabel("Date")
plt.ylabel("Amount")

plt.tight_layout()

plt.savefig("images/daily_spending_trend.png")

plt.show()

# ==========================================
# REPORT GENERATION
# ==========================================

report = f"""
==========================================
PERSONAL EXPENSE TRACKER REPORT
==========================================

Total Spending:
₹{df['amount'].sum():.2f}

Average Daily Spending:
₹{average_daily_spending:.2f}

Highest Spending Category:
{highest_category}

Highest Category Amount:
₹{highest_amount:.2f}

==========================================
CATEGORY ANALYSIS
==========================================

{category_analysis}

==========================================
MONTHLY ANALYSIS
==========================================

{monthly_analysis}

==========================================
PAYMENT METHOD ANALYSIS
==========================================

{payment_analysis}
"""

# Save text report
with open("reports/expense_report.txt", "w") as file:
    file.write(report)

# Save CSV reports
category_analysis.to_csv(
    "reports/category_analysis.csv"
)

monthly_analysis.to_csv(
    "reports/monthly_analysis.csv"
)

payment_analysis.to_csv(
    "reports/payment_analysis.csv"
)

print("\nReports Generated Successfully!")


# ==========================================
# CLOSE DATABASE CONNECTION
# ==========================================

conn.close()

print("\nExpense Tracker Project Completed Successfully!")