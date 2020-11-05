from datetime import date
data_atual=date.today()
dia=data_atual.day
mes=data_atual.month
ano=data_atual.year
name=input("Digite o seu nome:\n")
dia_in=int(input("Digite o dia do seu nascimento:\n"))
mes_in=int(input("Digite o mês do seu nascimento:\n(Número)\n"))
ano_in=int(input("Digite o ano do seu nascimento:\n"))
if ano_in>ano or dia_in>31 or dia_in<1 or mes_in>12 or mes_in<1:
    print("Data inválida")
elif mes_in>mes:
    idade=ano-ano_in-1
    print(f"{name},Hoje: {dia}/{mes}/{ano}\nVocê tem {idade} anos")
elif mes_in==mes and dia_in>dia:
    idade=ano-ano_in-1
    print(f"{name},Hoje: {dia}/{mes}/{ano}\nVocê tem {idade} anos")
else:
    idade=ano-ano_in
    print(f"{name},Hoje: {dia}/{mes}/{ano}\nVocê tem {idade} anos")