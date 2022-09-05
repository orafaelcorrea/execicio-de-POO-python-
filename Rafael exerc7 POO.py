
class Investimento:
    
    def __init__(self, nome, num, saldo, tax, total):
        self.nome = nome
        self.num = num
        self.saldo = saldo
        self.tax = tax
        self.total = total
       
    def saldo(self):
        return self.saldo

    def addjur(self):
        self.saldo +=(self.taxjur / 100 * self.saldo)
        return "o novo valor é {:.2F}".format (self.saldo)
    nome = input("Nome :").upper()
    num = input("Conta :")
    saldo = float(input("Informe seu saldo em R$ :"))
    tax = float(input("Informe a taxa de juros :"))        
    total = (saldo + tax)
    print(total)