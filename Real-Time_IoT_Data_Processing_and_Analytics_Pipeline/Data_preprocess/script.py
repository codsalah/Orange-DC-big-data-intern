import pandas as pd
from faker import Faker
from datetime import timedelta

# Initialize the Faker instance
fake = Faker()

# Load the existing CSV data into a DataFrame
# Replace 'data.csv' with the actual filename or path to your CSV file
file_path = 'Time-Series_for_predictive_maintenance/Data/raw_processed.csv'  
df = pd.read_csv(file_path)

# Remove the first two columns
df = df.iloc[:, 2:]

# Function to generate ordered timestamps
def generate_ordered_timestamps(start_time, num):
    return [start_time + timedelta(seconds=i) for i in range(num)]

# Generate ordered timestamps starting from a specific date
start_time = fake.date_time_this_decade()
df['Timestamp'] = generate_ordered_timestamps(start_time, len(df))

# Reorder the DataFrame to put the new timestamp column at the front
df = df[['Timestamp'] + df.columns[:-1].tolist()]

# Save the updated DataFrame to a new CSV file
output_file_path = 'Time-Series_for_predictive_maintenance/Spark_scripts/updated_data.csv'  
df.to_csv(output_file_path, index=False)

# Display the updated DataFrame
print(df)
