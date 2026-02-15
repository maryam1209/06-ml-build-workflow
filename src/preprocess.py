import pandas as pd

def load_and_clean(file_path):
    """
    Loads a CSV file and drops rows with missing values.
    """
    df = pd.read_csv(file_path)
    df_clean = df.dropna()
    return df_clean
