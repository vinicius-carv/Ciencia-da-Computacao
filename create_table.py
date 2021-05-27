from funcoes import *
try:
    conexao = cria_conexao()
    cursor = conexao.cursor()
    sql="show tables"
    cursor.execute(sql)
    for x in cursor:
        print(x[0])
    print("Qtd. tables:",cursor.rowcount)
    #criar primeiro a tabela que não tem a foreign key
    sql_cargo= """CREATE TABLE IF NOT EXISTS td_cargo(
    idt INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(45) UNIQUE NOT NULL,
    PRIMARY KEY (idt)
    )   """ 
    cursor.execute(sql_cargo)
    cursor.execute(sql)
    print('Tabelas:')
    for x in cursor:
        print(x[0])
    sql_empregado=""" CREATE TABLE IF NOT EXISTS tb_empregado(
        idt INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(45) NOT NULL,
        dta_nascimento date NULL,
        genero enum('M', 'F') NOT NULL,
        cod_cargo int NOT NULL,
        FOREIGN KEY(cod_cargo) REFERENCES td_cargo(idt),
        PRIMARY KEY (idt)
    )"""
    cursor.execute(sql_empregado)
    cursor.execute(sql)
    print("Tabelas:")
    for x in cursor:
        print(x[0])
    print("Qtd. tabelas:",cursor.rowcount)
except Error as erro:
    print("Erro no create table.\n",erro)
else:
    cursor.close()
    fecha_conexao(conexao)