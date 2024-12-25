import pandas as pd

def load_well_data(file_path):
    """
    Load well data from a CSV file.
    """
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        return data
    except FileNotFoundError:
        print("Error: File not found.")
        return None
