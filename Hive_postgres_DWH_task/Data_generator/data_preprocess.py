import pandas as pd
import numpy as np
# Load the product_data CSV file
file_path = 'Hive_postgres_DWH_task/Data_generator/product_data.csv' 
product_data = pd.read_csv(file_path)

# Remove the supplier_id column
product_data = product_data.drop(columns=['supplier_id'])

# Display the updated columns
print("Updated columns:", product_data.columns)

# Save the updated DataFrame back to the same CSV file
output_file_path = 'Hive_postgres_DWH_task/Data_generator/product_data.csv'  
product_data.to_csv(output_file_path, index=False)
