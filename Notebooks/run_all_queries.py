import sqlite3

conn = sqlite3.connect("Data/db/bluestock_mf.db")
cursor = conn.cursor()

queries = {
    "1. Average NAV":
    "SELECT AVG(nav) FROM fact_nav;",

    "2. Maximum NAV":
    "SELECT MAX(nav) FROM fact_nav;",

    "3. Total Transactions":
    "SELECT COUNT(*) FROM fact_transactions;",

    "4. Total SIP Amount":
    "SELECT SUM(amount_inr) FROM fact_transactions WHERE transaction_type='SIP';",

    "5. Total Redemption Amount":
    "SELECT SUM(amount_inr) FROM fact_transactions WHERE transaction_type='Redemption';",

    "6. Total Lumpsum Amount":
    "SELECT SUM(amount_inr) FROM fact_transactions WHERE transaction_type='Lumpsum';",

    "7. Average Expense Ratio":
    "SELECT AVG(expense_ratio_pct) FROM fact_performance;",

    "8. Highest 5-Year Return":
    "SELECT MAX(return_5yr_pct) FROM fact_performance;",

    "9. Total Funds":
    "SELECT COUNT(*) FROM fact_performance;",

    "10. Negative Sharpe Ratios":
    "SELECT COUNT(*) FROM fact_performance WHERE sharpe_ratio < 0;"
}

for title, query in queries.items():
    print("\n" + "="*50)
    print(title)
    print("="*50)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

conn.close()