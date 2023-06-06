import oracledb as ora
import csv,os
import pandas as pd

# Inicializacion de base de datos
print('Conectando con base de datos...')
ora.init_oracle_client(r"instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9")
db = ora.connect(user="UATMXPR",password="uatmx286p5",host="10.1.36.125", port=1531, service_name="ecmxpr")
cur = db.cursor()
# Se obtiene el directorio de queries e inicializan listas necesarias
files = os.listdir('queries')
queries = []
dataframes = []

# Ingresa usuario las cuentas que desea solicitar
print('Ingrese las solicitudes que desea realizar:')
solicitudes = input()

# Se leen queries de archivos txt
print('Leyendo Queries...')
for file in files:
    with open('queries/'+file,'r') as f:
        queries.append(f.read()) 

# Formateo de queries        
for i in range(len(queries)):
    queries[i] = queries[i].replace(';','')
    queries[i] = queries[i].replace('S0L1C1TUD3S',solicitudes)
    
# Lectura de encabezado de datos input
with open('input.csv','r') as inputcsv:
    reader = csv.reader(inputcsv)
    header = next(reader)

print('Ejecutando queries...')
# Inicializacion de dataframes. Se ejecutan los queries en la base de datos con el cursor de la conexion a Oracle
for i in range(len(queries)):
    dataframes.append(pd.DataFrame(cur.execute(queries[i]).fetchall()))
db.close()
print('Formateando datos...')
# Se juntan los resultados de las distintas tablas
df = dataframes[0].merge(dataframes[1],on=dataframes[0].columns[0],suffixes=('table1', 'table2')).merge(dataframes[2],on=dataframes[0].columns[0],suffixes=('table2', 'table3')).merge(dataframes[3],on=dataframes[0].columns[0],suffixes=('table3', 'table4'))

# Se asigna el encabezado leido del input.csv al dataframe
header.insert(0,'ID')
df.columns = header

# Impresion y eliminacion de filas duplicadas de cada dataframe
""" for i in range(len(dataframes)):
    print(dataframes[i]) """

#Se eliminan filas completamente duplicadas, se setea como index del dataframe las IDs extraidas de la BD y se elimina como columna.
df = df.drop_duplicates(subset=['ID'])
df.index = df['ID'].tolist()
df = df.drop(columns=['ID'])

print('Exportando CSV...')

# Dataframe subido a csv
outfile = 'pruebaRemapeo.csv'
df.to_csv(outfile)
print('LISTO. Proceso Finalizado. Archivo Exportado: ', outfile)