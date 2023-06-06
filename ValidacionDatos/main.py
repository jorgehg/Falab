import xml.etree.ElementTree as et
import oracledb as ora
import pandas as pd

def main():    
    """ cur = conexionDB()

    df_cuentas_sql = pd.DataFrame(cur.execute("SELECT * FROM TB_BCRES_CUENTAS where idsolicitud = '200000156'"))
    field_names_cuentas = [i[0] for i in cur.description]
    df_cuentas_sql.columns = field_names_cuentas """

    responses_buro = getXML(validarID('200000156'))
    #leerCuentas(responses_buro[2][4])
    print((responses_buro[2][4][0].find('NombreOtorgante').text))

    



def lecturaXML(url):
    with open(url) as file:
        texto = file.read()
        texto = texto.replace(' xmlns="http://bean.consulta.ws.bc.com/"','')
    return texto

def validarID(id):
    if id == '':
        print('Inserte ID a validar')
        id = input()
    directorio = id+'\\'+id
    return directorio

def getXML(directorio):
    responses_buro = []
    responses_buro.append(et.fromstring(lecturaXML(directorio+"_bc_pre.xml"))[0][0][0])
    try:
        responses_buro.append(et.fromstring(lecturaXML(directorio+"_bc_eva.xml"))[0][0][0])
    except:
        print('NO CIRCULO')
        responses_buro.append(None)
    responses_buro.append(et.fromstring(lecturaXML(directorio+"_bc_pro.xml"))[0][0][0])
    return responses_buro

def conexionDB():
    ora.init_oracle_client(r"instantclient-basic-windows.x64-21.10.0.0.0dbru\instantclient_21_10")
    db = ora.connect(user="UATMXPR",password="uatmx286p5",host="10.1.36.125", port=1531, service_name="ecmxpr")
    cur = db.cursor()
    return cur

#def compareCuentas():

def leerCuentas(cuentas):
    for i in cuentas:
        i=1



if __name__ == "__main__":
    main()