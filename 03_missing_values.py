import pandas as pd

invoices_null = pd.read_csv('02.2_invoices_full.csv')

invoices_null.info()

percentage = ((invoices_null.isnull().sum()) / len(invoices_null) ) * 100

null_report = pd.DataFrame({
    'nulls': invoices_null.isnull().sum(),
    'percentage': percentage.round(1)
})
print(null_report)

# CLEANING DECISIONS:
# date     → DROP_in_dropped_invoices.csv: invoices without date cannot be audited or aged
# amount   → DROP_in_dropped_invoices.csv: invoices without amount have no financial obligation
# category → FILL 'unknown': invoice is valid but cannot be categorized in reports
# status   → FILL 'pending': AP default — if not marked as paid, treat as outstanding

#Back up for rows with null data in date and amount
dropped = invoices_null[invoices_null['date'].isnull() | invoices_null['amount'].isnull()]
dropped.to_csv('dropped_invoices.csv', index=False)
print(f'Rows reclasified to dropped_invoices: {len(dropped)}')

print(dropped[['date', 'amount']].isnull().sum())

#Deleting invoices with null data in date and amount to work with the final dataset
invoices_clean = invoices_null.dropna(subset=['date', 'amount'])

#Filling cells from category and status columns that are null values
invoices_clean['category'] = invoices_clean['category'].fillna('unknown')
invoices_clean['status'] = invoices_clean['status'].fillna('pending')
print(invoices_clean.isnull().sum())

#Saving cleaned Datatset
invoices_clean.to_csv('invoices_clean.csv', index=False)
print(f"Saved: invoices_clean.csv - {len(invoices_clean)} rows")

