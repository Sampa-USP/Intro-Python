"""
A função "soma_lista" recebe uma lista de números inteiros como argumento e retorna a soma desses números. O primeiro passo é criar uma variável "soma" e inicializá-la com o valor 0. Em seguida, usamos um loop "for" para percorrer todos os elementos da lista, somando cada um deles à variável "soma". Finalmente, a função retorna o valor de "soma".

Para testar a função, criamos uma lista de números inteiros chamada "minha_lista" e a passamos como argumento para a função "soma_lista". Em seguida, imprimimos o resultado da função usando a função "print". O resultado deve ser a soma de todos os números da lista, neste caso, 15 (1 + 2 + 3 + 4 + 5).
"""

def soma_lista(lista):
    """
    Esta função recebe uma lista de números inteiros e retorna a soma desses números.
    """
    soma = 0
    for numero in lista:
        soma += numero
    return soma

# Exemplo de uso da função
minha_lista = [1, 2, 3, 4, 5]
resultado = soma_lista(minha_lista)
print(resultado)

