import sys
from random import randint

VALOR = 0
PESO = 1

memo = {}


# ENTRADA
# itens: lista de n pares (v_i, w_i),
#        onde v_i eh o valor e w_i eh o peso
#        do i-esimo elemento;
#        e um inteiro W, o peso maximo suportado
#
# SAIDA
# o valor da mochila otima,
# i.e., aquela que otimiza o somatorio dos itens
# nela contidos sem estourar a capacidade maxima
# da mochila
def mochila(itens, W):
    memo.clear()
    N = len(itens)
    sys.setrecursionlimit(N+10)         
    return m(itens, W, N)


def m(itens, w, n):
    if n == 0:
        return 0
    if w == 0:
        return 0
    
    result_from_memo = memo.get((w,n))
    if result_from_memo is not None:
        return result_from_memo

    valor = itens[n-1][VALOR]
    peso = itens[n-1][PESO]

    valor_com_ultimo = \
        valor + m(itens, w-peso, n-1) if peso <= w \
        else 0
    valor_sem_ultimo = m(itens, w, n-1)

    result = max(valor_com_ultimo, valor_sem_ultimo)

    memo[(w,n)] = result
    return result

def criar_mochila(n):
    mochila = []
    for i in range(n):
        peso = randint(1,9)
        valor = randint(1,100)
        mochila.append((valor, peso))
    return mochila


while True:
    tamanho = int(input("Tamanho: "))
    itens = criar_mochila(tamanho)
    W = 3*tamanho
    print(itens)
    print("W=%d" % W)
    resultado = mochila(itens, W)
    print("Mochila otima tem valor %d" % resultado)
    print("\n\n")




    



