import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_transactions(n=900, output_path="../data/transactions.csv"):
    categories = ["Groceries", "Rent", "Utilities", "Dining", "Travel",
                  "Entertainment", "Healthcare", "Shopping", "Fuel"]

    merchants = {
        "Groceries": ["Walmart", "Target", "Kroger"],
        "Rent": ["Landlord"],
        "Utilities": ["Electric Co", "Water Co"],
        "Dining": ["McDonalds", "Starbucks", "Chipotle"],
        "Travel": ["Uber", "Lyft", "Airlines"],
        "Entertainment": ["Netflix", "AMC"],
        "Healthcare": ["CVS", "Walgreens"],
        "Shopping": ["Amazon", "BestBuy"],
        "Fuel": ["Shell", "Exxon"]
    }

    start_date = datetime(2024, 1, 1)
    data = []

    for _ in range(n):
        category = random.choice(categories)
        merchant = random.choice(merchants[category])
        amount = round(np.random.exponential(scale=50), 2)

        if category == "Rent":
            amount = 1200

        transaction = {
            "Transaction_ID": random.randint(100000, 999999),
            "Date": start_date + timedelta(days=random.randint(0, 365)),
            "Category": category,
            "Merchant": merchant,
            "Amount": amount
        }
        data.append(transaction)

    df = pd.DataFrame(data)
    df.to_csv(output_path, index=False)
    print(f"Generated {n} transactions at {output_path}")