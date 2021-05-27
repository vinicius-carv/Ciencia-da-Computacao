from funcoes import *
conexao = cria_conexao()
cursor = conexao.cursor()   
sql="""
    insert into tb_produto
    (nome, preco, dta_validade)
    values (%s, %s, %s)
    """
a_nome=input('Nome: ')
a_preco=float(input('Preço: '))
a_data= input('aaaa-mm-dd: ')
a_nome1=input('Nome: ')
a_preco1=float(input('Preço: '))
a_data1= input('aaaa-mm-dd: ')
lista=[(a_nome, a_preco, a_data),
       (a_nome1, a_preco1, a_data1)]
cursor.executemany(sql,lista)
print("Registros inseridos: ",cursor.rowcount)
conexao.commit()
cursor.close()
fecha_conexao(conexao)