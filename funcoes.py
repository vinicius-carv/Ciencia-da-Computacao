from mysql.connector import connect, Error
def cria_conexao():
    try:
        conexao = connect(user='root',password='16Caduceus',host='127.0.0.1',database='db_cadastro')
        print("conexao:",conexao)
    except Error as erro:
        print("Erro na conexão: \n",erro)
    else:
        return conexao
def fecha_conexao(con):
    con.close()
    print("\nConexão fechada")
def qtd_registros_cargo(con):
    try:
        cursor=con.cursor()
        sql='''select * from td_cargo'''
        cursor.execute(sql)
        registros=cursor.fetchall()
        print("Cargo - registros:", cursor.rowcount)
    except Error as erro:
        print('Erro em qtd_registros cargo.\n',erro)
def qtd_registros_empregado(con):
    try:
        cursor=con.cursor()
        sql='''select * from tb_empregado'''
        cursor.execute(sql)
        registros=cursor.fetchall()
        print("Cargo - registros:", cursor.rowcount)
    except Error as erro:
        print('Erro em qtd_registros empregado.\n',erro)
def mostra_registros_cargo(con):
    try:
        cursor = con.cursor()
        sql = ''' select * from td_cargo '''
        cursor.execute(sql)
        registros = cursor.fetchall()
        print('- Cargo - registros:')
        # for row in registros:                         # Na horizontal no formato de tupla
        # print(row)
        for idt, nome in registros:  # Na horizontal com f-string
            print(f'Idt {idt}: {nome}')
        qtd_registros_cargo(con)
    except Error as erro:
        print('Erro na mostra_registros_cargo.\n', erro)
def mostra_registros_empregado(con):
    cursor = con.cursor()
    sql = ''' select * from tb_empregado '''
    cursor.execute(sql)
    registros = cursor.fetchall()
    print('- Empregado - registros:')
    # for row in registros:                         # Na horizontal no formato de tupla
    #     print(row)
    for idt, nome, dta_nascimento, genero, cod_cargo in registros:  # Na horizontal com f-string
        print(f'Idt {idt}: {nome}, {dta_nascimento}, {genero}, {cod_cargo}')
    qtd_registros_empregado(con)