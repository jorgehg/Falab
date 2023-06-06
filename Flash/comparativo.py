import csv,os
import pandas as pd

direccion_motor_viejo = r'C:\Users\ext_johirayg\Documents\Comparacion26Marzo\ResultadosMotorActual.csv'
direccion_motor_nuevo = r'C:\Users\ext_johirayg\Documents\Comparacion26Marzo\ResultadosMotorNuevo.csv'
direccion_diccionario = r'diccionario.csv'

dfMotorViejo = pd.read_csv(direccion_motor_viejo)
dfMotorNuevo = pd.read_csv(direccion_motor_nuevo)
dfDiccionario = pd.read_csv(direccion_diccionario)
df = pd.read_csv(direccion_diccionario)

dfDiccionario = pd.Series(df['CamposNuevos'])
dfDiccionario.index = df['CamposViejos']

resultado = pd.DataFrame(columns=['ID','Variables','ValorViejo','ValorNuevo'])

dfMotorViejo.index = dfMotorViejo['IDSOLICITUD']
dfMotorNuevo.index = dfMotorNuevo['IDSOLICITUD']

dfMotorViejo=dfMotorViejo.drop(columns=['IDSOLICITUD'])
dfMotorNuevo= dfMotorNuevo.drop(columns=['IDSOLICITUD'])

print(dfMotorNuevo)
print(dfMotorViejo)
print(dfDiccionario)


for column in dfMotorViejo.columns:
    print(column)
    for index in dfMotorViejo.index:
        valorDiccionario = dfDiccionario[column]
        valorMotorViejo = dfMotorViejo.at[index,column]
        valorMotorNuevo = dfMotorNuevo.at[index,valorDiccionario]

        if valorMotorViejo != valorMotorNuevo:
            add = {'ID': column,
    	        'Variables': valorDiccionario,
	            'ValorViejo': valorMotorViejo,
                'ValorNuevo': valorMotorNuevo}

            resultado = resultado._append(add,ignore_index=True)

print(resultado)
resultado.to_csv('comparativa.csv',index=False)