"""   CEUB   -   Bacharelado em Ciência da Computação (BCC)   -   Prof. Barbosa
Teclas de atalho: ctlr <d>, duplica linha. ctrl <y>, apaga linha. ctrl </>, comenta linha.  """
from funcoes import *
try:
    conexao = cria_conexao()
    cursor = conexao.cursor()
    ''' Sintaxe:                    # Consulta em colunas de duas tabelas relacionadas.
        select t1.nome_coluna1, t1.nome_coluna2, t2.nome_coluna1
        from nome_tabela1 as t1 inner join nome_tabela2 as t2
            on t1.nome_coluna_fk = t2.nome_coluna_pk                        '''
    # Use alias no nome das tabelas no from e usw prefixo no nome das colunas no select
    sql = ''' select e.nome, e.dta_nascimento, e.genero, c.nome
              from tb_empregado as e inner join td_cargo as c
                on e.cod_cargo = c.idt                          '''
    cursor.execute(sql)
    registros = cursor.fetchall()           # registros é uma lista de tuplas
    print('- List of tuplas:')
    print(registros)                        # Mostra os registros na horizontal
    print('- Tuplas:')
    for row in registros:
        print(row)                          # Mostra os registros na vertical
    print("- Colunas, notação de vetor:")
    for row in registros:
        print("Nome:", row[0])
        print("Data nascimento:", row[1])
        print('Gênero:', row[2])
        print('Nome cargo:', row[3])
    print("- Colunas, nome coluna:")
    for nome, dta_nascimento, genero, nome_cargo in registros:
        print("Name:", nome)
        print("Data nascimento:", dta_nascimento)
        print('Gênero:', genero)
        print('Nome cargo:', nome_cargo)
    print('Registros na tabela:', cursor.rowcount)
    # mostra_registros_empregado(conexao)
except Error as erro:
    print('Erro no select all.\n', erro)
else:
    cursor.close()
    fecha_conexao(conexao)

'''

- Posso usar só algumas colunas:
for row in registros:
    print("Idt:", row[0])
    print("Name:", row[1])
- Preciso usar todas as colunas, senão dá erro:
for idt, nome, preco, dta_validade in registros:
    print("Idt:", idt)
    print("Name:", nome)


'''
