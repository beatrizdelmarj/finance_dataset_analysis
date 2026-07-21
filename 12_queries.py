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

conn.close()
