import pandas as pd
import csv, os

carpeta_header = r'campos.csv'
with open(carpeta_header) as headerfile:
    header = next(csv.reader(headerfile))

header[0] = 'IDSOLICITUD'
df = pd.DataFrame(columns=header)
carpeta_outputs = r"C:\Users\ext_johirayg\Documents\Comparacion26Marzo\InputsMotorNuevo\\"

files = os.listdir(carpeta_outputs)

for file in files:
    df2 = pd.read_csv(carpeta_outputs+file,low_memory=False)
    common_columns = df.columns.intersection(df2.columns)
    df2_filtered = df2[common_columns]
    df = pd.concat([df,df2_filtered],ignore_index=True)

print('Nombre archivos:')
nombre_archivo = input()
df.to_csv(nombre_archivo+'.csv',index=False)
print('Proceso Exitoso')
