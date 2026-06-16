import pandas as pd
facturas = pd.read_csv('facturas_2025.csv')
pagos = pd.read_csv('pagos_2025.csv')

print(f'Facturas {facturas.columns}')
