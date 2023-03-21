"""
O programa começa pedindo ao usuário para digitar um número inteiro, usando a função "input" do Python. Em seguida, o número é convertido em um inteiro usando a função "int".

O programa então verifica se o número é par ou ímpar usando o operador de módulo ("%"). Se o resultado da divisão por 2 for igual a zero, o número é par, e o programa imprime uma mensagem informando isso. Caso contrário, o número é ímpar, e o programa imprime outra mensagem.

Essa solução é simples e direta, seguindo a boas práticas de programação em Python, como usar nomes descritivos para as variáveis e comentar o código quando necessário.
"""

# Recebe o número inteiro como entrada do usuário
num = int(input("Digite um número inteiro: "))

# Verifica se o número é par ou ímpar
if num % 2 == 0:
    print("O número digitado é par.")
else:
    print("O número digitado é ímpar.")

