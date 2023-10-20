import pandas as pd
import matplotlib.pyplot as plt

# Sample sales data
sales_data = {
    'date': ['2023-10-01', '2023-10-02', '2023-10-03', '2023-10-04', '2023-10-05'],
    'sales': [100, 120, 90, 80, 150],
    'product': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B'],
    'hour': [10, 12, 14, 18, 20]
}

# Creating a DataFrame
sales_df = pd.DataFrame(sales_data)

# Analyzing sales trends over time
sales_df['date'] = pd.to_datetime(sales_df['date'])
sales_df.set_index('date', inplace=True)
print("Sales Trends Over Time:")
print(sales_df)

# Creating a sales chart
sales_df.plot(kind='line', y='sales', marker='o', linestyle='-', color='b')
plt.title('Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.show()

# Identifying peak sales hours
peak_sales_hour = sales_df.groupby('hour')['sales'].sum().idxmax()
print(f"Peak Sales Hour: {peak_sales_hour}")

# Identifying popular products
popular_product = sales_df['product'].value_counts().idxmax()
print(f"Most Popular Product: {popular_product}")

# Generating reports for store management
# You can export the DataFrame to an Excel or CSV file
sales_df.to_excel('sales_report.xlsx', index=True)
