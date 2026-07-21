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

conn.close()
