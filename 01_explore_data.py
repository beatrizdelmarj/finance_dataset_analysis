import pandas as pd

# Load the datasets
invoices = pd.read_csv('invoices_2025.csv')
payments = pd.read_csv('payments_2025.csv')

# ============================================================
# INVOICES EXPLORATION
# ============================================================
print("=" * 60)
print("INVOICES DATASET")
print("=" * 60)

print(f"\nShape: {invoices.shape[0]} rows, {invoices.shape[1]} columns")

print("\nColumn names:")
print(list(invoices.columns))

print("\nData types:")
print(invoices.dtypes)

print("\nFirst 5 rows:")
print(invoices.head())

print("\nMissing values (nulls):")
print(invoices.isnull().sum())

print("\nBasic statistics:")
print(invoices.describe())

# ============================================================
# PAYMENTS EXPLORATION
# ============================================================
print("\n" + "=" * 60)
print("PAYMENTS DATASET")
print("=" * 60)

print(f"\nShape: {payments.shape[0]} rows, {payments.shape[1]} columns")

print("\nColumn names:")
print(list(payments.columns))

print("\nData types:")
print(payments.dtypes)

print("\nFirst 5 rows:")
print(payments.head())

print("\nMissing values (nulls):")
print(payments.isnull().sum())

print("\nBasic statistics:")
print(payments.describe())

print(invoices[invoices['amount'].isnull()].head(10))
print(invoices[invoices['amount'].isnull()][['invoice_id', 'date', 'amount']].head(10))

#Este codigo muestra que hay 211 lineas corruptas
filas_corruptas = invoices[invoices['invoice_id'].str.contains(',', na=False)]
print(f"Filas corruptas: {len(filas_corruptas)}")
print(filas_corruptas['invoice_id'].head(5))
# DECISION: 211 rows have comma-separated data inside invoice_id — CSV parsing error.
# These rows are unrecoverable without the original source system.
# Action: drop before cleaning. This reduces the dataset from 808 to ~597 rows.
