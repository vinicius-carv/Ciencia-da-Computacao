class ContaCorrente(object):
    num_conta=0
    @classmethod
    def num_contas(cls):
        print(f"{cls.num_conta} contas registradas no sistema")
    def __init__(self,titular,numero="000-0",saldo=0):
        ContaCorrente.num_conta+=1
        self.nome=titular
        self.num=numero
        self.saldo=saldo
    def __str__(self):
        s=self.nome + " - " + str(self.num) + " - " + str(saldo)
        return s
    def get_titular(self):
        return self.nome
    def get_num(self):
        return self.num
    def get_saldo(self):
        return self.saldo
    def set_titular(self,name):
        if isinstance(nome,str):
            self.nome=name
        else:
            print("Valor inválido inserido")
    def set_numero(self,numero):
        self.num=numero
    def deposito(self,dep):
        if dep>0:
            self.saldo+=dep
        else:
            return ValueError
    def retirada(self,ret):
        print("Taxa de transferência de R$5")
        if ret>=saldo:
            self.saldo-=ret
            return True
        else:
            print("Saldo insuficiente")
            return False
    def transfere(self,beneficente):
        tra=float(input("Digite o valor da transferência: "))
        if tra>self.saldo:
            print("Saldo insuficiente")
        else:
            self.saldo-=tra-5
            beneficente.saldo+=tra
            d=input(f"Transferência realizada por {self.nome} para {beneficente.nome} no valor de R${tra}\nSr.{self.nome} deseja ver o seu novo saldo?\nSim ou Não\n").upper()
            if d=="SIM":
                print(f"Seu saldo é: R${self.saldo}")
            elif d=="NAO" or d=="NÃO":
                print("Finalizado")
            else:
                print("Opção inválida")
if __name__ == '__main__':
    conta1=ContaCorrente("João","123-4",1000)
    print(ContaCorrente.get_titular(conta1))
    ContaCorrente.set_numero(conta1,"923-4")
    ContaCorrente.deposito(conta1,1000)
    print(ContaCorrente.get_saldo(conta1))
    name=input("Digite o nome do cliente: ")
    conta=input("Digite a conta do usuário: ")
    saldo=float(input("Digite o saldo do cliente: "))
    conta2=ContaCorrente(name,conta,saldo)
    conta3=ContaCorrente("Nagflar",saldo=4200)
    ContaCorrente.transfere(conta3,conta2)
    print(ContaCorrente.get_saldo(conta2))
    ContaCorrente.num_contas()