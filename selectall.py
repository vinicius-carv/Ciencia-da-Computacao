from funcoes import *

conexao = cria_conexao()

cursor = conexao.cursor()

sql = '''select * from tb_empregado'''
cursor.execute(sql)
registros = cursor.fetchall()

print('- List of tuplas: ')
print(registros)

print('- Tuplas: ')
for row in registros:
    print(row)

print('- Colunas, notacao de vetor:')
for row in registros:
    print("------")
    print("idt:",row[0])
    print("nome:",row[1])
    print("Data Nascimento:",row[2])
    print("Gênero:",row[3])

print('- Colunas, nome coluna:')
for idt,nome,dta_nascimento,genero, cod_cargo in registros:
    print('Nome:', nome)
    print("Preco:",dta_nascimento)
    print('Data Validade:',genero)
    print('Código cargo:',cod_cargo)
cursor.close()
fecha_conexao(conexao)