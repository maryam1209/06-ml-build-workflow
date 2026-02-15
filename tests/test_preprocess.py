import pandas as pd
from src.preprocess import load_and_clean

def test_load_and_clean():
    df = load_and_clean("data/sample.csv")
    
    # Check dataframe is not empty
    assert not df.empty
    
    # Check no missing values remain
    assert df.isnull().sum().sum() == 0
