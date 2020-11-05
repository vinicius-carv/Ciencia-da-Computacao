class Produto(object):
    def __init__(self,nome,vlr_compra=10,vlr_venda=10,qtd_estoque=100,qtd_min=100):
        self.nome=nome
        self.compra=vlr_compra
        self.venda=vlr_venda
        self.estoque=qtd_estoque
        self.min=qtd_min
    def __str__(self):
        s=str(self.nome)+str(self.compra)+str(self.venda)+str(self.estoque)+str(self.min)
        return s
    def get_name(self):
        return self.nome
    def get_vlr_compra(self):
        return self.compra
    def get_qtd_min(self):
        return self.min
    def set_name(self,nome):
        self.nome=nome
    def set_vlr_compra(self,compra):
        self.compra=compra
    def set_qtd_min(self,minima):
        self.min=minima
    def lucro(self):
        lucro=self.venda-self.compra
        return lucro
    def atualiza_qtd(self,qtd):
        self.estoque-=qtd
    def alerta_compra(self):
        if self.estoque<self.min:
            return False
        else:
            return True
    def repor_produto(self,novo):
        self.estoque+=novo
    def maior_qtd(self,prod1):
        if self.estoque > prod1.estoque:
            print(f"Há mais {self.estoque} do que {prod1.estoque}")
        elif self.estoque==prod1.estoque:
            print("Ambos estão na mesma quantidade")
        else:
            print(f"Há mais {prod1.estoque} do que {self.estoque}")
    def maior_lucro(self,prod1):
        if (self.compra-self.venda) > (prod1.compra-prod1.venda):
            print(f"{self.nome} é mais lucrativo do que {prod1.nome}")
        elif (self.compra-self.venda)==(prod1.compra-prod1.venda):
            print("Ambos dão o mesmo lucro")
        else:
            print(f"{prod1.nome} é mais lucrativo do que {self.nome}")
if __name__ == '__main__':
    arroz=Produto("Arroz",15.00,19.50,67,20)
    Produto.set_qtd_min(arroz,15)
    name1=input("Digite o nome do produto: ")
    prod1=Produto(name1)
    prod2=Produto("Pimentão",qtd_estoque=20)
    print(Produto.get_qtd_min(arroz))