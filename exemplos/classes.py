"""
A classe "ContaBancaria" tem dois atributos, "saldo" e "titular", que são definidos no método construtor "init". O método "depositar" adiciona uma quantia ao saldo da conta e imprime uma mensagem informando sobre o depósito realizado. O método "sacar" remove uma quantia do saldo da conta, desde que o saldo seja suficiente, e imprime uma mensagem informando sobre o saque realizado ou a falta de saldo. O método "consultar_saldo" imprime uma mensagem com o saldo atual da conta. Para criar uma nova conta, basta criar um objeto da classe "ContaBancaria" passando o nome do titular e o saldo inicial (opcional) como parâmetros:
"""

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado na conta de {self.titular}.")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado na conta de {self.titular}.")
        else:
            print(f"Saldo insuficiente na conta de {self.titular}.")

    def consultar_saldo(self):
        print(f"O saldo atual da conta de {self.titular} é R${self.saldo}.")

#USO :
#conta1 = ContaBancaria("João", 1000)
#conta1.depositar(500)
#conta1.sacar(200)
#conta1.consultar_saldo()

