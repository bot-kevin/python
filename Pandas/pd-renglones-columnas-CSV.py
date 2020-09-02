import pandas as pd

####################### -----> SELECCIONAR RENGLONES CON NUMEROS <----- ###############
datos = pd.read_csv('ATP.csv')

#print(datos.head(5))

# IMPRIMIR 5 RENGLONES 
datos.iloc[0:5]

# IMPRIMIR RENGLONES SALTEADOS , [0,5,23,10] Y SE PONE LA COMA AL FINAL
datos.iloc[[0, 5, 23, 10] , ]

# IMPRIMIR COLUMNAS
datos.iloc[:3 ,0:2]

# RENGLONES Y COLUMNAS EN DESORDEN
datos.iloc[ [0,3,6,4] ,[0,2] ] 

####################### -----> SELECCIONAR RENGLONES CON NOMBRE DE COLUMNA <----- ###############

# MODIFICAR EL INDICE 
datos.set_index('Location', inplace=True)

# FILTRACIÓN DE SOLO LO RELACIONADO CON MELBOURNE
datos.loc['Melbourne']

# HACER UNA BUSQUED DE TODO LO QUE TENGA QUE VER CON ATLANTA Y SUPERFICIE
datos.loc['Atlanta','Surface']
# SELECCIONAR CON RANGO DE COLUMNA Y FILTRADO RE FILAS
datos.loc[ ['Atlanta','Melbourne'], 'Series':'Round']




