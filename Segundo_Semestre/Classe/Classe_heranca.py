class Funcionario(object):
    def __init__(self,nome,cpf,salario=0):
        self.nome=nome
        self.cpf=cpf
        self.salario=salario
    def __str__(self):
        s=f"Nome: {self.nome}, CPF: {str(self.cpf)}, Salario: {str(self.salario)}"
        return s
    def get_nome(self):
        return self.nome
    def get_cpf(self):
        return self.cpf
    def get_salario(self):
        return self.salario
    def set_nome(self,name):
        self.nome=name
    def set_cpf(self,novo):
        self.cpf=novo
    def set_salario(self,novo):
        self.salario=novo
    def bonificacao(self):
        bon=(self.salario*0.1)
        return bon
    def salario_total(self):
        total=self.salario+Funcionario.bonificacao(self)
        return total
    def salario_total2(self):
        b=self.bonificacao()
        if isinstance(self,Gerente):
            total=self.salario+b+500
        elif isinstance(self, Funcionario):
            total=self.salario+self.bonificacao()
        return total
class Gerente(Funcionario):
    def __init__(self,nome,cpf,senha,qtd_gerencia=0,salario=0):
        super().__init__(nome,cpf,salario)
        self.senha=senha
        self.qtd=qtd_gerencia
        self.salario+=500
    def __str__(self):
        s1=super().__str__()
        s=s1 + ", Qtd.: {}" .format(self.qtd)
        return s
    def autentica(self,senha):
        if senha==self.senha:
            print("Acesso permitido")
            return True
        else:
            print("Acesso Negado")
            return False
if __name__ == '__main__':
    '''
    Formas de inserção de dados:
    Funcionário -> nome,cpf,salario
    Gerente -> nome,cpf,senha,qtd_gerencia,salario
    '''
    f1=Funcionario("Jorge Pereira Almeida",15678467469,4700)
    g1=Gerente("Carlos Batista Ramos", 74589612345,144597, 20, 7800)
    print(Funcionario.__str__(f1))
    Gerente.autentica(g1,784126)
    g2=Gerente("Vasconcelos Ribeiro", 44468456157, 784126, 20,7800)
    g3=Gerente("Heliton Fabrício Jurandir", 78945612347, 471356, 25, 8300)
    print(Funcionario.get_salario(f1))
    print(Gerente.get_salario(g1))
    print(vars(g1))
    print(Gerente.salario_total(g3))