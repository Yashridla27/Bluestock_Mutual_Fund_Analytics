import pandas as pd
from sqlalchemy import create_engine

# Connect to SQLite database
engine = create_engine("sqlite:///Data/db/bluestock_mf.db")

# Load cleaned CSV files
nav = pd.read_csv("Data/Processed/clean_nav.csv")
transactions = pd.read_csv("Data/Processed/clean_transactions.csv")
performance = pd.read_csv("Data/Processed/clean_performance.csv")

# Load data into tables
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("All cleaned datasets loaded successfully!")