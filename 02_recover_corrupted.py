import pandas as pd
import io

# Reading file invoices_2025
invoices = pd.read_csv('invoices_2025.csv')

# Filter by corrupted rows or csv parsing error
corrupt_rows = invoices[invoices['invoice_id'].str.contains(',', na=False)]
print(f"Corrupted rows: {len(corrupt_rows)}")
print(corrupt_rows['invoice_id'].head(5))

# Separating the clean rows from the unclean ones
clean_rows = invoices[~invoices['invoice_id'].str.contains(',', na=False)]
print(f"Cleaned rows: {len(clean_rows)}")

# Verifying that both variables add up to the total of 808 lines of the original file.
total_rows = len(corrupt_rows) + len(clean_rows)
print(f"Total rows: {total_rows}")

# Creating a backup file with the corrupted rows since the variable is temporary in Python and saving with .to_csv anchors the information to disk (traceability)
corrupt_rows.to_csv('02.1_corrupted_rows_backup.csv', index=False)
print("Backup saved as: 02.1_corrupted_rows_backup.csv")

# Defining a function parse_row to parsing every corrupted rows
def parse_row(row):
    row_parse = pd.read_csv(io.StringIO(row), header=None).iloc[0]
    return row_parse

recovered_rows = corrupt_rows['invoice_id'].apply(parse_row)
recovered_rows.columns = ['invoice_id','date','vendor','category','amount','status']

print(recovered_rows.head())
print(f'Total rows: {len(recovered_rows)}')
print(recovered_rows.isnull().sum())

# Merging clean_rows with recovered_rows in invoices_full
invoices_full = pd.concat([clean_rows, recovered_rows], ignore_index=True)
invoices_full.info()

# Saving invoices_full as a CSV file
invoices_full.to_csv('02.2_invoices_full.csv', index=False)
print(f"Saved: 02.2_invoices_full.csv — {len(invoices_full)} rows")