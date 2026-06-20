import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('retail_sales_dataset.csv')

df['Date'] = pd.to_datetime(df['Date'])
df['Month_Year'] = df['Date'].dt.to_period('M')

sales_column = 'Total Amount' 
print("--- Descriptive Statistics ---")
print(f"Mean (Average) Sales: {df[sales_column].mean():.2f}")
print(f"Median (Middle) Sales: {df[sales_column].median():.2f}")
print(f"Mode (Most Frequent) Sales: {df[sales_column].mode()[0]:.2f}")
print(f"Standard Deviation: {df[sales_column].std():.2f}\n")

monthly_sales = df.groupby('Month_Year')['Total Amount'].sum().reset_index()
monthly_sales['Month_Year'] = monthly_sales['Month_Year'].astype(str)

plt.figure(figsize=(10, 5))
sns.lineplot(data=monthly_sales, x='Month_Year', y='Total Amount', marker='o', color='b')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=45)
plt.grid(True)
plt.savefig('monthly_sales_trends.png', bbox_inches='tight')
plt.show()

product_sales = df.groupby('Product Category')['Total Amount'].sum().reset_index()

plt.figure(figsize=(8, 4))
sns.barplot(data=product_sales, x='Product Category', y='Total Amount', palette='viridis')
plt.title('Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales ($)')
plt.savefig('revenue_by_category.png', bbox_inches='tight')
plt.show()