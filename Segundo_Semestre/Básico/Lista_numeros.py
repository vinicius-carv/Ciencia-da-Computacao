lista=[]
num10=[]
count=0
while True:
    num=int(input("Insira um número, para sair digite 0\n"))
    lista.append(num)
    if num==0:
        break
    if num>10:
        num10.append(num)
while True:
    dec = int(input("Deseja verificar se há um valor na lista?\n[1] - Sim\n[2] - Não\n"))
    if dec == 1:
        search = int(input("Insira o valor que deseja procurar na lista:\n"))
        if search in lista:
            print(f"O número {search} está na lista e se repete {lista.count(search)} vezes e está na posição"
                  f" {lista.index(search)}")
        else:
            print("O número não está na lista")
    elif dec == 2:
        break
lista.sort()
lista.insert(1,33)
calcmaior10=(len(num10)/len(lista))*100
print(f"Informações:\n"
      f"Número de elementos: {len(lista)}\n"
      f"Soma de elementos: {sum(lista)}\n"
      f"Maior elemento: {max(lista)}\n"
      f"Menor elemento: {min(lista)}\n"
      f"Lista em forma crescente: {lista}\n"
      f"Lista em forma decrescente: {lista.sort(reverse=True)}\n"
      f"Média dos valores da lista: {(sum(lista))/(len(lista))}\n"
      f"Quantidade de números maiores que 10: {calcmaior10}%\n")