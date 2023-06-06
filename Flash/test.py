import pandas as pd

direccion_diccionario = r'diccionario.csv'

df = pd.read_csv(direccion_diccionario)


dfDiccionario = pd.Series(df['CamposNuevos'])
dfDiccionario.index = df['CamposViejos']
print(dfDiccionario['Estrategia Apertura.Input.Antecedente.number1'])