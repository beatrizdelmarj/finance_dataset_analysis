import pandas as pd

invoices = pd.read_csv('invoices_clean.csv')

print(f'Total rows: {len(invoices)}')
print(f'Duplicated rows: {invoices.duplicated().sum()}')

# Saving duplicated invoices in dropped_duplicates.csv
duplicates = invoices[invoices.duplicated()]
duplicates.to_csv('dropped_duplicates.csv', index=False)

# Deleting from invoices_clean.csv the 27 invoices duplicated
invoices = invoices.drop_duplicates()
print(f'Total rows: {len(invoices)}')

# Saving changes in invoices_clean.csv
invoices.to_csv('invoices_clean.csv', index=False)
print(f"Saved: invoices_clean.csv - 718 rows, duplicates removed")

