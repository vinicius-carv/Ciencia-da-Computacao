from funcoes import *
conexao = cria_conexao()
cursor = conexao.cursor(conexao)
sql='''
    delete
    from td_cargo
    where idt = 3
    '''
cursor.execute(sql)
conexao.commit()
cursor.close()
fecha_conexao(conexao)