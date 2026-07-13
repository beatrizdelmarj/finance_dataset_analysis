import pandas as pd

invoices = pd.read_csv('invoices_clean.csv')

#Seeing dates formats
print(invoices['date'].unique()[:20])

#Converting all date to a single standard format YYYY-MM-DD international standard
invoices['date'] = pd.to_datetime(invoices['date'], format='mixed', dayfirst=True)
print(invoices['date'].dtype)
print(invoices['date'].head(10))

#Checking there is not any NaT - Not a time - value or not parsed dates
print(f'total dates null: {invoices['date'].isnull().sum()}')

#Saving dataset with dates converted to ISO 8601
invoices.to_csv('invoices_clean.csv', index=False)
print("Saved: invoices_clean.csv with clean dates")
