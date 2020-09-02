"""Juego tres rayas"""
import random
import time
import os

def presentacion_1():
    """Devuelve el nivel en el que quiere jugar el usuario"""
    
    print()
    print()
    print("                 TRES EN RAYA")
    print()
    print()
    print("                 1. Fácil")
    print("                 2. Difícil")
    print()
    print()

    nivel = ""
    while nivel != "1" and nivel != "2":
        nivel = input("                 -->")
    return int(nivel)


def presentacion_2():
    """devuelve la ficha elegida por el usuario y la ficha por el ordenador"""    
    
    print()
    print()
    print("                 TRES EN RAYA")
    print()
    print()
    print("                 Sale fa ficha O")
    print("                 Elige: O / X")
    print()
    print()

    ficha = ""
    while ficha != "O" and ficha != "X":
        ficha = input("                 -->").upper()

    if ficha == "O":
        humano = "O"
        ordenador = "X"
    else :
        humano = "X"
        ordenador = "O"
    return humano,ordenador


def mostrar_tablero(tablero):
    """Muestra el tablero con las casillas vacias y las fichas puestas"""
    
    print()    
    print("                 TRES EN RAYA")
    print()
    print("     1       |2      |3")
    print("          {}  |  {}    |   {}".format(tablero[0],tablero[1],tablero[2]))
    print("             |       |")
    print("     --------+-------+-----")
    print("     4       |5      |6")
    print("          {}  |  {}    |   {}".format(tablero[3],tablero[4],tablero[5]))
    print("             |       |")
    print("     --------+-------+-----")
    print("     7       |8      |9")
    print("          {}  |  {}    |   {}".format(tablero[6],tablero[7],tablero[8]))
    print("             |       |")
    print()

def seguir_jugando():
    """Devuelve True si el usuario quiere jugar otra partida, sino False"""
    
    print()
    respuesta = input("         ¿Otra? partida (s)").lower()
    if respuesta == "s" or respuesta == "si":
        return True
    else:
        return False

def hay_ganador(tablero,jugador):
    """Comprueba si el estado del tablero es ganador: Tiene tres fichas en raya"""
    if tablero[0] == tablero[1] == tablero[2] == jugador or\
       tablero[3] == tablero[4] == tablero[5] == jugador or\
       tablero[6] == tablero[7] == tablero[8] == jugador or\
       tablero[1] == tablero[4] == tablero[7] == jugador or\
       tablero[2] == tablero[5] == tablero[8] == jugador or\
       tablero[0] == tablero[3] == tablero[6] == jugador or\
       tablero[0] == tablero[4] == tablero[8] == jugador or\
       tablero[2] == tablero[4] == tablero[6] == jugador:

       return True
    else :
       return False

def tablero_lleno(tablero):
    """devuelve True si el tablero esta lleno, y False si teiene campos disponibles"""
    for i in tablero:
        tablero_lleno = False
        if i == " ":
            tablero_lleno = True        

def casilla_libre(tablero,casilla):
    """Devuelve True si una casilla dada está  vacía  y False  si está llena"""
    return tablero[casilla] == " "

def movimiento_jugador(tablero):
    """Devuelve la casilla elegida por el jugador humano"""
    posiciones  = ["1","2","3","4","5","6","7","8","9"]
    posicion = None
    while True:
        if posicion not in posiciones:       
            #print(type(posicion))     
            posicion = input ("             Te toca (1,9): ")
        else:
            posicion = int(posicion)            
            if not casilla_libre(tablero,posicion-1):
                print("        Esta posicion esta ocupada")
            else:
                return posicion-1

