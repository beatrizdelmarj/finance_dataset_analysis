import sqlite3
import pandas as pd

conn = sqlite3.connect('finance.db')

# Total spending by vendor
query = """
SELECT vendor, SUM(amount) AS total_amount, COUNT(*) AS invoice_count
FROM invoices
GROUP BY vendor
ORDER BY total_amount DESC
LIMIT 10
"""

result = pd.read_sql(query, conn)
print(result)


# Spending by category
query2 = """
SELECT category, SUM(amount) AS total_amount, COUNT(*) AS invoice_count
FROM invoices
GROUP BY category
ORDER BY total_amount DESC
"""

result2 = pd.read_sql(query2, conn)
print(result2)

# AP Aging Report
query3 = """
SELECT 
    aging_bucket,
    COUNT(*) AS invoice_count,
    SUM(amount) AS total_outstanding
FROM (
    SELECT 
        amount,
        CASE 
            WHEN julianday('2025-12-31') - julianday(date) <= 30  THEN '1. 0-30 days'
            WHEN julianday('2025-12-31') - julianday(date) <= 60  THEN '2. 31-60 days'
            WHEN julianday('2025-12-31') - julianday(date) <= 90  THEN '3. 61-90 days'
            ELSE '4. 90+ days'
        END AS aging_bucket
    FROM invoices
    WHERE invoice_id NOT IN (
        SELECT DISTINCT invoice_id FROM payments 
        WHERE invoice_id IS NOT NULL
    )
)
GROUP BY aging_bucket
ORDER BY aging_bucket
"""

result3 = pd.read_sql(query3, conn)
print(result3)

# Payment methods breakdown
query4 = """
SELECT 
    method,
    COUNT(*) AS payment_count,
    SUM(amount_paid) AS total_paid,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM payments), 1) AS pct_of_payments
FROM payments
WHERE method != 'UNKNOWN'
GROUP BY method
ORDER BY total_paid DESC
"""

# Note: UNKNOWN (77 payments, 13.6%) excluded — method pending treasury confirmation
result4 = pd.read_sql(query4, conn)
print(result4)

# Monthly spending trend
query5 = """
SELECT 
    SUBSTR(date, 1, 7) AS month,
    COUNT(*) AS invoice_count,
    SUM(amount) AS total_amount
FROM invoices
GROUP BY month
ORDER BY month
"""

result5 = pd.read_sql(query5, conn)
print(result5)


conn.close()
