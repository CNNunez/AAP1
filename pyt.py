from Generator.dominoes import * 
from FuerzaBruta import *
from BackTracking import *
import copy

#######################################
#           Main principal            #
#######################################

Tablero = []
Fichas = []
# PRIMERO CREAR EL TABLERO
#Este recibe un N con la cantidad a generar
def creacion(n):
    global Tablero
    global Fichas
    board = True
    while(type(board) == bool):
        board = create_puzzle(n)        
    tiles = make_tiles(n)

    Tablero = copy.deepcopy(board)
    Fichas = copy.deepcopy(tiles)

#Recibie un n para saber cual algoritmo llamar 0 = Fuerza Bruta, 1 = Backtracking
def main(m):
    if(m == 0):
        print(main_FB(copy.deepcopy(Tablero),copy.deepcopy(Fichas)))
    elif(m == 1):
        main_btk(copy.deepcopy(Tablero))
#######################################
#        Main para Fuerza Bruta       #
#######################################
def main_FB(board,tiles):
    num_solu = listaCero(len(tiles))
    final = []

    #Este ciclo es para probar todas las posiciones posibles x cada ficha
    for i in range(2**len(tiles)):
        
        if( fuerza_bruta(copy.deepcopy(board),copy.deepcopy(tiles),num_solu) ):
            final.append(copy.deepcopy(num_solu))
        
        #Sino funciono entonces hay que cambiar la lista de ceros, para probar otra posicion
        cambio(num_solu)
        
    return final

#Esto para tener una lista con el numero de fichas y de posiciones de cada una
def listaCero(n):
    lista = []
    for i in range(n):
            lista.append(0)
    return lista

#Este algoritmo es para cambiar los valores entre 0 y 1
#Esto para que el algortimos "se devuelva" y pruebe otra posicion
def cambio(lista):
    for i in range(1,len(lista)+1):
        if(lista[-i]) == 0:
            lista[-i] = 1
            return
        else:
            lista[-i] = 0


#######################################
#        Main para Backtracking       #
#######################################
def main_btk(board):
    lista_resultados = []
    Medicion_Analitica = []
    Medicion_Empirica = []
    result,hist,time_emp,time_an = backtracking(board)
    Medicion_Empirica.append(time_emp)
    Medicion_Analitica.append(time_an)
    for coord in hist:
        lista_resultados.append(result[coord[0]][coord[1]])
    print(lista_resultados)