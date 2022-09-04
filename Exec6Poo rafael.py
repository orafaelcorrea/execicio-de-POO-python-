#criar um classe para interpretar uma conta corrente
#atributos: número da conta, nome do correntista e saldo
class ContaCorrente:
    def __init__(self, correntista, nConta, saldo):
        self.correntista = correntista
        self.nConta = int(nConta)
        self.saldo = float(saldo)
#ter o metodo alterarNome()
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
        return self.nome 
#ter o metodo deposito e saque
    def deposito(self, vDeposito):
        self.saldo += vDeposito
        return self.saldo

    def saque(self, vSaque):
        self.saldo += vSaque
        return self.saldo
            
CC = ContaCorrente (1000 , 'Rafael dos Santos')