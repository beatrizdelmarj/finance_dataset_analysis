import pandas as pd
facturas = pd.read_csv('facturas_2025.csv')
pagos = pd.read_csv('pagos_2025.csv')

rename_columns = {
    'factura_id':'invoice_id',
    'fecha':'date',
    'proveedor': 'vendor',
    'categoria': 'category',
    'monto':'amount',
    'estado':'status'
}

rename_pagos= {
    'pago_id':'payment_id',
    'factura_id':'invoice_id',
    'fecha_pago': 'payment_date',
    'monto_pagado':'amount_paid',
    'metodo':'method'
}

facturas = facturas.rename(columns=rename_columns)
pagos = pagos.rename(columns=rename_pagos)

print(f'New columns name in facturas_2025.csv:')
print(facturas.columns.to_list())

print(f'New columns name in pagos_2025.csv:')
print(pagos.columns.to_list())

facturas.to_csv('invoices_2025.csv', index=False)
pagos.to_csv('payments_2025.csv', index=False)

print(f'Files saved:')
print(f'invoices_2025.csv')
print(f'payments_2025.csv')

