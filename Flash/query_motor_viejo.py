import oracledb as ora
import csv,os
import pandas as pd

# Inicializacion de base de datos
print('Conectando con base de datos...')
ora.init_oracle_client(r"C:\Users\ext_johirayg\Documents\Desarrollo\Originacion_Input_Generator\instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9")
db = ora.connect(user="UATMXPR",password="uatmx286p5",host="10.1.36.125", port=1531, service_name="ecmxpr")
cur = db.cursor()

with open(r'C:\Users\ext_johirayg\Documents\Desarrollo\Flash\Request Motor Interactive 2.txt') as f:
    query = f.read()

query = query.replace(';','')

df = pd.DataFrame(cur.execute(query).fetchall())

db.close()

df = df.drop_duplicates(subset=df.columns[0])
df = df.drop(columns=df.columns[2])
print(df)

df.to_csv('3001-3021.csv',index=False)

