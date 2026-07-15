import pandas as pd

invoices = pd.read_csv('invoices_clean.csv')

# Cleaning supplier column with .str.strip + .str.upper
invoices['vendor'] = invoices['vendor'].str.strip()
invoices['vendor'] = invoices['vendor'].str.upper()
print(sorted(invoices['vendor'].unique()))

# Using a dictionary for the  rest of 5 supplier name pending to normalize

vendor_mapping = {
    'ASEO TOTAL S.A.S': 'ASEO TOTAL SAS',
    'CAFÉ DE LA MONTANA': 'CAFE DE LA MONTANA',
    'DIST. EL SOL SAS': 'DISTRIBUIDORA EL SOL SAS',
    'DISTRIBUIDORA EL SOL S.A.S': 'DISTRIBUIDORA EL SOL SAS',
    'PAPELERÍA CENTRAL': 'PAPELERIA CENTRAL',
}

invoices['vendor'] = invoices['vendor'].replace(vendor_mapping)

print(invoices['vendor'].nunique())

# Cleaning status column with .str.strip + .str.upper
invoices['status'] = invoices['status'].str.strip()
invoices['status'] = invoices['status'].str.upper()
print(sorted(invoices['status'].unique()))

# Translating some status column

status_mapping = {
'PENDIENTE': 'PENDING',
'PAGADA':'PAID',
'ANULADA':'CANCELLED',
}
invoices['status'] = invoices['status'].replace(status_mapping)

print(invoices['status'].nunique())

# Saving changes in invoices_clean.csv

invoices.to_csv('invoices_clean.csv', index=False)
print(f"Saved: invoices_clean.csv - vendors normalized, status translated")

