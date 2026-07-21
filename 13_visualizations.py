import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# Monthly Spending chart
conn = sqlite3.connect('finance.db')

monthly = pd.read_sql("""
    SELECT SUBSTR(date, 1, 7) AS month, SUM(amount) AS total_amount
    FROM invoices
    GROUP BY month
    ORDER BY month
""", conn)

print(monthly)

fig, ax = plt.subplots(figsize=(12, 5))

ax.bar(monthly['month'], monthly['total_amount'] / 1_000_000, color='steelblue')

ax.set_title('Monthly Invoice Amount — 2025', fontsize=14)
ax.set_xlabel('Month')
ax.set_ylabel('Amount (COP millions)')
ax.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('chart_monthly_spending.png', dpi=150)
print("Saved: chart_monthly_spending.png")

# AP Aging chart
aging = pd.read_sql("""
    SELECT 
        CASE 
            WHEN julianday('2025-12-31') - julianday(date) <= 30  THEN '1. 0-30 days'
            WHEN julianday('2025-12-31') - julianday(date) <= 60  THEN '2. 31-60 days'
            WHEN julianday('2025-12-31') - julianday(date) <= 90  THEN '3. 61-90 days'
            ELSE '4. 90+ days'
        END AS aging_bucket,
        SUM(amount) AS total_outstanding
    FROM invoices
    WHERE invoice_id NOT IN (
        SELECT DISTINCT invoice_id FROM payments WHERE invoice_id IS NOT NULL
    )
    GROUP BY aging_bucket
    ORDER BY aging_bucket
""", conn)

fig, ax = plt.subplots(figsize=(8, 5))
colors = ['#2ecc71', '#f39c12', '#e67e22', '#e74c3c']
ax.bar(aging['aging_bucket'], aging['total_outstanding'] / 1_000_000, color=colors)
ax.set_title('AP Aging Report — Unpaid Invoices', fontsize=14)
ax.set_xlabel('Aging Bucket')
ax.set_ylabel('Outstanding Amount (COP millions)')
plt.tight_layout()
plt.savefig('chart_ap_aging.png', dpi=150)
print("Saved: chart_ap_aging.png")

