import pandas as pd
import numpy as np
datos = {
    'Nombre':['Camilo','Yolanda','Daniel','Kevin','Daniela'],
    'Calificaciones':['100','90','40','30','50'],
    'Deportes':['Fútbol','Natación','Basquetbol','Beisbol','Ciclismo'],
    'Materias':['Calculo','Metodos numericos', 'Cocina','Quimica','Sociales']
}
df  =  pd.DataFrame(datos)
#print(df)
print('\n' *2)
# DATOS NO VALIDOS
datos2 = {
    'Nombre':['Camilo','Yolanda','N/A','Kevin','Daniela'],
    'Calificaciones':['100',np.nan,'40','30','50'],
    'Deportes':['Fútbol','Natación','Basquetbol','N/A','Ciclismo'],
    'Materias':['Calculo','Lima', 'Cocina','Quimica','Sociales']
}
df2 = pd.DataFrame(datos2)
#print(df2)
print('\n' *2)
# VER INFORMACION BASICA DEL DATAFRAME
    #print(df2.info())
# VER ESTADISTICAS DEL DATAFRAME
    #print(df2.describe())

#BUSCAR Y REEMPLAZAR
nuevo = pd.DataFrame(df2)
nuevo = nuevo.replace(np.nan,'0')
#print(nuevo)

# ELIMINAR LA LINEA QUE TENGA UN CAMPO N/A
nuevo2 = pd.DataFrame(df2)
nuevo2.dropna(how='any',inplace=True)
#print(nuevo2)

# ELIMINAR REGISTRO BUSCANDO POR COLUMNA
columna = df2[df2['Nombre'] != 'N/A']
#print(columna)

# LLENAR CON CEROS CUALQUIER VALOR CON n/a EN EL DATAFRAME
nuevo3 = pd.DataFrame(df2)
nuevo3.fillna(0,inplace=True)
#print(nuevo3)
#print(nuevo3.describe())

# COMVERTIR A ENTEROS LOS ESTRING 
nuevo2['Calificaciones'] = nuevo2.Calificaciones.astype(int)
#print(nuevo2.describe())

# ESTADISTICAS INDIVIDUALES
print("Estaditica primedio: ", nuevo2['Calificaciones'].mean())
