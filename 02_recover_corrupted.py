import pandas as pd
import io

# Reading file invoices_2025
invoices = pd.read_csv('invoices_2025.csv')

# Filter by corrupted rows or csv parsing error
filas_corruptas = invoices[invoices['invoice_id'].str.contains(',', na=False)]
print(f"Filas corruptas: {len(filas_corruptas)}")
print(filas_corruptas['invoice_id'].head(5))

# Separating the clean rows from the unclean ones
filas_limpias = invoices[~invoices['invoice_id'].str.contains(',', na=False)]
print(f"Filas limpias: {len(filas_limpias)}")

# Verifying that both variables add up to the total of 808 lines of the original file.
total_filas = len(filas_corruptas) + len(filas_limpias)
print(f"Total Filas: {total_filas}")

# Creating a backup file with the corrupted rows since the variable is temporary in Python and saving with .to_csv anchors the information to disk (traceability)
filas_corruptas.to_csv('corrupted_rows_backup.csv', index=False)
print("Backup guardado: corrupted_rows_backup.csv")

# Defining a function parse_row to parsing every corrupted rows
def parse_row(row):
    row_parse = pd.read_csv(io.StringIO(row), header=None).iloc[0]
    return row_parse

recovered = filas_corruptas['invoice_id'].apply(parse_row)
recovered.columns = ['invoice_id','date','vendor','category','amount','status']

print(recovered.head())