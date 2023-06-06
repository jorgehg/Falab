import os

with open("texto.txt", 'r') as file:
    texto = file.read()

texto = texto.replace("'Variables Auxiliares.Calc_Clasif para Cupo'", "'Auxiliar LDS.Cupo.ClasifCupo'")
texto = texto.replace("""'Variables Auxiliares.Input_Flag BC o CC' = "0" ""","""'Input LDS.Datos Buro.TipoSIC'[1] = "1" """)
texto = texto.replace("'Variables Auxiliares.Input_Flag Pre Evaluacion Conexion'","'Input LDS.Datos Buro.ConexionConectado'[1]")
texto = texto.replace("'Variables Auxiliares.Input_BC Score'","'Auxiliar LDS.Score.BCScore'")
texto = texto.replace("""'Variables Auxiliares.Input_Flag BC o CC' = "1" ""","""'Input LDS.Datos Buro.TipoSIC'[2] = "1" """)
texto = texto.replace("'Variables Auxiliares.Input_Flag Pre Evaluacion Conexion CC'","'Input LDS.Datos Buro.ConexionConectado'[2]")
texto = texto.replace("'Variables Auxiliares.Input_FICO Score'","'Auxiliar LDS.Score.FICOScore'")
texto = texto.replace("'Variables Auxiliares.ScoreConExpConTC_ScoreCalc'","'Auxiliar LDS.ScoreConExpConTC.ScoreCalc'")
texto = texto.replace("'Variables Auxiliares.ScoreConExpSinTC_ScoreCalc'","'Auxiliar LDS.ScoreConExpSinTC.ScoreCalc'")
texto = texto.replace("'Variables Auxiliares.Input_Score Trans'", "'Input LDS.Datos Cliente Existente.RFMScoreTrans'")
texto = texto.replace("'Variables Auxiliares.Calc_Grupo RFM'","'Auxiliar LDS.RFM.GrupoRFM'")
texto = texto.replace("'Variables Auxiliares.Input_Flag RFM'","'Input LDS.Datos Cliente Existente.RFMFlag'")
texto = texto.replace("'Variables Auxiliares.Calc_Cupo por Rescate'","'Auxiliar LDS.Cupo.CupoPorRescate'")
texto = texto.replace("'Variables Auxiliares.Input_Conteo MOP 4 U12M'","'Auxiliar LDS.Cuenta.Conteo MOP 4 U12M'")
texto = texto.replace("'Variables Auxiliares.Input_MOP 5 Historico'","'Auxiliar LDS.Cuenta.MOP 5 Historico'")
texto = texto.replace("'Variables Auxiliares.Calc_Flag Rescate Score Int'","'Auxiliar LDS.Cupo.FlagRescate_ScoreInt'")
texto = texto.replace("'Variables Auxiliares.Calc_Edad'","'Auxiliar LDS.Solicitud.Edad'")
texto = texto.replace("'Variables Auxiliares.ScoreSocioDemo_CODIGO_POSTAL'","'Input LDS.Datos Cliente Existente.CodigoPostal'")
texto = texto.replace("'Variables Auxiliares.Input_Sucursal Entry Level'","'Auxiliar LDS.Solicitud.SucursalEntryLevel'")
texto = texto.replace("'Variables Auxiliares.Input_MOP Actual'","'Auxiliar LDS.Cuenta.MOP_Actual'")
texto = texto.replace("'Variables Auxiliares.ScoreBuro_PEOR_MOP_ACTUAL_MORAS'","'Auxiliar LDS.Cuenta.ScoreBuro_PEOR_MOP_ACTUAL_MORAS'")
texto = texto.replace("'Variables Auxiliares.Input_Sumatoria Saldo Actual con MOP 2'","'Auxiliar LDS.Cuenta.SumatoriaSaldoActualconMOP2'")
texto = texto.replace("'Variables Auxiliares.Calc_Match RFM Duda'","'Auxiliar LDS.RFM.Match_RFM_Duda'")
texto = texto.replace("'Variables Auxiliares.Calc_Meses de Antiguedad Laboral'","'Auxiliar LDS.Empleo.MesesAntiguedadLaboral'")
texto = texto.replace("'Estrategia Apertura.Rsltd.Evaluacion.RCode'","'Resultados LDS.EvalProducto.Oferta.Tarjeta.Politicas.TablaCodigosRazon TJ1'")
texto = texto.replace("'Variables Auxiliares.Calc_Años de Antiguedad Laboral'","'Auxiliar LDS.Empleo.AniosAntiguedadLaboral'")
texto = texto.replace("'Estrategia Apertura.Input.Antecedente.filler1'","'Auxiliar LDS.Cupo.UniversoPF'")
texto = texto.replace("'Estrategia Apertura.Rsltd.Evaluacion.DTable'","'Resultados LDS.EvalProducto.Oferta.Tarjeta.Politicas.TablaDecision TJ1'")
texto = texto.replace("Decision Manual","Revision Manual")

os.remove("texto.txt")
with open("texto.txt", 'w') as file:
    file.write(texto)

