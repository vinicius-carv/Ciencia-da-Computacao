'''
Aluno: Vinícius Alves de Carvalho
RA: 22000691
1. Implemente a função maximo que recebe três números e retorna o maior deles. A função principal
(main) lê três números, chama a função maximo passando os três argumentos (os valores lidos) e gera a tela de
saída com o valor retornado pela função maximo.
'''
def maxi(num1,num2,num3): # Função recebendo 3 números para a comparação
    if max(num1,num2,num3)==num1:
        return num1
    elif max(num1,num2,num3)==num2:
        return num2
    elif max(num1,num2,num3)==num3:
        return num3
if __name__ == '__main__':
    num1=float(input("Digite um número:\t"))
    num2=float(input("Digite um número:\t"))
    num3=float(input("Digite um número:\t"))
    print(maxi(num1,num2,num3))
'''
2. Desenvolva o programa que leia vários números, armazene-os numa lista e mostre estas informações:
a- Leia um valor e verifique se ele está na lista. Se estiver, mostre também a posição (índice) do valor encontrado
na pesquisa;
b- Mostre a lista na ordem crescente.
c- Insira (acrescente) o valor 33 na posição (índice) 1 da lista.
d- Mostre a lista na ordem decrescente.
e- Média dos valores da lista;
f- Porcentagem dos números maiores que dez na lista.
g- Elabore o enunciado e a implementação de mais uma questão na lista criada. A complexidade do enunciado e da
implementação da questão serão considerados para mensurar a avaliação da questão.
'''
if __name__ == '__main__':
    lista=[]
    maidez=[] #Lista para armazenar os números maiores que dez
    par=[] #Lista para armazenar os números pares
    impar=[] #Lista para armazenar os números ímpares
    i=0
    while True:
        num=float(input("Digite um número (Insira -0 para sair):\n"))#Colocada uma condição fora do real para quebrar o laço de repetição e não limitar as possibilidades de entrada
        if num==-0:
            lista.sort()#Organizando em ordem crescente
            lista.insert(1,33)#Como solicitado na letra c
            print("Lista na ordem crescente\n")
            for i in range(len(lista)):
                print(lista[i]," ")
            lista.sort(reverse=True)
            print("Lista na ordem decrescente\n")
            for i in range(len(lista)):
                print(lista[i], " ")
            print(f"Média: {sum(lista)/len(lista)}")
            for i in range(len(lista)):
                if lista[i]>10:
                    maidez.append(lista[i])
            por=(len(maidez)/len(lista))*100 #Variável que vai armazenar os números maiores que 10
            print(f"A porcentagem de números maiores que dez é: {por}%")
            for i in range(len(lista)):
                if lista[i]%2==0:
                    par.append(lista[i])
                else:
                    impar.append(lista[i])
            porp=(len(par)/len(lista))*100 #Variável que vai armazenar os números pares
            print(f"A porcentagem de pares é: {porp}%")
            pori=(len(impar)/len(lista))*100  # Variável que vai armazenar os números ímpares
            print(f"A porcentagem de ímpares é: {pori}%")
            break
        else:
            lista.append(num)
            print(f"Valor {num} armazenado na lista")
            if num in lista:
                pos=lista.index(num)
                print(f"O número {num} foi encontrado na posição {pos+1}\n")#Adicionando um número a mais no índice para entendimento do usuário
'''
3. Crie a classe Livro com os atributos título, autor, páginas e preço. Crie o método construtor que além do
parâmetro self recebe mais quatro parâmetros que serão atribuídos aos respectivos atributos da classe Livro. O
parâmetro preço do construtor deve ter o valor default.
Crie o método get_autor e o método set_preco, para consultar o autor e alterar o preço do livro. Crie o método
funcional porcentagem para o aumento preço com o objetivo de atualizar o preço do livro. Esse método recebe o
valor do aumento e atualiza o atributo preco. Crie também o método funcional retorna dados, ele concatena três
atributos da classe e retorna a variável concatenada.

No método main, instancie três objetos dessa classe. Crie o primeiro objeto passando quatro argumentos, o segun-
do objeto passando apenas o título e páginas e crie o terceiro objeto livro passando apenas título e preço. Use e
teste todos os método criados na classe Livro para um dos objetos criados.
Elabore o enunciado e a implementação de mais um método funcional na classe Livro, esse método deve receber
dois objetos. A complexidade do enunciado e da implementação do método serão considerados para mensurar a
avaliação do método.
'''
class Livro:
    def __init__(self,tit,aut="",pag=10,preco=10):
        self.tit=tit
        self.aut=aut
        self.pag=pag
        self.preco=preco
    def get_autor(self):
        return self.aut
    def set_preco(self,preconovo):
        self.preco=preconovo
    def aumento_porcentagem(self,porcento):
        self.preco=(self.preco*(porcento/100))+self.preco
    def get_preco(self):
        return self.preco
    def retorna_dados(self):
        dados = self.tit + ' - ' + self.aut + ' - ' + str(self.preco)
        return dados
    def compara_preco(self,livro):
        if self.preco > livro.get_preco():
            return self.preco
        elif livro.get_preco()>self.preco:
            return livro.get_preco()
        else:
            return "Eles possuem o mesmo valor"
if __name__ == '__main__':
    livro1=Livro("O Corvo","Edgar Allan Poe",4,15)
    livro2=Livro("Alto da Compadecida",pag=265)
    livro3=Livro("O Ateneu",preco=56)
    Livro.get_autor(livro1)
    Livro.aumento_porcentagem(livro3,20)
    Livro.set_preco(livro2,45)
    print(Livro.retorna_dados(livro1))
    print(Livro.compara_preco(livro3,livro1))