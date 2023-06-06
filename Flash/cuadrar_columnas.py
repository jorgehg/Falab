import pandas as pd
import csv,os

template = pd.read_csv('template.csv')
template.index = template[template.columns[0]]
template = template.drop(columns=[template.columns[0]])
print(template)
df = pd.read_csv(r'C:\Users\ext_johirayg\Documents\Comparacion26Marzo\ResultadosMotorNuevo.csv')
df.index = df[df.columns[0]]
df = df.drop(columns=[df.columns[0]])

print(df)
for column in template.columns:
    for index in template.index:
        try:
            template.at[index,column] = df.at[index,column] 
        except:
            template.at[index,column] = 0
print(template)

template.to_csv('MotorNuevoFix.csv')
""" 
for column, index, value in zip(template.columns,template.index) """
