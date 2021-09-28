from Generator.dominoes import * 
from FuerzaBruta import *
import copy

"""
 Opcion principal que crea el tablero y todas las posibles fichas
"""
def main(n):
    board = True
    while(type(board) == bool):
        board = create_puzzle(n)        
    tiles = make_tiles(n)
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
