from conexao import *
from mysql.connector import connect, Error
try:
    conexao = mysql.connector.connect(host='localhost',user='root',password='16Caduceus',database='')
    print("Conexão:",conexao)
    db_info = conexao.get_server_info()
    print("Connected to MySQL Server version:", db_info)
    cursor=conexao.cursor()
    cursor.execute("SHOW DATABASES")
    print('- Show databases')
    for x in cursor:
        print(x[0])
    print('Qtd. databases:', cursor.rowcount)
    sql="CREATE DATABASE if not exists db_cadastro"
    cursor.execute(sql)
    cursor.execute("SHOW DATABASES")
    registros=cursor.fetchall()
    print("- Show databases")
    print(registros)
    print("Qtd. databases", cursor.rowcount)
except Error as erro:
    print("Erro na conexão ou no create database\n", erro)
else:
    cursor.close()
    fecha_conexao(conexao)