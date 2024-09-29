import pandas as pd
products_data = {
    'ProductID': range(1, 51),  # 50 Product IDs
    'ProductName': [
        'Smartphone', 'Laptop', 'Headphones', 'Desk Chair', 'Table', 'Book', 'Lamp',
        'Keyboard', 'Mouse', 'T-shirt', 'Blender', 'Washing Machine', 'Fridge',
        'Shoes', 'Jacket', 'Microwave', 'Television', 'Coffee Maker', 'Sofa', 'Bed',
        'Fan', 'Air Conditioner', 'Heater', 'Oven', 'Rice Cooker', 'Smartwatch',
        'Tablet', 'Monitor', 'Camera', 'Tripod', 'Gaming Console', 'Iron',
        'Hair Dryer', 'Toaster', 'Kettle', 'Vacuum Cleaner', 'Dishwasher',
        'Water Dispenser', 'Pen', 'Notebook', 'Backpack', 'Desk', 'Chair', 'Pillow',
        'Blanket', 'Mirror', 'Speaker', 'Projector', 'Router', 'Blender'
    ],  # 50 Product Names
    'Category': [
        'Electronics', 'Electronics', 'Electronics', 'Furniture', 'Furniture', 'Literature',
        'Furniture', 'Electronics', 'Electronics', 'Clothing', 'Home Appliances',
        'Home Appliances', 'Home Appliances', 'Clothing', 'Clothing', 'Home Appliances',
        'Electronics', 'Home Appliances', 'Furniture', 'Furniture', 'Home Appliances',
        'Home Appliances', 'Home Appliances', 'Home Appliances', 'Home Appliances',
        'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Electronics',
        'Electronics', 'Home Appliances', 'Home Appliances', 'Home Appliances',
        'Home Appliances', 'Home Appliances', 'Home Appliances', 'Stationery', 'Stationery',
        'Clothing', 'Furniture', 'Furniture', 'Furniture', 'Furniture', 'Furniture',
        'Electronics', 'Electronics', 'Electronics', 'Electronics', 'Home Appliances'
    ],  # 50 Categories
    'Price': [
        699.99, 999.99, 199.99, 149.99, 249.99, 9.99, 29.99, 49.99, 39.99, 19.99,
        59.99, 499.99, 899.99, 79.99, 149.99, 119.99, 499.99, 79.99, 699.99, 999.99,
        49.99, 399.99, 89.99, 299.99, 49.99, 199.99, 399.99, 199.99, 699.99, 29.99,
        299.99, 39.99, 59.99, 19.99, 49.99, 299.99, 499.99, 199.99, 1.99, 4.99, 49.99,
        149.99, 99.99, 29.99, 49.99, 29.99, 199.99, 599.99, 79.99, 129.99
    ]  # 50 Prices
}

orders_data = {
    'Order ID': range(1001, 1051),  # 50 Order IDs
    'ProductID': [
        1, 2, 3, 4, 5, 6, 1, 3, 10, 4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 1, 2, 3, 4, 5, 6, 10, 15, 12, 14, 17, 21, 22, 24, 25,
        30, 35, 36, 40, 45, 47, 48, 49, 50
    ],  # 50 Product IDs
    'Quantity': [
        2, 1, 3, 2, 1, 5, 1, 4, 2, 1, 3, 1, 2, 1, 4, 1, 3, 2, 1, 5,
        2, 3, 4, 1, 2, 1, 1, 1, 1, 1, 2, 2, 2, 3, 2, 1, 2, 1, 3, 3,
        1, 2, 4, 3, 2, 1, 3, 2, 1, 3
    ],  # 50 Quantities
    'Order Date': [
        '05-12-2023', '05-13-2023', '05-14-2023', '05-15-2023', '05-16-2023', '06-01-2023',
        '06-02-2023', '06-03-2023', '06-04-2023', '06-05-2023', '06-06-2023', '06-07-2023',
        '06-08-2023', '06-09-2023', '06-10-2023', '06-11-2023', '06-12-2023', '06-13-2023',
        '06-14-2023', '06-15-2023', '06-16-2023', '06-17-2023', '06-18-2023', '06-19-2023',
        '06-20-2023', '06-21-2023', '06-22-2023', '06-23-2023', '06-24-2023', '06-25-2023',
        '06-26-2023', '06-27-2023', '06-28-2023', '06-29-2023', '06-30-2023', '07-01-2023',
        '07-02-2023', '07-03-2023', '07-04-2023', '07-05-2023', '07-06-2023', '07-07-2023',
        '07-08-2023', '07-09-2023', '07-10-2023', '07-11-2023', '07-12-2023', '07-13-2023',
        '07-14-2023', '07-15-2023'
    ]  # 50 Dates
}

products_df = pd.DataFrame(products_data)
orders_df = pd.DataFrame(orders_data)

products_df.to_csv(r'C:\Users\arsha\OneDrive\Desktop\products.csv', index=False)
orders_df.to_csv(r'C:\Users\arsha\OneDrive\Desktop\orders.csv', index=False)

products_df.head(), orders_df.head()
