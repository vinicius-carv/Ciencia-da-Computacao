def menu():
    l_opcoes=['c','r','u','d','e']
    print("[C] - Create\n[R] - Read\n[U] - Update\n[D] - Delete\n[E] - Exit\n")
    opcao=input().lower()
    while True:
        if opcao not in l_opcoes:
            print("Opção inválida")
        else:
            break
    return opcao
def lista_vazia():
    if lista!=[]:
        nao_vazia=True
    else:
        nao_vazia=False
        print("Lista vazia")
    return nao_vazia
def create():
    while True:
        op_in=input("Escolha uma opção:\n[f] - Incluir vários nomes sempre no final da lista;\n [p] - Incluir vários nomes em posições específicas;\n [s] - Sair").lower()
        if op_in=='f':
            while True:
                name_in=input("Insira um valor/nome e escreva '-0' para sair")
                if name_in=='-0':
                    break
                else:
                    lista.append(name_in)
        elif op_in=='p':
            if op_in == 'f':
                while True:
                    name_in = input("Insira um valor/nome e escreva '-0' para sair:\n")
                    pos_in = int(input("Insira a posição onde o valor será adicionado:\n"))
                    if name_in == '-0':
                        break
                    else:
                        lista.insert(pos_in,name_in)
        elif op_in =='s':
            break
        else:
            print("Opção inválida, digite novamente")
def read():
    if len(lista)!=0:
        for i in range(0,len(lista)):
            print(lista[i],' - ',i)
    else:
        lista_vazia()
def update():
    if len(lista)!=0:
        while True:
            op_in = input(
                "Escolha uma opção:\n[f] - Incluir vários nomes procurando pela posição;\n [p] - Incluir vários nomes procurando pelo nome;\n [s] - Sair").lower()
            try:
                if op_in=='f':
                    p = int(input("Qual posição de substituição?\n"))
                    new_name = input("Novo nome: ")
                    lista[p] = new_name
                elif op_in'p':
                    p = input("Qual o nome do item de substituição?\n")
                    replace=lista.index(p)
                    new_name = input("Novo nome: ")
                    lista[replace] = new_name
            except IndexError:
                print("A posição digitada é inválida")
    else:
        print("Lista vazia")
def delete():
    if len(lista)==0:
        print("A lista está vazia, insira um valor para depois excluir")
    else:
        op_in = input(
            "Escolha uma opção:\n[f] - Excluir vários nomes procurando pela posição;\n [p] - Excluir vários nomes procurando pelo nome;\n [s] - Sair").lower()
        print(lista)
        if op_in=='p':
            d=int(input("Insira o item que deseja excluir:\n"))

            if d not in lista:
                print(f"{d} não presente na lista")
            else:
                lista.remove(d)
        elif op_in=='f':

if __name__ == '__main__':
    lista=[]
    while True:
        op=menu()
        if op=='c':
            create()
        elif op=='r':
            read()
        elif op=='u':
            update()
        elif op=='d':
            delete()
        elif op=='e':
            break