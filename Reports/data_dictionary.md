# Data Dictionary

## dim_fund

| Column Name | Description |
|------------|------------|
| amfi_code | Unique AMFI code of the mutual fund |
| scheme_name | Name of the mutual fund scheme |
| fund_house | Fund house managing the scheme |
| category | Mutual fund category |

---

## fact_nav

| Column Name | Description |
|------------|------------|
| amfi_code | Mutual fund AMFI code |
| nav_date | Date of NAV record |
| nav | Net Asset Value |

---

## fact_transactions

| Column Name | Description |
|------------|------------|
| investor_id | Unique investor identifier |
| transaction_date | Date of transaction |
| amfi_code | Mutual fund AMFI code |
| transaction_type | SIP, Redemption or Lumpsum |
| amount_inr | Transaction amount in INR |

---

## fact_performance

| Column Name | Description |
|------------|------------|
| amfi_code | Mutual fund AMFI code |
| return_1yr_pct | One year return percentage |
| return_3yr_pct | Three year return percentage |
| return_5yr_pct | Five year return percentage |
| sharpe_ratio | Risk adjusted performance measure |
| expense_ratio_pct | Expense ratio percentage |

---

## dim_benchmark

| Column Name | Description |
|------------|------------|
| benchmark_name | Name of benchmark index |
| benchmark_return | Benchmark return percentage |