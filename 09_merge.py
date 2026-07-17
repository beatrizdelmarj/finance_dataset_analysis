import pandas as pd

invoices = pd.read_csv('invoices_clean.csv')
payments = pd.read_csv('payments_clean.csv')

resultado = invoices.merge(payments, on='invoice_id', how='left')
print(resultado.shape)
print(resultado.head())

print(payments['invoice_id'].value_counts().head(10))

# Facturas sin pago (pendientes)
sin_pago = resultado[resultado['payment_id'].isna()]
print(f"Facturas sin pago: {len(sin_pago)}")

# Pagos huérfanos (invoice_id en payments que no existe en invoices)
huerfanos = payments[~payments['invoice_id'].isin(invoices['invoice_id'])]
print(f"Pagos huérfanos: {len(huerfanos)}")

resultado.to_csv('invoices_payments.csv', index=False)
print(f"Saved: invoices_payments.csv — {len(resultado)} rows")

