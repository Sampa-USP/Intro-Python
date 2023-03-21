"""
O programa começa importando a biblioteca NumPy para realizar os cálculos. Em seguida, pede ao usuário para digitar uma lista de números inteiros, separados por espaço, usando a função input() do Python. Essa lista é convertida em uma lista de inteiros usando uma compreensão de lista e o método split() para separar os números.

Depois, a biblioteca NumPy é usada para calcular a média e o desvio padrão da lista de números usando as funções mean() e std(). Os resultados são armazenados nas variáveis media e desvio_padrao.

Finalmente, o programa imprime os resultados na tela usando a função print().
"""

import numpy as np

# Recebe uma lista de números inteiros do usuário
numeros = input("Digite uma lista de números inteiros separados por espaço: ")
numeros = [int(numero) for numero in numeros.split()]

# Usa a biblioteca NumPy para calcular a média e o desvio padrão dos números
media = np.mean(numeros)
desvio_padrao = np.std(numeros)

# Imprime os resultados
print("A média dos números é:", media)
print("O desvio padrão dos números é:", desvio_padrao)

