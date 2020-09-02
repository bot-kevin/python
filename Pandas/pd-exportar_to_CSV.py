import pandas as pd

datos = pd.read_csv('ATP.csv')

df = pd.DataFrame(datos)

# EXPORTAR TODO LOS DATOS
 #df.reset_index().to_csv('Datos_exportador.csv', header=True, index=False)

#EXPORTAR UNA FILTRACION 
df = datos.iloc[0:5:,0:3] 
df.reset_index().to_csv('Filtrado.csv', header=True,index=False)