def movimiento_ordenador_facil(tablero,jugador):
    """El ordenador sólo se defiende de ser ganado en la siguiente jugada"""
    if tablero[0] == tablero[1] == jugador and tablero[2] == " ":
        casilla = 2
    elif tablero[0] == tablero[2] == jugador and tablero[1] ==" ":
        casilla = 1
    elif tablero[1] == tablero[2] == jugador and tablero[0] ==" ":
        casilla = 0

    elif tablero[3]== tablero[4] == jugador and tablero[5] ==" ":
        casilla = 5
    elif tablero[3] == tablero[5] == jugador and tablero[4] ==" ":
        casilla = 4
    elif tablero[4] == tablero[5] == jugador and tablero[3] ==" ":
        casilla = 3

    elif tablero[6]== tablero[7] == jugador and tablero[8] ==" ":
        casilla = 8
    elif tablero[6] == tablero[8] == jugador and tablero[7] ==" ":
        casilla = 7
    elif tablero[7] == tablero[8] == jugador and tablero[6] ==" ":
        casilla = 6

    elif tablero[0]== tablero[3] == jugador and tablero[6] ==" ":
        casilla = 6
    elif tablero[0] == tablero[6] == jugador and tablero[3] ==" ":
        casilla = 3
    elif tablero[3] == tablero[6] == jugador and tablero[0] ==" ":
        casilla = 0
    
    elif tablero[1]== tablero[4] == jugador and tablero[7] ==" ":
        casilla = 7
    elif tablero[1] == tablero[7] == jugador and tablero[4] ==" ":
        casilla = 4
    elif tablero[4] == tablero[7] == jugador and tablero[1] ==" ":
        casilla = 1

    elif tablero[2]== tablero[5] == jugador and tablero[8] ==" ":
        casilla = 8
    elif tablero[2] == tablero[8] == jugador and tablero[5] ==" ":
        casilla = 5
    elif tablero[5] == tablero[8] == jugador and tablero[2] ==" ":
        casilla = 2

    elif tablero[0]== tablero[4] == jugador and tablero[8] ==" ":
        casilla = 8
    elif tablero[0] == tablero[8] == jugador and tablero[4] ==" ":
        casilla = 4
    elif tablero[4] == tablero[8] == jugador and tablero[0] ==" ":
        casilla = 0

    elif tablero[2]== tablero[4] == jugador and tablero[6] ==" ":
        casilla = 6
    elif tablero[2] == tablero[6] == jugador and tablero[4] ==" ":
        casilla = 4
    elif tablero[6] == tablero[4] == jugador and tablero[2] ==" ":
        casilla = 2
    else :
        while True:
            casilla = random.randint(0,8)
            if tablero[casilla] == " ":
                break
                    
    return casilla

def movimiento_ordenador_facil2(tablero, jugador):
    print(tablero)
############ PROGRAMA PRINCIPAL ##########
jugando = True
while jugando:
    tablero = [" "]*9
    os.system("cls")

    nivel = presentacion_1()
    os.system("cls")

    # Eligir nivel y ficha (turno)
    humano, ordenador = presentacion_2()
    os.system("cls")
    
    mostrar_tablero(tablero)

    if humano == "O":
        turno = "Humano"
    else:
        turno = "Ordenador"

    partida  = True
    while partida:        
        # Si es el turno del jugador humano mueve el usuario 
            #Cambiar el espacio vacio de la lista por la ficha de ese jugador
            #Compobar si ha ganado
            #Si ha ganado se sale de la partida y se muestra el ganador
        #si el turno es del ordenador, mueve el ordenador deacuerdo al nivel elegido
            #Cambiar el espacio vacio de la lista por la ficha de ese jugador
            #Compobar si ha ganado
            #Si ha ganado se sale de la partida y se muestra el ganador
        #Tras cada movimiento hay que comprobar si hay empate.
            # si hay empate se sale de la partida y se muestra que hay empate            
        #print(tablero)
        if tablero_lleno(tablero):
            print("             Empate")
            partida = False

        elif turno  == "Humano":
            casilla = movimiento_jugador(tablero)
            #print("La casilla que esogio el humano es",casilla, "La var humano es:",humano)
            #time.sleep(10)
            tablero[casilla] = humano
            turno = "Ordenador"
            os.system("cls")
            mostrar_tablero(tablero)

            if hay_ganador(tablero,humano):
                print("             Has ganado")
                partida = False
        elif turno == "Ordenador":
            print("            El Ordenador esta pensando ...")
            time.sleep(2)
            if nivel == 1:
                casilla = movimiento_ordenador_facil(tablero,humano)
                #movimiento_ordenador_facil2(tablero,humano)
            tablero[casilla] = ordenador
            turno = "Humano"
            #os.system("cls")
            mostrar_tablero(tablero)
            if hay_ganador(tablero,ordenador):
                print("            has perdido")
                partida =False

    jugando = seguir_jugando()