#criar uma classe bombaCombustivel
class Bomba: 
#na classe tipo de combustivel, valorLitro, quantidadeCombustivel 
    def __init__(self, capacidade, preco):
        self.capacidade = capacidade
        self.preco = preco   
#ter o metodo abastecerPorValor()
    def porValor(self,valor):
        litros = valor / self.preco
        self.capacidade = self.capacidade - litros
        return litros
#ter o metodo abastecerPorLitro()
    def porLitro(self, litros):
        valor = litros * self.preco
        self.capacidade = self.capacidade - litros
        return valor
#ter o metodo alterarValor()
    def alterarPreco(self, preco):
        self.preco = preco
#ter o metodo alterarQuantidadeCombustivel() 
    def encherBomba(self, litros):
        self.capacidade = self.capacidade + litros

bomba = Bomba(2000, 5.45)
print ("Abasteceu %f litros" % bomba.porValor(100))
print ("Abasteceu %f reais" % bomba.porLitro(100))
bomba.alterarPreco(2.55)
print ("Abasteceu %f reais" % bomba.porLitro(100),bomba.encherBomba(100))
print ("Capacidade: %f litros" % bomba.capacidade)

