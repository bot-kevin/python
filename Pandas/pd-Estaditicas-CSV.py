import pandas as pd
import numpy as np

# LEER EL ARCHIVO CSV 
datos  = pd.read_csv('ATP.csv')

# VER COMO VIENE EL ARCHIVO
    #print(datos.info())
    #print(datos.head())

# REEMPLAZAR LOS DATOS DE TIPO N/A
nuevo  =pd.DataFrame(datos)
nuevo = nuevo.replace(np.nan, "0")

# CONVERTIR A NUMERO ENTEROS
#print(nuevo.describe(include=[np.number]))
nuevo = nuevo.replace('N/A','0')
nuevo =nuevo.replace('NR','0')
print(nuevo.describe)

