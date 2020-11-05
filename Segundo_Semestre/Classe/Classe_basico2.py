class Veiculo(object):
    def __init__(self,nome,ano,valor):
        self.nome=nome
        self.ano=ano
        self.valor=valor
    def get_nome(self):
        return self.nome
    def get_valor(self):
        return self.valor
    def get_valor(self):
        return self.ano
    def set_nome(self,nome):
        if nome=="":
            print("Nada digitado\nTente novamente")
        else:
            self.nome=nome
    def set_valor(self,valor):
        if valor>0:
            self.valor = valor
        else:
            print("Valor inválido")
    def set_ano(self,ano):
        if ano<1900:
            print("Valor inválido digitado")
        else:
            self.ano=ano
    def mostra_dados(self):
        info=str(self.nome)+ " - " +str(self.ano)+ " - R$" +str(self.valor)
        print(info)
    def retorna_dados(self):
        return self.nome,self.ano,self.valor
    def aumenta_valor(self):
        aumento=float(input("Insira o valor do aumento: "))
        final=self.valor+aumento
        return final
    def compara_valor(self, carro):
        if self.valor > carro.valor:
            return self.valor
        elif carro.valor > self.valor:
            return carro.valor
        else:
            return 'Possuem o mesmo valor'
if __name__ == '__main__':
    veiculo1=Veiculo('Civic',2019,50000)
    veiculo2=Veiculo('Corolla',2018,48000)
    print(Veiculo.mostra_dados(veiculo1))
    print(veiculo1.compara_valor(veiculo2))