class Aluno(object):
    def __init__(self,nome,mensalidade=1000,idade=0):
    #def __init__(self, nome, mensalidade, idade):
        self.nome=nome
        self.mens=mensalidade
        self.age=idade
    def mostra_dados(self):
        dados= self.nome+ ' - ' + str(self.age) + ' - ' + str(self.mens)
        print(dados)
    def retorna_dados(self):
        dados = self.nome + ' - ' + str(self.age)
        return dados
    def pode_cnh(self):
        if self.age>=18:
            print("Pode possuir CNH")
        else:
            print("Não pode tirar CNH")
    def aumento(self):
        increase=float(input("Qual é o aumento na mensalidade?\n"))
        self.mens=+increase
        print(f"O reajuste foi de: {increase} R$\nAgora a mensalidade custa: {self.mens}")
    def get_nome(self):
        return self.nome
    def set_nome(self):
        self.nome=nome
    def mostra_dados2(self):
        print("Nome: ",self.get_nome())
        print("Idade: ", self.get_idade())
        print("Nome: ", self.get_mensalidade())
    def get_idade(self):
        return self.age
    def set_idade(self):
        self.age=idade
    def get_mensalidade(self):
        return self.mens
    def set_mensalidade(self):
        self.mens=mensalidade
    def aumenta_mensalidade_porc(self,pct):
        aumento=(self.mens(pct/100))+self.mens
        print(aumento)
        return aumento
if __name__ == '__main__':
    aluno1=Aluno('Kevelino',885,56)
    aluno2=Aluno('Paulo',850,18)
    aluno3=Aluno('Namae')
    aluno4=Aluno('Kiubi',720)
    aluno5=Aluno('Jucolomeu',idade=52)
    Aluno.mostra_dados(aluno1)
    #Aluno.pode_cnh(aluno2)