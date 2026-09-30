import pandas as pd

# 1. Load the dataset
file_path = "Task1_Data_cleaning/Sample-Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")

# 2. Inspect the original dataset
print("Original Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

print("\nOriginal Data Types:")
print(df.dtypes)

# 3. Clean column names
df.columns = df.columns.str.strip()

# 4. Remove unnecessary spaces from text columns
text_columns = df.select_dtypes(include="str").columns

for column in text_columns:
    df[column] = df[column].str.strip()

# 5. Convert date columns to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# 6. Check the cleaned data
print("\nAfter Cleaning:")

print("\nData Types:")
print(df.dtypes)

print("\nFinal Missing Values:")
print(df.isnull().sum())

print("\nFinal Duplicate Rows:")
print(df.duplicated().sum())

# 7. Save cleaned dataset
output_file = "cleaned_superstore.csv"
df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")