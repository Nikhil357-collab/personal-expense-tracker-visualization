import pandas as pd

df = pd.read_csv("data/expenses.csv")

print("\nOriginal Data:")
print(df.head())

# REMOVE DUPLICATES
df.drop_duplicates(inplace=True)

# REMOVE NULL VALUES
df.dropna(inplace=True)

# DATE CONVERSION
df["date"] = pd.to_datetime(df["date"])

# MONTH COLUMN
df["month"] = df["date"].dt.strftime("%Y-%m")

# DAY COLUMN
df["day"] = df["date"].dt.day_name()

print("\nCleaned Data:")
print(df.head())

# SAVE CLEAN DATA
df.to_csv("data/cleaned_expenses.csv", index=False)

print("\nData cleaned successfully!")