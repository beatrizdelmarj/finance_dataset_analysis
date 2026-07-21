import sqlite3
import pandas as pd

conn = sqlite3.connect('finance.db')

invoices = pd.read_csv('invoices_clean.csv')
payments = pd.read_csv('payments_clean.csv')

invoices.to_sql('invoices', conn, if_exists='replace', index=False)
payments.to_sql('payments', conn, if_exists='replace', index=False)

print(f"Table 'invoices': {len(invoices)} rows loaded")
print(f"Table 'payments': {len(payments)} rows loaded")
print("Database ready: finance.db")

conn.close()
