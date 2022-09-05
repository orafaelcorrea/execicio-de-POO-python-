
class Investimento:
    nome = None
    numero = None
    saldo = None
    taxjur = None

    def __init__(self, nome, num, saldo, tax):
        self.nome = nome
        self.num = num
        self.saldo = saldo
        self.tax = tax
       
    def saldo(self):
        return self.saldo

    def addjur(self):
        self.saldo +=(self.taxjur / 100 * self.saldo)
        return "o novo valor é {:.2F}".format (self.saldo)
    nome = input("Nome :").upper()
    num = input("Conta :")
    saldo = float(input("Informe seu saldo em R$ :"))
    tax = float(input("Informe a taxa de juros :"))        