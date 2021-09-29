
"""
 Algoritmo que revisa todas las posibles soluciones para completar el tablero
"""
def fuerza_bruta(board,tiles,solut):
    buscar = [] #Ficha que va buscar y verficar

    #Condiciones de parada basicas
    #1 todas las soluciones hechas y ya no hay fichas 
    if solut == [] and tiles == []:
        return True
    #2 Solucion invalida
    elif solut == [] and tiles!=[]:
        return False
    #Recorrer toda la matriz
    else:
        for i in range(len(board)):
            for j in range(len(board[i])):

                #Podas
                if board[i][j] != -1:
                    
                    #Pruebas de posiciones, se utilizara valores binarios 0 = horizontal / 1 = vertical
                    if(solut[0] == 0):
                        #Para quitar validaciones de bordes utilizamos un try
                        try:
                            buscar.append(board[i][j])
                            buscar.append(board[i][j+1])

                            #Saber que no tengo que volver a pasar por ahí
                            board[i][j] = -1
                            board[i][j+1] = -1
                        
        
                        except IndexError:
                            return False

                    #Repetir proceso para la funcion en vertical
                    elif(solut[0] == 1):
                        #Para quitar validaciones de bordes utilizamos un try
                        try:
                            buscar.append(board[i][j])
                            buscar.append(board[i+1][j])

                            #Saber que no tengo que volver a pasar por ahí
                            board[i][j] = -1
                            board[i+1][j] = -1
                        
                        except IndexError:
                            return False    

                    if(isIn(buscar,tiles)):

                        try:
                            tiles.remove(buscar)
                        except:
                            buscar[0],buscar[1] = buscar[1],buscar[0]
                            tiles.remove(buscar)

                        return fuerza_bruta(board,tiles,solut[1:]) 
                    
                    else:
                        return False


#Tenemos que confirmar que la ficha esta entre todas las fichas posibles
#Tanto al derecho, como a la inversa
def isIn(ficha,Tfichas):
    if(ficha in Tfichas):
        return True
    else:
        #Se voltea la ficha para volver a verificar
        ficha[0],ficha[1] = ficha[1],ficha[0]
        if(ficha in Tfichas):
            return True
        else:
            return False