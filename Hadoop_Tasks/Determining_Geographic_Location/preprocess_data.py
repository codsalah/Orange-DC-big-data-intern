import pandas as pd
import os

# Define paths
script_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(script_dir, 'Input_data')
output_folder = os.path.join(script_dir, 'preprocessed_data')

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

input_file_path = os.path.join(input_folder, 'usa_latitude_and_longitude.csv')
output_file_path = os.path.join(output_folder, 'processed_data.csv')

# Check if the input file exists
if not os.path.isfile(input_file_path):
    print(f"File not found: {input_file_path}")
else:
    # Load the data
    df = pd.read_csv(input_file_path)

    # Keep only the latitude and longitude columns
    df = df[['country_code','latitude', 'longitude']]

    # Save the result to a new CSV file
    df.to_csv(output_file_path, index=False)

    print(f"Processed data saved to {output_file_path}")
