from conexao import *
conexao = cria_conexao()
cursor = conexao.cursor(conexao)
qtd_registros(conexao)
sql='''
    select * from tb_produto
    # where nome_coluna = valor
    # where idt = 1
    # where nome = 'Arroz'
    where preco > 10
    # where dta_validade < '2021-12-01'
    '''
cursor.execute(sql)
registros = cursor.fetchall()
print("Registros na consulta: ", cursor.rowcount)
print('- List of tuplas:')
print(registros)
print('- Tuplas:')
for row in registros:
    print(row)
cursor.close()
fecha_conexao(conexao)