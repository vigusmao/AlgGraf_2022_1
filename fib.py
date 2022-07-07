from time import time 

memo = {}   # hash map (chave-->valor)
            # chave: n   valor: fib(n) 


def fib(n):
    # verifica se ja foi calculado antes 
    result_from_memo = memo.get(n)
    if result_from_memo is not None:
        return result_from_memo

    
    if n <= 1:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)

    # agora que paguei caro pelo resultado, 
    # vou armazena-lo no memo para uso futuro
    memo[n] = result

    return result



while True:
    n = input("Digite um inteiro: ")
    if n < 0:
        break;

    inicio = time()
    print("fib(%d) = %d" % (n, fib(n)))
    duracao = time() - inicio
    print("duracao = %.3f" % duracao)
     







