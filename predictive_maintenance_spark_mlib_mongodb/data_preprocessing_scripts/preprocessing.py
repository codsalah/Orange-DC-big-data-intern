import pandas as pd
import os

class DataPreprocessor:
    def __init__(self, train_file: str, test_file: str, columns: list):
        self.train_file = train_file
        self.test_file = test_file
        self.columns = columns
        self.train_data = None
        self.test_data = None

    def load_data(self):
        """Load the datasets from the provided file paths."""
        self.train_data = pd.read_csv(self.train_file, sep=" ", header=None)
        self.test_data = pd.read_csv(self.test_file, sep=" ", header=None)
        print(f"Train data shape: {self.train_data.shape}")  # Print shape of train data
        print(f"Test data shape: {self.test_data.shape}")    # Print shape of test data
        self._assign_columns()

    def _assign_columns(self):
        """Assign column names to the datasets."""
        if len(self.train_data.columns) == len(self.columns):
            self.train_data.columns = self.columns
        else:
            print(f"Warning: Number of train columns {len(self.train_data.columns)} does not match the number of assigned columns {len(self.columns)}.")
        
        if len(self.test_data.columns) == len(self.columns):
            self.test_data.columns = self.columns
        else:
            print(f"Warning: Number of test columns {len(self.test_data.columns)} does not match the number of assigned columns {len(self.columns)}.")

    def preview_data(self):
        """Preview the first few rows of the datasets."""
        print("Training Data Preview:")
        print(self.train_data.head())
        print("\nTest Data Preview:")
        print(self.test_data.head())

    def handle_missing_values(self, strategy='drop'):
        """Handle missing values in the datasets."""
        if strategy == 'drop':
            self.train_data.dropna(inplace=True)
            self.test_data.dropna(inplace=True)
        elif strategy == 'fill':
            self.train_data.fillna(method='ffill', inplace=True)
            self.test_data.fillna(method='ffill', inplace=True)

    def drop_columns(self, columns_to_drop: list):
        """Drop specified columns from both train and test datasets."""
        self.train_data.drop(columns=columns_to_drop, inplace=True, errors='ignore')
        self.test_data.drop(columns=columns_to_drop, inplace=True, errors='ignore')

    def save_processed_data(self, train_output_dir: str, test_output_dir: str):
        """Save the processed datasets to CSV files in the specified directory."""
        # Create directories if they do not exist
        os.makedirs(train_output_dir, exist_ok=True)
        os.makedirs(test_output_dir, exist_ok=True)

        train_output_file = os.path.join(train_output_dir, "train_processed.csv")
        test_output_file = os.path.join(test_output_dir, "test_processed.csv")

        self.train_data.to_csv(train_output_file, index=False)
        self.test_data.to_csv(test_output_file, index=False)


# Example usage
if __name__ == "__main__":
    # Updated column names
    columns = ['engine', 'cycle', 'setting1', 'setting2', 'setting3',
               'sensor1', 'sensor2', 'sensor3', 'sensor4', 'sensor5',
               'sensor6', 'sensor7', 'sensor8', 'sensor9', 'sensor10',
               'sensor11', 'sensor12', 'sensor13', 'sensor14', 'sensor15',
               'sensor16', 'sensor17', 'sensor18', 'sensor19', 'sensor20',
               'sensor21']

    # File paths
    train_file = "predictive_maintenance_spark_mlib_mongodb/raw_data/train_sensor001.txt"
    test_file = "predictive_maintenance_spark_mlib_mongodb/raw_data/test_sensor001.txt"
    output_dir = "predictive_maintenance_spark_mlib_mongodb/preprocessed_dataa"

    # Initialize the preprocessor
    preprocessor = DataPreprocessor(train_file, test_file, columns)

    # Run preprocessing steps
    preprocessor.load_data()

    # Drop specified columns
    columns_to_drop = [26, 27]  # Change these indices based on your dataset
    preprocessor.drop_columns(columns_to_drop)

    # Preview data after dropping columns
    preprocessor.preview_data()

    # Handle missing values
    preprocessor.handle_missing_values(strategy='fill')  # Or 'drop'

    # Save processed data in the specified directory
    preprocessor.save_processed_data(output_dir, output_dir)

    print("Data preprocessing completed and saved.")
