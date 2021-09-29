
###########################################################################################
#           ES EL MISMO ARCHIVO QUE PYT.PY PERO TIENE UN FOR GRANDE PARA PRUEBAS           #
###########################################################################################
from timeit import default_timer as timer
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
        print("Solucion Fuerza Bruta")
        start = timer()
        print(main_FB(copy.deepcopy(Tablero),copy.deepcopy(Fichas)))
        end = timer()
        tiempo = (end-start) * 1000000
        print("Tiempo ejecucion", tiempo)
    elif(m == 1):
        print("Solucion BackTracking")
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
    print("Los resultados obtenidos de las mediciones: ")
    print('- Empirico: ',Medicion_Empirica)
    print('- Analitico: ',Medicion_Analitica)    
    print(lista_resultados)

#######################################
#        Main para pruebas            #
#######################################

def pruebas():
    #lista_entrada = [1,2,4,2,5,3,4,1,3,5,4,5,5,2]
    lista_entrada = [1,2,3]
    for n in lista_entrada:
        creacion(n)
        main(0)
        main(1)
        print("\n")


# Variables
lista_entrada = [1,2,3,4,5]
lista_entrada_validadas = []
Medicion_Empirica_bkt = []
Medicion_Analitica_bkt = []
Medicion_Empirica_fb = []
Medicion_Analitica_fb = []

# Realizar las Pruebas
for n in lista_entrada:
    board = create_puzzle(n)
    lista_resultados = []
    if board != False:
        lista_entrada_validadas.append(n)
        # FUERZA BRUTA
        start = timer()
        main(0)
        end = timer()
        time_emp_fb = (end-start)*1000000000
        # BACKTRACKING
        result,hist,time_emp_bkt,time_an = backtracking(board)

        # LISTAS A GRAFICAR
        Medicion_Empirica_fb.append(time_emp_fb)
        Medicion_Empirica_bkt.append(time_emp_bkt)
        Medicion_Analitica_bkt.append(time_an)
        


# Graficar
graficar(lista_entrada_validadas, Medicion_Empirica_fb, 'Mediciones Empiricas Fuerza Bruta', 'r')
graficar(lista_entrada_validadas, Medicion_Empirica_bkt, 'Mediciones Empiricas Backtracking', 'r')
graficar(lista_entrada_validadas, Medicion_Analitica_bkt, 'Mediciones Analiticas Backtracking', 'b')
