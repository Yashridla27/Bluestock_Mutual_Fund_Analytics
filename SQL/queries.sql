-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3. Total SIP inflow
SELECT SUM(amount_inr) AS total_sip
FROM fact_transactions
WHERE transaction_type='SIP';

-- 4. Total Redemption
SELECT SUM(amount_inr) AS total_redemption
FROM fact_transactions
WHERE transaction_type='Redemption';

-- 5. Total Lumpsum
SELECT SUM(amount_inr) AS total_lumpsum
FROM fact_transactions
WHERE transaction_type='Lumpsum';

-- 6. Funds with expense ratio less than 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 7. Highest 5 year return funds
SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- 8. Average expense ratio
SELECT AVG(expense_ratio_pct)
FROM fact_performance;

-- 9. Count transactions
SELECT COUNT(*)
FROM fact_transactions;

-- 10. Maximum NAV
SELECT MAX(nav)
FROM fact_nav;