Task 1 – Data Cleaning


1. Objective

The objective of this task is to inspect and clean a sales dataset using Python and Pandas.

The data-cleaning process focuses on identifying data-quality issues, checking for missing values and duplicate records, resolving formatting and data-type issues, and producing a clean dataset that can be used for further analysis.

2. Dataset

The dataset used for this task is the Sample Superstore sales dataset.

The dataset contains information related to:

Orders
Customers
Products
Categories
Regions
Sales
Quantity
Discounts
Profit
Order dates
Shipping dates
Dataset Dimensions
Rows: 9,994
Columns: 21
Dataset Files
Sample-Superstore.csv – Original raw dataset
cleaned_superstore.csv – Cleaned dataset
3. Tools and Technologies

The following tools and technologies were used:

Python
Pandas
CSV
Visual Studio Code
4. Data Inspection

Before applying any cleaning operations, the dataset was inspected to understand its structure and identify potential data-quality issues.

The following checks were performed:

Dataset dimensions
Column names
Missing values
Duplicate records
Data types
Text formatting
Date formatting

The dataset was loaded using:

import pandas as pd

file_path = r"C:\Users\rohit\Downloads\4-1 ppts\superstore archive\Sample - Superstore.csv"

df = pd.read_csv(file_path, encoding="latin1")

The latin1 encoding was used because the original CSV file produced an encoding error when it was initially read using the default UTF-8 encoding.

5. Initial Data Findings
5.1 Dataset Dimensions

The dataset contains:

9,994 rows
21 columns
5.2 Missing Values

Missing values were checked using:

df.isnull().sum()
Result

No missing values were found in the dataset.

Missing Values: 0

Since there were no missing values, no missing-value treatment was required.

5.3 Duplicate Records

Duplicate rows were checked using:

df.duplicated().sum()
Result
Duplicate Rows: 0

No exact duplicate rows were identified.

The same Order ID can appear in multiple rows because a single order can contain multiple products. These records were retained.

6. Data Type Inspection

The data types of all columns were inspected using:

df.dtypes

The following date columns were initially stored as strings:

Order Date
Ship Date

These columns were converted into proper datetime format.

7. Data Cleaning Process
Step 1 – Load the Dataset

The original Superstore CSV file was loaded into a Pandas DataFrame.

df = pd.read_csv(file_path, encoding="latin1")
Step 2 – Inspect the Dataset

The dataset was inspected using:

df.shape
df.columns
df.dtypes
df.isnull().sum()
df.duplicated().sum()
Step 3 – Standardize Column Names

Leading and trailing spaces in column names were removed using:

df.columns = df.columns.str.strip()
Step 4 – Clean Text Columns

Text columns were identified and leading and trailing spaces were removed.

text_columns = df.select_dtypes(include="str").columns

for column in text_columns:
    df[column] = df[column].str.strip()
Step 5 – Convert Order Date

The Order Date column was converted to datetime format:

df["Order Date"] = pd.to_datetime(df["Order Date"])
Step 6 – Convert Ship Date

The Ship Date column was converted to datetime format:

df["Ship Date"] = pd.to_datetime(df["Ship Date"])
Step 7 – Verify the Cleaned Dataset

The dataset was checked again after cleaning:

df.isnull().sum()
df.duplicated().sum()
df[["Order Date", "Ship Date"]].dtypes

The verification confirmed:

No missing values
No exact duplicate rows
Order Date converted to datetime
Ship Date converted to datetime

8. Final Results
Data Quality Check	Result
Total Rows	9,994
Total Columns	21
Missing Values	0
Exact Duplicate Rows	0
Order Date	Datetime
Ship Date	Datetime

The cleaned dataset was saved as:

cleaned_superstore.csv

9. Project Structure
Task1_Data_cleaning/
│
├── Sample-Superstore.csv
├── cleaned_superstore.csv
├── data_cleaning.py
└── README.md
File Description

Sample-Superstore.csv

The original Superstore dataset used for the cleaning process.

cleaned_superstore.csv

The dataset generated after applying the cleaning and formatting operations.

data_cleaning.py

The Python script used to inspect, clean, verify, and save the dataset.

README.md

The documentation for the data-cleaning process and results.

10. Conclusion

The Sample Superstore dataset was inspected and cleaned using Python and Pandas.

The dataset was checked for missing values and exact duplicate records. No missing values or exact duplicate rows were found.

The Order Date and Ship Date columns were converted into proper datetime format.

Text columns were standardized by removing leading and trailing spaces.

The cleaned dataset was saved as cleaned_superstore.csv.

