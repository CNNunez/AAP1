def arreglo_binario(A, n):
    if n==0:
        print(A)
    else:
        A[n-1] = 0
        arreglo_binario(A, n-1)
        A[n-1] = 1
        arreglo_binario(A, n-1)

#arreglo_binario([0,0],2)


def arreglo_k_ario(A, n):
    if n==0:
        print(A)
    else:
        for i in range (0,4):
            if i != 2:
                A[n-1] = i
                arreglo_k_ario(A, n-1)

#arreglo_k_ario([0,0],2)

def mochila(A, m, L):
    if (m == 0):
        if (L == 0):
            print (A)
    else:
        A[m] = False
        mochila(A, m-1, L)
        if (segmentos[m] <= L):
            A[m] = True
            mochila(A, m-1, L-segmentos[m])

#mochila( [1, 2, 2, 4, 5, 2, 4] , 6 ,15)