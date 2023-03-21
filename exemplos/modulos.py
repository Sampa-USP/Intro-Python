"""
O código acima define um módulo chamado "fatorial.py". Esse módulo contém uma única função chamada "calcular_fatorial" que recebe um número como argumento e retorna o fatorial desse número. O fatorial de um número é o produto de todos os números inteiros de 1 até o número em questão. Por exemplo, o fatorial de 5 é 5 * 4 * 3 * 2 * 1 = 120.

A função "calcular_fatorial" implementa o cálculo do fatorial de forma recursiva. Se o número fornecido for igual a zero, a função retorna 1. Caso contrário, a função chama a si mesma passando como argumento o número decrementado em uma unidade e multiplica o resultado pelo número original. Esse processo se repete até que o número fornecido seja igual a zero.

Para utilizar o módulo "fatorial.py", basta importá-lo em outro script Python usando a instrução "import fatorial" e chamar a função "calcular_fatorial" passando o número desejado como argumento.
"""

# Criando o módulo fatorial.py

def calcular_fatorial(numero):
    """
    Função que calcula o fatorial de um número.

    Args:
        numero (int): Número para calcular o fatorial.

    Returns:
        int: Fatorial do número fornecido.
    """
    if numero == 0:
        return 1
    else:
        return numero * calcular_fatorial(numero - 1)
