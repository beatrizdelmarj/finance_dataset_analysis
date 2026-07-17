import pandas as pd

invoices = pd.read_csv('invoices_clean.csv')

#Removing $ in amount column from the DB
invoices['amount'] = invoices['amount'].str.replace('$','', regex=False)

#Removing COP in amount column from the DB
invoices['amount'] = invoices['amount'].str.replace('COP','', regex=False)

#Removing spaces in amount column from the DB
invoices['amount'] = invoices['amount'].str.replace(' ','', regex=False)

#Removing . in amount column from DB
invoices['amount'] = invoices['amount'].str.replace('.','', regex=False)

#Removing , in amount column from DB
invoices['amount'] = invoices['amount'].str.replace(',','', regex=False)

#Converting from string format to numeric format
invoices['amount'] = pd.to_numeric(invoices['amount'])
print(invoices['amount'].dtype)
print(invoices['amount'].describe())

print(invoices['amount'].head(10))
print(invoices['amount'].unique()[:20])

print(invoices[invoices['amount'] == invoices['amount'].max()])

#There is a strange value in .max option, then I will mark as audit_flag
#      invoice_id        date                vendor   category      amount   status
#591  F-2025-0653  2025-07-13  Cafe de la Montana    Cafeteria  1001410000  pending
invoices['audit_flag'] =''
invoices.loc[invoices['amount'] == invoices['amount'].max(), 'audit_flag'] = 'suspicious amount - pending audit'
print(invoices[invoices['audit_flag'] != ''][['invoice_id', 'vendor', 'amount', 'audit_flag']])

invoices.to_csv('invoices_clean.csv', index=False)

#To see if there are , data values in amount column
#print(invoices[invoices['amount'].str.contains(',', regex=False)]['amount'].head(10))

#To see if there is any decimal values that uses . in amount column
#tiene_punto = invoices[invoices['amount'].str.contains('\.', regex=True)]
#print(tiene_punto['amount'].unique()[:15])
