"""
O programa começa solicitando ao usuário que digite dois números inteiros. Em seguida, ele verifica se o primeiro número é divisível pelo segundo número usando o operador de módulo "%". Se o resto da divisão do primeiro número pelo segundo número for zero, isso significa que o primeiro número é divisível pelo segundo número, e o programa imprime "Divisível". Caso contrário, o programa imprime "Não divisível".
"""

# Recebe dois números inteiros do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Verifica se o primeiro número é divisível pelo segundo número
if num1 % num2 == 0:
    # Imprime "Divisível" se o primeiro número for divisível pelo segundo número
    print("Divisível")
else:
    # Imprime "Não divisível" se o primeiro número não for divisível pelo segundo número
    print("Não divisível")
