import pandas as pd
import numpy as np
from faker import Faker

# Initialize Faker
fake = Faker()

def generate_customer_data(num_records: int) -> pd.DataFrame:
    """Generate customer data and return as a DataFrame."""
    customer_data = {
        "customer_id": range(1, num_records + 1),
        "first_name": [fake.first_name() for _ in range(num_records)],
        "last_name": [fake.last_name() for _ in range(num_records)],
        "email": [fake.email() for _ in range(num_records)],
        "phone": [fake.phone_number() for _ in range(num_records)],
        "address": [fake.street_address() for _ in range(num_records)],
        "city": [fake.city() for _ in range(num_records)],
        "state": [fake.state() for _ in range(num_records)],
        "zip_code": [fake.zipcode() for _ in range(num_records)],
        "country": [fake.country() for _ in range(num_records)]
    }
    
    customer_df = pd.DataFrame(customer_data)
    customer_file_path = "customer_data.csv"
    customer_df.to_csv(customer_file_path, index=False)
    
    return customer_df

def generate_sales_data(num_records: int, customer_ids: range, product_ids: range, time_ids: range, store_ids: range) -> pd.DataFrame:
    """Generate sales data and return as a DataFrame."""
    sales_data = {
        "sales_id": range(1, num_records + 1),
        "customer_id": np.random.choice(customer_ids, num_records),
        "product_id": np.random.choice(product_ids, num_records),
        "time_id": np.random.choice(time_ids, num_records),
        "store_id": np.random.choice(store_ids, num_records),
        "quantity_sold": np.random.randint(1, 20, num_records),  # Quantity sold between 1 and 20
        "total_sales": np.round(np.random.uniform(5.00, 500.00, num_records), 2)  # Total sales between $5.00 and $500.00
    }
    
    sales_df = pd.DataFrame(sales_data)
    sales_file_path = "sales_data.csv"
    sales_df.to_csv(sales_file_path, index=False)
    
    return sales_df

def generate_product_data(num_records: int, num_suppliers: int) -> pd.DataFrame:
    """Generate product data and return as a DataFrame."""
    categories = ["Electronics", "Clothing", "Home & Kitchen", "Books", "Toys"]
    sub_categories = {
        "Electronics": ["Mobile", "Laptop", "Camera"],
        "Clothing": ["Men", "Women", "Kids"],
        "Home & Kitchen": ["Furniture", "Appliances", "Decor"],
        "Books": ["Fiction", "Non-Fiction", "Children"],
        "Toys": ["Action Figures", "Puzzles", "Board Games"]
    }
    
    product_data = {
        "product_id": range(1, num_records + 1),
        "product_name": [fake.word().capitalize() + " " + fake.word().capitalize() for _ in range(num_records)],
        "category": np.random.choice(categories, num_records),
        "sub_category": [np.random.choice(sub_categories[cat]) for cat in np.random.choice(categories, num_records)],
        "brand": [fake.company() for _ in range(num_records)],
        "price": np.round(np.random.uniform(10.00, 500.00, num_records), 2),  # Price between $10.00 and $500.00
        "supplier_id": np.random.choice(range(1, num_suppliers + 1), num_records)
    }
    
    product_df = pd.DataFrame(product_data)
    product_file_path = "product_data.csv"
    product_df.to_csv(product_file_path, index=False)
    
    return product_df

def generate_time_data(num_records: int) -> pd.DataFrame:
    """Generate time dimension data and return as a DataFrame."""
    dates = pd.date_range(start="2023-01-01", periods=num_records, freq='D')
    time_data = {
        "time_id": range(1, num_records + 1),
        "date": dates,
        "day_of_week": dates.day_name(),
        "month": dates.month_name(),
        "quarter": dates.quarter,
        "year": dates.year
    }
    
    time_df = pd.DataFrame(time_data)
    time_file_path = "time_data.csv"
    time_df.to_csv(time_file_path, index=False)
    
    return time_df

def generate_store_data(num_records: int) -> pd.DataFrame:
    """Generate store dimension data and return as a DataFrame."""
    store_data = {
        "store_id": range(1, num_records + 1),
        "store_name": [fake.company() + " Store" for _ in range(num_records)],
        "location": [fake.address() for _ in range(num_records)],
        "manager_name": [fake.name() for _ in range(num_records)]
    }
    
    store_df = pd.DataFrame(store_data)
    store_file_path = "store_data.csv"
    store_df.to_csv(store_file_path, index=False)
    
    return store_df

def generate_supplier_data(num_records: int) -> pd.DataFrame:
    """Generate supplier dimension data and return as a DataFrame."""
    supplier_data = {
        "supplier_id": range(1, num_records + 1),
        "supplier_name": [fake.company() for _ in range(num_records)],
        "contact_name": [fake.name() for _ in range(num_records)],
        "phone": [fake.phone_number() for _ in range(num_records)],
        "email": [fake.email() for _ in range(num_records)],
        "address": [fake.street_address() for _ in range(num_records)],
        "city": [fake.city() for _ in range(num_records)],
        "state": [fake.state() for _ in range(num_records)],
        "zip_code": [fake.zipcode() for _ in range(num_records)],
        "country": [fake.country() for _ in range(num_records)]
    }
    
    supplier_df = pd.DataFrame(supplier_data)
    supplier_file_path = "supplier_data.csv"
    supplier_df.to_csv(supplier_file_path, index=False)
    
    return supplier_df

# Example usage
if __name__ == "__main__":
    num_customers = 100  # Number of customers to generate
    num_sales = 1_000  # Number of sales records to generate
    num_products = 100  # Number of products to generate
    num_suppliers = 20  # Number of suppliers
    num_stores = 20     # Number of stores
    num_time_records = 365  # Number of days in a year

    # Generate customer data
    customer_df = generate_customer_data(num_customers)
    
    # Generate product data
    product_df = generate_product_data(num_products, num_suppliers)

    # Generate store data
    store_df = generate_store_data(num_stores)

    # Generate time data
    time_df = generate_time_data(num_time_records)

    # Generate supplier data
    supplier_df = generate_supplier_data(num_suppliers)

    # Generate sales data using customer IDs from the generated customer data
    customer_ids = range(1, num_customers + 1)  # Using customer IDs from 1 to 100
    product_ids = range(1, num_products + 1)  # Using product IDs from 1 to 100
    time_ids = range(1, num_time_records + 1)  # Using time IDs from 1 to 365
    store_ids = range(1, num_stores + 1)  # Using store IDs from 1 to 20

    sales_df = generate_sales_data(num_sales, customer_ids, product_ids, time_ids, store_ids)

    print(customer_df.head())  # Display the first few rows of the generated customer data
    print(product_df.head())  # Display the first few rows of the generated product data
    print(store_df.head())    # Display the first few rows of the generated store data
    print(time_df.head())     # Display the first few rows of the generated time data
    print(supplier_df.head())  # Display the first few rows of the generated supplier data
    print(sales_df.head())     # Display the first few rows of the generated sales data
