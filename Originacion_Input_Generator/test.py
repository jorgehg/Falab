import pandas as pd
import csv, os
import oracledb as ora

ora.init_oracle_client(r"instantclient-basic-windows.x64-21.9.0.0.0dbru\instantclient_21_9")
db = ora.connect(user="UATMXPR",password="uatmx286p5",host="10.1.36.125", port=1531, service_name="ecmxpr")
cur = db.cursor()
# Se obtiene el directorio de queries e inicializan listas necesarias
files = os.listdir('queries')
queries = []

# Se leen las IDs de solicitudes
df = pd.read_csv('cuentas.csv')
cuentas = df[df.columns[0]]

# Declaracion de variables y calculos
solicitudes = ""
dataframes = []
dataframes_fake = []
iteraciones = len(cuentas)//250
residuo = len(cuentas) % 250
isResiduo = False

# Lectura de encabezado de datos input
with open('input.csv','r') as inputcsv:
    reader = csv.reader(inputcsv)
    header = next(reader)
header.insert(0,'IDSOLICITUD')

# Se crean los dataframes con los IDs divididos
for i in range(iteraciones):
    principio = i*250
    fin = (i+1)*250
    solicitudes = ''
    queries = []
    dataframes_fake = []
    dataframes.append(pd.DataFrame())
    if isResiduo:
        principio+=250
        fin+=250+residuo
        i+=1
    dataframes[i]['ID'] = cuentas[(principio):fin]
    # Se crea el string con las solicitudes formateadas para juntarlas a los queries
    for id in cuentas[principio:fin]:
        solicitudes = solicitudes + "'"+str(id)+"'," 
    
    for file in files:
        with open('queries/'+file,'r') as f:
            queries.append(f.read()) 
    # Formateo de queries
    for y in range(len(queries)):
        queries[y] = queries[y].replace(';','')
        queries[y] = queries[y].replace('S0L1C1TUD3S',solicitudes[:-1])

    # Inicializacion de dataframes. Se ejecutan los queries en la base de datos con el cursor de la conexion a Oracle
    for y in range(len(queries)):
        dataframes_fake.append(pd.DataFrame(cur.execute(queries[y]).fetchall()))
        dataframes_fake[y].rename(columns={dataframes_fake[y].columns[0]:'ID'},inplace=True)
        dataframes_fake[y]['ID'] = dataframes_fake[y]['ID'].astype(int)
    # Se juntan los resultados de las distintas tablas
    
    resultado = dataframes[i].merge(dataframes_fake[0],on=dataframes[i].columns[0],suffixes=('a', 'b')).merge(dataframes_fake[1],on=dataframes[i].columns[0],suffixes=('c', 'd')).merge(dataframes_fake[2],on=dataframes[i].columns[0],suffixes=('e', 'f')).merge(dataframes_fake[3],on=dataframes[i].columns[0],suffixes=('g', 'h')).merge(df,on=dataframes[i].columns[0])
    dataframes[i] = resultado
    dataframes[i].columns = header

    dataframes[i] = dataframes[i].drop_duplicates(subset=['IDSOLICITUD'])

    outfile = str(principio+1)+'-'+str(fin)+'.csv'
    dataframes[i].to_csv(outfile,index=False)
    print('LISTO. Proceso Finalizado. Archivo Exportado: ', outfile)

    if(i+1==iteraciones and residuo != 0):
        isResiduo = True
        i-=1       

        principio = i*250
    fin = (i+1)*250
    solicitudes = ''
    queries = []
    dataframes_fake = []
    dataframes.append(pd.DataFrame())
    if isResiduo:
        principio+=250
        fin+=250+residuo
        i+=1
    dataframes[i]['ID'] = cuentas[(principio):fin]
    # Se crea el string con las solicitudes formateadas para juntarlas a los queries
    for id in cuentas[principio:fin]:
        solicitudes = solicitudes + "'"+str(id)+"'," 
    
    for file in files:
        with open('queries/'+file,'r') as f:
            queries.append(f.read()) 
    # Formateo de queries
    for y in range(len(queries)):
        queries[y] = queries[y].replace(';','')
        queries[y] = queries[y].replace('S0L1C1TUD3S',solicitudes[:-1])

    # Inicializacion de dataframes. Se ejecutan los queries en la base de datos con el cursor de la conexion a Oracle
    for y in range(len(queries)):
        dataframes_fake.append(pd.DataFrame(cur.execute(queries[y]).fetchall()))
        dataframes_fake[y].rename(columns={dataframes_fake[y].columns[0]:'ID'},inplace=True)
        dataframes_fake[y]['ID'] = dataframes_fake[y]['ID'].astype(int)
    # Se juntan los resultados de las distintas tablas
    
    resultado = dataframes[i].merge(dataframes_fake[0],on=dataframes[i].columns[0],suffixes=('a', 'b')).merge(dataframes_fake[1],on=dataframes[i].columns[0],suffixes=('c', 'd')).merge(dataframes_fake[2],on=dataframes[i].columns[0],suffixes=('e', 'f')).merge(dataframes_fake[3],on=dataframes[i].columns[0],suffixes=('g', 'h')).merge(df,on=dataframes[i].columns[0])
    dataframes[i] = resultado
    dataframes[i].columns = header

    dataframes[i] = dataframes[i].drop_duplicates(subset=['IDSOLICITUD'])

    outfile = str(principio+1)+'-'+str(fin)+'.csv'
    dataframes[i].to_csv(outfile,index=False)
    print('LISTO. Proceso Finalizado. Archivo Exportado: ', outfile)

    if(i+1==iteraciones and residuo != 0):
        isResiduo = True
        i-=1       


solicitudes = ''
queries = []
dataframes_fake = []
dataframe = pd.DataFrame()

dataframe['ID'] = cuentas
# Se crea el string con las solicitudes formateadas para juntarlas a los queries
for id in cuentas:
    solicitudes = solicitudes + "'"+str(id)+"'," 

for file in files:
    with open('queries/'+file,'r') as f:
        queries.append(f.read()) 
# Formateo de queries
for y in range(len(queries)):
    queries[y] = queries[y].replace(';','')
    queries[y] = queries[y].replace('S0L1C1TUD3S',solicitudes[:-1])

# Inicializacion de dataframes. Se ejecutan los queries en la base de datos con el cursor de la conexion a Oracle
for y in range(len(queries)):
    dataframes_fake.append(pd.DataFrame(cur.execute(queries[y]).fetchall()))
    dataframes_fake[y].rename(columns={dataframes_fake[y].columns[0]:'ID'},inplace=True)
    dataframes_fake[y]['ID'] = dataframes_fake[y]['ID'].astype(int)
# Se juntan los resultados de las distintas tablas

resultado = dataframe.merge(dataframes_fake[0],on=dataframes[i].columns[0],suffixes=('a', 'b')).merge(dataframes_fake[1],on=dataframes[i].columns[0],suffixes=('c', 'd')).merge(dataframes_fake[2],on=dataframes[i].columns[0],suffixes=('e', 'f')).merge(dataframes_fake[3],on=dataframes[i].columns[0],suffixes=('g', 'h')).merge(df,on=dataframes[i].columns[0])
dataframe = resultado
dataframe.columns = header

dataframe = dataframe.drop_duplicates(subset=['IDSOLICITUD'])

outfile = 'pruebasLeslie.csv'
dataframes[i].to_csv(outfile,index=False)
print('LISTO. Proceso Finalizado. Archivo Exportado: ', outfile)



db.close() 

print('LISTOOOOOOOOOOOOOO')