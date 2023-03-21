"""
Escreva um programa que solicite as notas de um aluno em três provas, calcule a média e informe se o aluno foi aprovado ou reprovado. Considere que a média para aprovação é 7.
"""



# Solicita as notas das três provas
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

# Calcula a média das três notas
media = (nota1 + nota2 + nota3) / 3

# Verifica se o aluno foi aprovado ou reprovado
if media >= 7:
    print("Parabéns, você foi aprovado com média", media)
else:
    print("Infelizmente você foi reprovado com média", media)
