INF = 10**9

def floyd(M):
    n = len(M)-1   # a matriz M é (n+1)x(n+1)
    
    for k in range(1, n+1):  # matriz de 1 a n
        for i in range(1, n+1):  # linhas
            for j in range(1, n+1):  # colunas 
                custo_com_k = M[i][k] + M[k][j]
                custo_sem_k = M[i][j]
                if custo_com_k < custo_sem_k:
                    M[i][j] = custo_com_k
     

M = [None,
    [None, 0,   6,   2,   3],
    [None, INF, 0,   INF, 4],
    [None, 1,   2,   0,   INF],
    [None, 8,   INF, 7,   0]]

print(M)

print("\n\n\n")

floyd(M)

print(M)



         


