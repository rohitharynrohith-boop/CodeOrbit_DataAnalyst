# Task 2 - Sales Data Analysis using Pandas

## About the Project

As part of my Data Analyst Internship at CodeOrbit Tech, I worked on a sales data analysis project using Python and Pandas.

The main goal of this project was to understand the sales data, calculate important sales metrics, find the best-performing products, and identify sales patterns across different categories, regions, years, and months.

I used the Superstore dataset for this analysis.

---

## Objective

The objective of this project was to:

- Calculate total sales
- Find the average order value
- Identify the top-selling products
- Analyze sales by category
- Compare sales across different regions
- Analyze yearly and monthly sales trends
- Extract useful insights from the data

---

## Dataset

The dataset used for this project is the Superstore sales dataset.

It contains **9,994 records and 21 columns** covering sales transactions from **2014 to 2017**.

The main columns used for this analysis include:

- Order ID
- Order Date
- Product Name
- Category
- Region
- Sales

The cleaned dataset generated during Task 1 was used as the input for this analysis.

---

## Tools and Technologies

- Python
- Pandas
- CSV
- VS Code

---

## What I Did

### 1. Loaded the Dataset

I loaded the cleaned Superstore CSV file using Pandas.

I also converted the `Order Date` column into datetime format so that I could perform year-wise and month-wise analysis.

### 2. Calculated Total Sales

I calculated the total sales from all the transactions in the dataset.

**Total Sales: $2,297,200.86**

### 3. Calculated Average Order Value

I grouped the sales using `Order ID` and calculated the total value of each order.

Then, I calculated the average of all order totals.

**Average Order Value: $458.61**

### 4. Found Top-Selling Products

I grouped the data by `Product Name` and calculated the total sales for each product.

The product with the highest total sales was:

**Canon imageCLASS 2200 Advanced Copier - $61,599.82**

I also identified the other top-performing products using the same method.

### 5. Analyzed Sales by Category

I grouped the sales based on product category.

| Category | Sales |
|----------|------:|
| Furniture | $741,999.80 |
| Office Supplies | $719,047.03 |
| Technology | $836,154.03 |

Technology recorded the highest sales among the three categories.

### 6. Analyzed Sales by Region

I grouped the sales based on region.

| Region | Sales |
|--------|------:|
| Central | $501,239.89 |
| East | $678,781.24 |
| South | $391,721.91 |
| West | $725,457.82 |

The West region recorded the highest sales, while the South region recorded the lowest sales.

### 7. Analyzed Sales by Year

I also analyzed how sales changed from year to year.

| Year | Sales |
|------|------:|
| 2014 | $484,247.50 |
| 2015 | $470,532.51 |
| 2016 | $609,205.60 |
| 2017 | $733,215.26 |

The highest annual sales were recorded in 2017.

### 8. Analyzed Monthly Sales

Finally, I grouped the sales by month to understand the monthly sales pattern.

The highest monthly sales in the dataset were recorded in:

**November 2017 - $118,447.83**

---

## Key Insights

From this analysis, I found the following:

- The total sales were approximately **$2.30 million**.
- The average order value was approximately **$458.61**.
- The **Canon imageCLASS 2200 Advanced Copier** had the highest total sales among individual products.
- **Technology** was the highest-selling category.
- The **West** region recorded the highest sales.
- **2017** had the highest annual sales.
- **November 2017** recorded the highest monthly sales.

---

## Project Files

```text
Task2_Sales_Analysis/
│
├── sales_analysis.py
└── README.md