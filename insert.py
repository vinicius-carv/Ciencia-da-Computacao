from conexao import *
import mysql.connector
conexao = cria_conexao()
cursor= conexao.cursor()
sql="""
    insert into tb_funcionario
    (idt, nome, salario)
    values
    # (1, 'Alice', 3000.00)
    # (2, 'Rogerio', 4000.00)
    # (3, 'Vinicius', 2000.00)
    # (8, 'Natalia', 13000.00)
    # (9, 'Lucas', 3000.00) #Dois
    # (10, 'Samuel', 4000.00)
    """
cursor.execute(sql)
print("Registros inseridos:", cursor.rowcount)
conexao.commit()
cursor.close()
fecha_conexao(conexao)