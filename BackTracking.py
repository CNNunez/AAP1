from Generator.dominoes import * 
from timeit import default_timer as timer
import matplotlib.pyplot as plt
from math import log
#######################################################################
##                      Solucion del proyecto
#######################################################################

"""
        A continuacion se presentan las funciones creadas para el desarrollo
        del proyecto.
"""

# Visualizacion de datos
def graficar(lista_n, lista_y, titulo, color):
    plt.plot(lista_n,lista_y,'-',linewidth=3,color=color)
    plt.grid()
    plt.xlabel('Tamaño de tablero (n)')
    plt.ylabel('Tiempo (s)')
    plt.title(titulo)
    plt.show()

# Algoritmo generar matriz vacia
def generarMatriz(tamano):
    a = -1
    filas = tamano + 1
    columnas = tamano + 2
    matriz = [[a for filas in range(columnas)] for filas in range(filas)]
    return matriz

# Funciones para el algoritmo de backtracking
def log(msg):
    #if debug:
    if False:
        print(msg)

def gen_pos(n, result, current):
    pos = random.randint(0,1)
    
    if pos==0:
        if current[1]+1 < n+2:
            if current[0]!=0:
                if result[current[0]-1][current[1]+1]!=1:
                    return pos
                else:
                    log("Horizontal blocked by vertical")
                    if current[0]<n:
                        return abs(pos-1)
                    else:
                        return -1
            else:
                return pos
        else:
            log("Horizontal out of bounds")
            if current[0]<n:
                return abs(pos-1)
            else:
                return -1
    else:
        if current[0]<n:
            return pos
        else:
            log("Vertical out of bounds")
            if current[1]+1 < n+2:
                if result[current[0]-1][current[1]+1]!=1:
                    return abs(pos-1)
                else:
                    return -1
            else:
                return -1
        
def update_current(n, result, prev_pos, current):  # Call at end of while, is recursive
    if prev_pos == 0:
        new_current = (current[0],current[1]+2)
    elif prev_pos == 1:
        new_current = (current[0],current[1]+1)
    else:
        new_current = (current[0],current[1])
    
    if new_current[0]<n+1:
        if new_current[1] < n+2:
            if new_current[0]!=0:
                if result[new_current[0]-1][new_current[1]]!=1:
                    return new_current
                else:
                    log("New current blocked by vertical")
                    return update_current(n, result, 1, new_current)
            else:
                return new_current
        else:
            log("New current out of bounds")
            return update_current(n, result, -1, (new_current[0]+1,0))
    else:
        log("End of board")
        return (-1,-1)
    
def get_domino(board, current, pos):
    if pos==0:
        return (board[current[0]][current[1]], board[current[0]][current[1]+1])
    else:
        return (board[current[0]][current[1]], board[current[0]+1][current[1]])
    
def domino_to_string(domino, invert=False):
    if invert:
        return f"{domino[1]}|{domino[0]}"
    return f"{domino[0]}|{domino[1]}"

def is_domino_valid(pieces, domino, pos):
    to_insert = domino_to_string(domino)
    inverted = domino_to_string(domino, True)
    current_pieces = pieces.keys()
    
    if (to_insert not in current_pieces) and (inverted not in current_pieces):
        pieces[to_insert] = pos
        return True
    else:
        return False
    
def is_pos_valid(n, result, current, pos):
    if pos==0:
        if current[1]+1 < n+2:
            if current[0]!=0:
                if result[current[0]-1][current[1]+1]!=1:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        if current[0]<n:
            return True
        else:
            if current[1]+1 < n+2:
                if result[current[0]-1][current[1]+1]!=1:
                    return True
                else:
                    return False
            else:
                return False
            

# Algoritmo de backtrscking
def backtracking(board):
    start = timer()
    n = len(board)-1
    result = generarMatriz(n)
    bt_times = generarMatriz(n)
    hist = []
    pieces = {}
    
    log(f"N: {n}\nData: {board}")
    latest_domino = None
    current = (0,0)
    not_at_end_of_board = True
    while not_at_end_of_board:
        log("__________________")
        pos = gen_pos(n, result, current)
        log(f"Pieces: {pieces}\nHist: {hist}\nResult: {result}\nBT_times: {bt_times}\nCurrent: {current}\nPos: {pos}\nLatest inserted domino: {latest_domino}")
        
        if pos != -1:
            domino = get_domino(board, current, pos)
        else:
            domino = latest_domino
        trying_to_add_domino = True
        while trying_to_add_domino:
            if (is_domino_valid(pieces, domino, pos) == False):
                log("--------------BACKTRACKING----------------")
                
                validating_pos = True
                while validating_pos and hist!=[]:
                    current = hist.pop()
                    old_pos = result[current[0]][current[1]]
                    result[current[0]][current[1]] = -1
                    del pieces[domino_to_string(get_domino(board, current, old_pos))]
                    pos = abs(old_pos-1)
                    log(f"$$$Hist: {hist}\nResult: {result}\nBT_times: {bt_times}\nCurrent: {current}\nInverted Pos: {pos}\nPieces: {pieces}")
                    if is_pos_valid(n, result, current,pos):
                        if bt_times[current[0]][current[1]] < 1:
                            validating_pos = False
                        
                    if validating_pos:
                        bt_times[current[0]][current[1]] = -1
                
                domino = get_domino(board, current, pos)
            else:
                latest_domino = domino
                hist.append(current)
                result[current[0]][current[1]] = pos
                bt_times[current[0]][current[1]] += 1
                trying_to_add_domino = False
            
        current = update_current(n, result, pos, current)
        if current == (-1,-1):
            not_at_end_of_board = False
    end = timer()
    time_emp = (end-start)*1000000000
    time_an = ec_analitica_bac(n)
    return result,hist,time_emp,time_an

# ecuacion de medicion analitica del back tracking
def ec_analitica_bac(n):
    time = n*3
    return time


#######################################################################
##                              MAIN
#######################################################################

# PARA MODO DEBUG
debug = False   # Set True para ver prints de proceso,
                # puzzle más de 4 puede crashear por el volumen de prints

"""
# Variables
lista_entrada = [1,2,4,2,5,3,4,1,3,5,4,5,5,2]
Medicion_Empirica = []
Medicion_Analitica = []

# Realizar las Pruebas
for n in lista_entrada:
    board = create_puzzle(n)
    lista_resultados = []
    if board != False:
        result,hist,time_emp,time_an = backtracking(board)
        Medicion_Empirica.append(time_emp)
        Medicion_Analitica.append(time_an)
        for coord in hist:
            lista_resultados.append(result[coord[0]][coord[1]])
        print(lista_resultados)


# Imprimir resultados
print("Los resultados obtenidos de las mediciones: ")
print('- Empirico: ',Medicion_Empirica)
print('- Analitico: ',Medicion_Analitica)


# Graficar
#graficar(lista_entrada, Medicion_Empirica, 'Medicion Empirica Mediciones Empiricas', 'r')
#graficar(lista_entrada, Medicion_Analitica, 'Medicion Empirica Mediciones Analiticas', 'b')

"""