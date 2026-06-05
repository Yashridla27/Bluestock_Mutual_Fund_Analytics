import pandas as pd

# Load NAV History dataset
nav = pd.read_csv("Data/Raw/02_nav_history.csv")

print("Shape:")
print(nav.shape)

print("\nColumns:")
print(nav.columns.tolist())

print("\nFirst 5 Rows:")
print(nav.head())

# Convert date column to datetime
nav['date'] = pd.to_datetime(nav['date'])

print("\nData Types:")
print(nav.dtypes)

# Sort data
nav = nav.sort_values(by=['amfi_code', 'date'])

print("\nAfter Sorting:")
print(nav.head())

#check for duplicates
print(nav.duplicated().sum())

#NAV validation
print("\nInvalid NAV Values:")
print((nav['nav'] <= 0).sum())

#save cleaned data
nav.to_csv("Data/Processed/clean_nav.csv", index=False)
print("clean_nav.csv saved successfully")


#Task 2: Clean 08_investor_transactions.csv
print("\n\n----- INVESTOR TRANSACTIONS -----")

transactions = pd.read_csv("Data/Raw/08_investor_transactions.csv")

print("Shape:")
print(transactions.shape)

print("\nColumns:")
print(transactions.columns.tolist())

print("\nFirst 5 Rows:")
print(transactions.head())

print("\nTransaction Types:")
print(transactions['transaction_type'].unique())

#Amount validation
print("\nInvalid Amounts:")
print((transactions['amount_inr'] <= 0).sum())

#KYC Status check
print("\nKYC Status:")
print(transactions['kyc_status'].unique())

# Convert transaction date to datetime
transactions['transaction_date'] = pd.to_datetime(
    transactions['transaction_date']
)

print("\nTransaction Date Type:")
print(transactions['transaction_date'].dtype)

#save cleaned transactions data
transactions.to_csv("Data/Processed/clean_transactions.csv",index=False)

print("clean_transactions.csv saved successfully")

#Task 3: 07_scheme_performance.csv
print("\n\n----- SCHEME PERFORMANCE -----")

performance = pd.read_csv("Data/Raw/07_scheme_performance.csv")

print("Shape:")
print(performance.shape)

print("\nColumns:")
print(performance.columns.tolist())

print("\nFirst 5 Rows:")
print(performance.head())

# Check return columns are numeric
print("\nReturn Data Types:")

print(performance[['return_1yr_pct','return_3yr_pct','return_5yr_pct']].dtypes)

# Negative Sharpe Ratio
negative_sharpe = (performance['sharpe_ratio'] < 0).sum()

print("\nNegative Sharpe Ratios:")
print(negative_sharpe)

# Expense Ratio Range Check
invalid_expense = performance[(performance['expense_ratio_pct'] < 0.1) |(performance['expense_ratio_pct'] > 2.5)]
print("\nInvalid Expense Ratios:")
print(len(invalid_expense))

#save cleaned performance data
performance.to_csv("Data/Processed/clean_performance.csv",index=False)
print("clean_performance.csv saved successfully")