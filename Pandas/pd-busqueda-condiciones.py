import pandas as pd

datos =pd.read_csv('ATP.csv')
# CAMBIAR EL INDEX O COLUMNA PRINCIPAL
datos.set_index('Location',inplace=True)

#filtras del campo cancha (Court) las que sean al aire libre (Outdoor), y las columnas que quiero ver

datos.loc[ datos['Court']=='Outdoor ' , ['Surface','Winner'] ]

# mas de una condicion 

print(datos.loc[ datos['Series'].str.endswith("Slam")&(datos['Surface']=='Clay')&(datos['Winner']=='Ferder R.')&(datos['Round']=='The final')])



