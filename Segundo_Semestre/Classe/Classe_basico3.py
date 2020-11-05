import datetime
class Pessoa(object):
    default=datetime.date(2000,1,1)
    def __init__(self,name,birth=default):
        self.name=name
        self.birth=birth
    def get_name(self):
        return self.name
    def get_birth(self):
        return self.birth
    def set_name(self,change):
        self.name=change
    def set_birth(self,new):
        self.birth=new
    def __str__(self):
        p=str(self.name) + " " + str(self.birth)
        return p
    def calcula_idade(self):
        atual = datetime.datetime.now().date()
        idade= atual.year-self.birth.year
        if atual.month<self.birth.month:
            return idade-1
        elif atual.month==self.birth.month:
            if atual.day<self.birth.day:
                return idade-1
            else:
                return idade
        else:
            return idade
    def mais_velho(self,pessoa):
        if self.calcula_idade()>pessoa.calcula_idade():
            print("A idade maior é de: ",self.calcula_idade())
        elif pessoa.calcula_idade()==self.calcula_idade():
            print("As idades são iguais")
        else:
            print("A idade maior é de: ",pessoa.calcula_idade)
if __name__ == '__main__':
    birth_date=datetime.date(1993,12,13)
    cliente=Pessoa("Carlos Pereira",birth_date)
    birth_date1=datetime.date(2000, 11, 23)
    cliente1=Pessoa("Maria Souza",birth_date1)
    birth_date2=datetime.date(1985, 12, 13)
    cliente.set_birth(birth_date2)
    '''print(Pessoa.get_birth(cliente))
    print(Pessoa.__str__(cliente))
    print(Pessoa.calcula_idade(cliente))'''
    print(Pessoa.mais_velho(cliente,cliente1))