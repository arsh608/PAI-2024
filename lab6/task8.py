import pandas as pd

products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')

print("First 5 rows of Products DataFrame:")
print(products_df.head())

print("\nLast 10 rows of Products DataFrame:")
print(products_df.tail(10))

print("\nFirst 5 rows of Orders DataFrame:")
print(orders_df.head())

print("\nLast 10 rows of Orders DataFrame:")
print(orders_df.tail(10))

merged_df = pd.merge(orders_df, products_df, on='ProductID')

merged_df['Revenue'] = merged_df['Quantity'] * merged_df['Price']

total_revenue = merged_df['Revenue'].sum()
print(f"\nTotal Revenue Generated: ${total_revenue:.2f}")

product_sales = merged_df.groupby('ProductName')['Quantity'].sum().sort_values(ascending=False)

top_5_best_selling = product_sales.head(5)
top_5_low_selling = product_sales.tail(5)

print("\nTop 5 Best-Selling Products:")
print(top_5_best_selling)

print("\nTop 5 Low-Selling Products:")
print(top_5_low_selling)

top_5_products = top_5_best_selling.index
top_5_categories = merged_df[merged_df['ProductName'].isin(top_5_products)]['Category']
most_common_category = top_5_categories.mode()[0]

print(f"\nMost Common Category among Top 5 Best-Selling Products: {most_common_category}")

average_price_per_category = products_df.groupby('Category')['Price'].mean()

print("\nAverage Price of Products in Each Category:")
print(average_price_per_category)

merged_df['Order Date'] = pd.to_datetime(merged_df['Order Date'], format='%m-%d-%Y')

merged_df['Year'] = merged_df['Order Date'].dt.year
merged_df['Month'] = merged_df['Order Date'].dt.month
merged_df['Day'] = merged_df['Order Date'].dt.day

revenue_per_day = merged_df.groupby(['Year', 'Month', 'Day'])['Revenue'].sum()
revenue_per_month = merged_df.groupby(['Year', 'Month'])['Revenue'].sum()
revenue_per_year = merged_df.groupby(['Year'])['Revenue'].sum()

day_highest_revenue = revenue_per_day.idxmax()
month_highest_revenue = revenue_per_month.idxmax()
year_highest_revenue = revenue_per_year.idxmax()

print(f"\nDay with Highest Total Revenue: {day_highest_revenue} with ${revenue_per_day.max():.2f}")
print(f"Month with Highest Total Revenue: {month_highest_revenue} with ${revenue_per_month.max():.2f}")
print(f"Year with Highest Total Revenue: {year_highest_revenue} with ${revenue_per_year.max():.2f}")

monthly_revenue_df = merged_df.groupby(['Year', 'Month'])['Revenue'].sum().reset_index()

print("\nTotal Revenue for Each Month:")
print(monthly_revenue_df)

print("\nChecking for null values in Products DataFrame:")
print(products_df.isnull().sum())

print("\nChecking for null values in Orders DataFrame:")
print(orders_df.isnull().sum())

products_df.dropna(inplace=True)
orders_df.dropna(inplace=True)

print("\nNull values have been removed (if any were present).")
