from random import randint
from time import time

INF = 10**9

memo ={}


def imprimir(matriz):
    for i in range(1, len(matriz)):
        print(matriz[i][1:])

def criar_matriz_quadrada(tamanho):
    matriz = []
    for i in range(tamanho):
        matriz.append([None] * tamanho)
    return matriz

def criar_grafo_aleatorio(n):
    matriz = criar_matriz_quadrada(n+1)
    for i in range(1, n+1):
        matriz[i][i] = 0
        for j in range(1, n+1):
            if i==j:
                continue
            matriz[i][j] = randint(1,9)
    return matriz

def floyd(M):
    memo.clear()

    n = len(M)-1   # a matriz M é (n+1)x(n+1)

    resultado = criar_matriz_quadrada(n+1)

    for i in range(1, n+1):
        for j in range(1, n+1):
            resultado[i][j] = \
                floyd_recursivo(M, i, j, n)

    return resultado


def floyd_recursivo(M, i, j, k):
    result_from_memo = memo.get((i, j, k))
    if result_from_memo is not None:
        return result_from_memo

    if k == 0:
        return M[i][j]

    custo_i_k = floyd_recursivo(M, i, k, k-1)
    custo_k_j = floyd_recursivo(M, k, j, k-1)

    custo_com_k = custo_i_k + custo_k_j
    custo_sem_k = floyd_recursivo(M, i, j, k-1)

    result = min(custo_com_k, custo_sem_k)

    # memo[(i, j, k)] = result 
    return result

def floyd_bottom_up(M):  # P.D. bottom-up (classica)
    n = len(M)-1   # a matriz M é (n+1)x(n+1)
    
    for k in range(1, n+1):  # matriz de 1 a n
        for i in range(1, n+1):  # linhas
            for j in range(1, n+1):  # colunas 
                custo_com_k = M[i][k] + M[k][j]
                custo_sem_k = M[i][j]
                if custo_com_k < custo_sem_k:
                    M[i][j] = custo_com_k
     

#M = [None,
#    [None, 0,   6,   2,   3],
#    [None, INF, 0,   INF, 4],
#    [None, 1,   2,   0,   INF],
#    [None, 8,   INF, 7,   0]]

while True:
    n = int(input("Quantos vertices? "))
    if n <= 0:
        break

    M = criar_grafo_aleatorio(n)

    imprimir(M)

    print("\nTOP-DOWN\n")
    inicio = time()
    topdown_results = floyd(M)
    duracao = time() - inicio 
    imprimir(topdown_results)
    print("\nduracao = %.3f segundos" % duracao)
    
    print("\nBOTTOM-UP\n")
    inicio = time()
    floyd_bottom_up(M)
    duracao = time() - inicio 
    imprimir(M)
    print("\nduracao = %.3f segundos" % duracao) 
    print("\n\n\n")








         


