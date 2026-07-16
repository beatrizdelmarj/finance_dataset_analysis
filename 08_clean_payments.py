import pandas as pd
import io

## Loading the dataset

payments = pd.read_csv('payments_2025.csv')
#print(payments.head(10))
#print(payments.describe())
#print(payments.info())

## Recover corrupted rows - csv parsing error

corrupt_rows = payments[payments['payment_id'].str.contains(',', na=False)]
print(f"Filas corruptas: {len(corrupt_rows)}")
print(corrupt_rows['payment_id'].head(5))
# DECISION: CSV parsing error - count shown above

## Handle Nulls

# Separating the clean rows from the unclean ones
clean_rows = payments[~payments['payment_id'].str.contains(',', na=False)]
print(f"Cleaned rows: {len(clean_rows)}")
print(clean_rows['payment_id'].head(5))

# Verifying that both variables add up to the total of 565 lines of the original file.
total_rows = len(corrupt_rows) + len(clean_rows)
print(f"Total rows: {total_rows}")

# Creating a backup file with the corrupted rows since the variable is temporary in Python and saving with .to_csv anchors the information to disk (traceability)
corrupt_rows.to_csv('08.1_payments_corrupted_rows_backup.csv', index=False)
print("Backup saved as: 08.1_payments_corrupted_rows_backup.csv")

# Defining a function parse_row to parsing every corrupted rows
def parse_row(row):
    row_parse = pd.read_csv(io.StringIO(row), header=None).iloc[0]
    return row_parse

recovered_rows = corrupt_rows['payment_id'].apply(parse_row)
recovered_rows.columns = ['payment_id','invoice_id','payment_date','amount_paid','method']

print(recovered_rows.head())
print(f'Total rows: {len(recovered_rows)}')
print(recovered_rows.isnull().sum())

# Merging clean_rows with recovered_rows in payments_full
payments_full = pd.concat([clean_rows, recovered_rows], ignore_index=True)
payments_full.info()

payments_full['method'] = payments_full['method'].fillna('UNKNOWN')
print(payments_full['method'].value_counts())

## Clean payment payment_date

payments_full['payment_date'] = pd.to_datetime(payments_full['payment_date'], format='mixed', dayfirst=True)
print(payments_full['payment_date'].dtype)
print(payments_full['payment_date'].head(10))

#Checking there is not any NaT - Not a time - value or not parsed payment_dates
print(f'total payment_dates null: {payments_full['payment_date'].isnull().sum()}')

## Clean amount paid

#Removing $ in amount_paid column from the DB
payments_full['amount_paid'] = payments_full['amount_paid'].str.replace('$','', regex=False)

#Removing COP in amount_paid column from the DB
payments_full['amount_paid'] = payments_full['amount_paid'].str.replace('COP','', regex=False)

#Removing spaces in amount_paid column from the DB
payments_full['amount_paid'] = payments_full['amount_paid'].str.replace(' ','', regex=False)

#Removing . in amount_paid column from DB
payments_full['amount_paid'] = payments_full['amount_paid'].str.replace('.','', regex=False)

#Removing , in amount_paid column from DB
payments_full['amount_paid'] = payments_full['amount_paid'].str.replace(',','', regex=False)

#Converting from string format to numeric format
payments_full['amount_paid'] = pd.to_numeric(payments_full['amount_paid'])

# Using Int64 - type nullable pandas- for amount_paid column which has NaN values
payments_full['amount_paid'] = payments_full['amount_paid'].astype('Int64')
print(payments_full['amount_paid'].dtype)
print(payments_full['amount_paid'].describe())


## Normalize method

# Cleaning supplier column with .str.strip + .str.upper
payments_full['method'] = payments_full['method'].str.strip()
payments_full['method'] = payments_full['method'].str.upper()
print(sorted(payments_full['method'].unique()))
print(payments_full['method'].nunique())

# Saving changes in payments_clean.csv
payments_full.to_csv('payments_clean.csv', index=False)
print(f"Saved: payments_clean.csv - {len(payments_full)} rows, method normalized")

