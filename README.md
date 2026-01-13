📊 Sales & Customer Data Analysis Dashboard
📌 Project Description

This project analyzes sales, customer, and product data to extract business insights using Python, Pandas, and Matplotlib.
It follows a typical data analytics workflow: data cleaning → feature engineering → aggregation → visualization.

The result is a 2×2 analytical dashboard highlighting revenue trends, customer performance, and segmentation.

🛠 Tools & Technologies

Python

Pandas

Matplotlib

CSV data sources

📂 Datasets Used

orders.csv – transaction-level sales data

customers.csv – customer demographics

products.csv – product catalog

🔄 Data Preparation

Removed duplicate records

Converted date columns to datetime

Cleaned text fields (names, cities, product names)

Created analytical features:

Monthly periods (order_month)

Revenue per order (quantity × unit_price × discount)

Joined datasets where required

📈 Key Analyses & Visualizations

Dashboard (2×2 grid):

Monthly Revenue Trend

Tracks sales performance over time

Top 10 Customers by Revenue

Identifies highest-value customers

Orders vs Total Revenue

Explores customer purchasing behavior

Customer Segmentation

Groups customers into High / Medium / Low value segments based on revenue

📊 Analytical Techniques

Grouping and aggregation (groupby, sum, mean, count)

KPI creation:

Total revenue

Average order value

Order frequency

Sorting and ranking

Business segmentation logic

Data visualization for decision support

▶️ How to Run
pip install pandas matplotlib
python analysis.py

🎯 Key Takeaways

Demonstrates practical business-oriented data analysis

Focuses on insight extraction, not just plotting

Mirrors tasks commonly expected in junior data analyst roles
