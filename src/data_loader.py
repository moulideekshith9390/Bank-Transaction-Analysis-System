import pandas as pd

def load_data(path="../data/transactions.csv"):
    df = pd.read_csv(path, parse_dates=["Date"])
    return df