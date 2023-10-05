import pandas as pd

pd.set_option('display.max_columns', None)
df = pd.read_parquet("TABLE_X_PART_CLASS_PARAMS.parquet", engine='fastparquet')
# df.to_json('table_site_part.parquet.json')
df.to_csv('TABLE_X_PART_CLASS_PARAMS.csv')
print(df.columns)
# df.info()
# print(df[['TransactionTime', 'OBJID', 'INSTANCE_NAME', 'SERIAL_NO', 'S_SERIAL_NO',
       # 'INVOICE_NO', 'SHIP_DATE']])