import os
def dibuja_presentacion ():
    """Muestra al usuario su menu inicial"""    
    print()    
    print("         Juego de adivinar la palabra")
    print()    
    print("                 1. Jugar")
    print("                 2. Ayuda")
    print()
    opcion = ""
    while opcion != '1' and opcion != '2':
        opcion = input('Ingrese su opcion (1/2): ')
    return int(opcion)
def ayuda():
    """Ayuda del juego"""
    print()
    print('           Este es un juego muy bueno')

def dibujar_tablero(palabra,vidas, pierde):
    print()
    print("    Juego Cuerda")
    print()
    if (pierde): print("  !oh!, Esa letra no es :( ")    
    print("  Vidas: ", vidas)
    print(" ", ("---*"*len(palabra)))    
    i = 0
    acu = " |"
    while i < len(palabra):
        acu += " {} |".format(palabra[i])
        i +=1
    print (acu)    
    print(" ","---*"*len(palabra))


def busca_y_reemplazar(palabra,palabra_oculta,letra):
    for i in palabra: 
        if letra == i:
            posicion = palabra.index(letra)
            palabra_oculta.pop(posicion) 
            palabra_oculta.insert(posicion, letra)                                   
            palabra.pop(posicion)
            palabra.insert(posicion, "*")        
    return palabra_oculta

if __name__ == "__main__":
      
    if dibuja_presentacion() == 1:
        os.system("clear")        
        palabra = list(input('Ingrese la palabra: '))        
        palabra_oculta = list(" " * len(palabra))
        vidas = 5
        dibujar_tablero(palabra_oculta,vidas,False)
        comova = list()
        

        while vidas != 0:              
            print()
            letra  = input('Ingrese un letra: ')
            if letra in palabra:
                comova = busca_y_reemplazar(palabra,palabra_oculta,letra)
                os.system("clear")
                dibujar_tablero(palabra_oculta,vidas,False)
            else :
                os.system("clear")
                vidas -= 1
                dibujar_tablero(palabra_oculta,vidas, True)                
                   
    else :
        ayuda()

    

       
    
    