from conexao import *
conexao = cria_conexao()
cursor = conexao.cursor(conexao)
qtd_registros(conexao)
sql='''
    select * from tb_produto
    # where nome_coluna = valor
    # where idt = 1
    # where nome = 'Arroz'
    where preco < %s    
    # where dta_validade < '2021-12-01'
    '''
pesquisa=float(input("Preço: "))
cursor.execute(sql,(pesquisa,))
registros = cursor.fetchall()
print("Registros na consulta: ", cursor.rowcount)
print('- List of tuplas:')
print(registros)
print('- Tuplas:')
for row in registros:
    print(row)
cursor.close()
fecha_conexao(conexao)