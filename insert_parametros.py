from funcoes import *
from mysql.connector import Error
try:
    conexao = cria_conexao()
    cursor = conexao.cursor()
    qtd_registros_cargo(conexao)
    sql="""
        insert into td_cargo
        (nome)
        values (%s)
        """
    a_nome=input('Nome do cargo: ')
    cursor.execute(sql, (a_nome,))
    print("Registros inseridos: ",cursor.rowcount)
    qtd_registros_empregado(conexao)
    sql="""
        insert into tb_empregado
        (nome, dta_nascimento, genero, cod_cargo)
        values (%s, %s, %s, %s)"""
    a_nome=input('Nome empregado: ')
    a_dta_nascimento = input("Data nascimento (aaaa-mm-dd): ")
    a_genero = input("Genero [M] ou [F]:")
    a_cod_cargo = input('Código Cargo: ')
    tupla = (a_nome, a_dta_nascimento, a_genero, a_cod_cargo)
    cursor.execute(sql, tupla)
except Error as erro:
    print("Erro no código aí:\n",erro)
else:
    conexao.commit()
    cursor.close()
    fecha_conexao(conexao)