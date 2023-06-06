import csv,os,time

def main():
    os.remove("Resultado.csv")
    time.sleep(1)
    with open("MotorActual.csv") as MotorActual, open("MotorNuevo.csv") as MotorNuevo, open("Resultado.csv",'w',newline='') as Resultado:
        
            readerMA = csv.reader(MotorActual)
            readerMN = csv.reader(MotorNuevo)
            writerResultado = csv.writer(Resultado)
            readerMAlist = list(readerMA)
            readerMNlist = list(readerMN)
            discr = []
            discranexo = []
            counted = ['Auxiliar LDS.Default.VAR_DECIMAL_15_2_DEFAULT']

            for a in range(len(readerMAlist)):
                if a == 0 or readerMNlist[a][0] in counted or a in range(127,146) or a in range(155,167): continue
                counted.append(readerMNlist[a][0])
                for b in range(len(readerMAlist[a])):
                    if b ==0:continue
                    lista = []
                    lista = correctorMA(readerMAlist[a][b],readerMNlist[a][b])
                    fieldMA = lista[0]
                    fieldMN = lista[1]
                    if fieldMA != fieldMN and validate(fieldMA,fieldMN,readerMNlist[a][0]):
                        discranexo = []
                        discranexo.append(readerMNlist[0][b])
                        discranexo.append(readerMNlist[a][0])
                        discranexo.append(fieldMA)
                        discranexo.append(fieldMN)
                        writerResultado.writerow(discranexo)
                        discr.append(discranexo)
                if a == 353: break

def validate(campo1,campo2,campoNombre):
    if (campo1 == 0 and campo2 == "Null")or(campo1 == "Null" and campo2 == 0)or(campoNombre=="Input LDS.Datos Buro.TipoSIC[1]" and campo1 == 0 and campo2 == 1)or(campoNombre=="Filler88X30")or(isinstance(campo1, int) and isinstance(campo2, int) and campo1 > 3 and (abs(campo1-campo2)<2)):
         return False
    else:
         return True
    
def correctorMA(campo1,campo2):
    lista = [campo1,campo2]

    for i in range(len(lista)):
        if lista[i] == '10101': lista[i] = 'Null'
        if lista[i] == 'FEMALE': lista[i] = 'F'
        if lista[i] == r"\0": lista[i] = 'Null'
        if lista[i] == 'EMPLEADO':lista[i] = '1'
        if lista[i] == '1.00E+12':lista[i] = 'Null'
        if lista[i] == '1E+13':lista[i] = 'Null'
        if lista[i] == '1.00E+13':lista[i] = 'Null'
        if lista[i] == '1E+13':lista[i] = 'Null'
        if lista[i] == '1E+12':lista[i] = 'Null'
        if lista[i] == '10101':lista[i] = 'Null'
        if lista[i] == '00010101':lista[i] = 'Null'
        if lista[i] == '9999': lista[i] = 'Null' 
        if lista[i] == 'Revision Manual':lista[i] = 'Decision Manual'
        if lista[i] == 'Aprobado':lista[i] = 'Aceptado'
        if lista[i] == 'AMARILLO':lista[i] = 'A'
        if lista[i] == 'VERDE':lista[i] = 'V'
        if lista[i] == 'ROJO':lista[i] = 'R'
        if lista[i] == '':lista[i] = 'Null'
        if lista[i] == '999999999999.99':lista[i] = 'Null'
        if lista[i] == '9999999999999.99':lista[i] = 'Null'
        if lista[i] == '19000101':lista[i] = 'Null'
        try: lista[i] = int(lista[i]) 
        except: lista[i] = lista[i]
        
    

    return lista
     

if __name__ == "__main__":
    main() 
    print("TERMINADO")