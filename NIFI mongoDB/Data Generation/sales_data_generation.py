import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Define parameters
num_products = 100  # Number of products
num_rows_sales = 1_000_000  # Number of rows for sales data
categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys"]
regions = ["North", "South", "East", "West"]
start_date = "2023-01-01"
end_date = "2023-12-31"
customer_ids = range(500, 600)  # Assume 100 customers with IDs 500 to 599

# Generate product data
product_ids = range(100, 200)  # Product IDs from 100 to 199
product_data = {
    "product_id": list(product_ids),
    "product_name": [fake.word().capitalize() for _ in range(num_products)],
    "category": np.random.choice(categories, num_products),
    "price": np.round(np.random.uniform(10, 1000, num_products), 2)
}
products_df = pd.DataFrame(product_data)

# Save product data to CSV
products_file_path = "products.csv"
products_df.to_csv(products_file_path, index=False)

# Generate sales data with consistent product IDs
sales_data = {
    "transaction_id": range(1, num_rows_sales + 1),
    "product_id": np.random.choice(product_ids, num_rows_sales),  # Product IDs must match the ones from product data
    "quantity": np.random.randint(1, 10, num_rows_sales),
    "price": products_df.set_index('product_id').loc[np.random.choice(product_ids, num_rows_sales), 'price'].values,
    "transaction_date": pd.to_datetime(
        np.random.choice(pd.date_range(start_date, end_date), num_rows_sales)
    ).strftime("%Y-%m-%d"),
    "customer_id": np.random.choice(customer_ids, num_rows_sales),
    "region": np.random.choice(regions, num_rows_sales)
}
sales_df = pd.DataFrame(sales_data)

# Save sales data to CSV
sales_file_path = "sales_data.csv"
sales_df.to_csv(sales_file_path, index=False)
