INF = 10**9

CUSTO = 0
PRED = 1

def floyd(M):
    n = len(M)-1   # a matriz M é (n+1)x(n+1)
    
    for k in range(1, n+1):  # matriz de 1 a n
        for i in range(1, n+1):  # linhas
            for j in range(1, n+1):  # colunas 

                custo_com_k = M[i][k][CUSTO] + \
                              M[k][j][CUSTO]
                custo_sem_k = M[i][j][CUSTO]

                if custo_com_k < custo_sem_k:
                    M[i][j][PRED] = M[k][j][PRED]
                    M[i][j][CUSTO] = custo_com_k
     
def imprimir(matriz):
    for i in range(len(matriz)):
        print(matriz[i])



M = [  None,
    [None, [0,1],     [6,1], [2,1],     [3,1]],
    [None, [INF,None],[0,2], [INF,None],[4,2]],
    [None, [1,3],     [2,3], [0,3],     [INF,None]],
    [None, [8,4],  [INF,None],[7,4],    [0,4]]]

imprimir(M)

print("\n\n\n")

floyd(M)

imprimir(M)



         


