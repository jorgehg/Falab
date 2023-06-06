import pandas as pd
df1 = pd.read_csv("MotorActual.csv")
df2 = pd.read_csv("MotorNuevo.csv")


print(df1.apply(tuple,1))