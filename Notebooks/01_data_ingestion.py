"""
Mutual Fund Analytics Capstone Project

File: 01_data_ingestion.py

Purpose:
Loads raw mutual fund datasets from CSV files and performs initial data ingestion
for further ETL and analytical processing.

Author: Yash Ridla
Date: June 2026
"""
import pandas as pd
import os

data_folder = "Data/Raw"

# Read all CSV files from Raw folder    
print("Files found in Data folder:\n")

for file in os.listdir(data_folder):
    if file.endswith(".csv"):
        file_path = os.path.join(data_folder, file)

        try:    
            df = pd.read_csv(file_path)

            print("=" * 50)
            print(f"File: {file}")
            print(f"Rows, Columns: {df.shape}")
            print("\nColumns:")
            print(df.columns.tolist())
            print("\nFirst 5 Rows:")
            print(df.head())
            print("\n")

        except Exception as e:
            print(f"Error reading {file}: {e}")

# Existing code

# Fund master analysis
fund_master = pd.read_csv("Data/Raw/01_fund_master.csv")

print("Unique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

# Validate that all AMFI codes in fund_master exist in nav_history

fund_master = pd.read_csv("Data/Raw/01_fund_master.csv")
nav_history = pd.read_csv("Data/Raw/02_nav_history.csv")

fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

print("\nMissing Codes:")
print(fund_codes - nav_codes)