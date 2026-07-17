import pandas as pd

invoices = pd.read_csv('invoices_clean.csv')
payments = pd.read_csv('payments_clean.csv')

print(invoices.info())
print(payments.info())
print(invoices[invoices['amount'] <= 0])
print(payments[payments['amount_paid'] <= 0])

print(f"Total invoices: {len(invoices)}")
print(f"Total payments: {len(payments)}")
print(f"Total invoiced amount: {invoices['amount'].sum():,}")
print(f"Total paid amount: {payments['amount_paid'].sum():,}")
