# import mysql.connector


# conexao = mysql.connector.connect(
#     host='localhost',
#     username='root',
#     password='Mnickol@s1983',
# )

# print('Conexão com sucesso')

# cursor = conexao.cursor()

# comando = '''
# CREATE DATABASE IF NOT EXISTS dados_clientes
# '''
# cursor.execute(comando)

# print('DB criado com sucesso')
# # conexao.commit() >edita o banco de dados
# # resultado = cursos.fetchall() >le o banco de dados


# cursor.close()
# conexao.close()


# import mysql.connector

# # Estabelecer conexão com o servidor MySQL
# conexao = mysql.connector.connect(
#     host='localhost',
#     username='root',
#     password='Mnickol@s1983',
#     database='dados_clientes'
# )

# # Verificar se a conexão foi estabelecida com sucesso
# if conexao.is_connected():
#     print('Conexão com sucesso')

# # Criar um cursor para executar comandos SQL
# cursor = conexao.cursor()

# # Comando SQL para criar uma tabela
# comando_criar_tabela = '''
# CREATE TABLE IF NOT EXISTS clientes (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     nome VARCHAR(255),
#     idade INT,
#     cidade VARCHAR(255)
# )
# '''

# # Executar o comando SQL para criar a tabela
# cursor.execute(comando_criar_tabela)

# print('Table criado com sucesso')

# # Fechar o cursor
# cursor.close()

# # Fechar a conexão com o servidor MySQL
# conexao.close()


import mysql.connector

# Estabelecer uma nova conexão com o servidor MySQL
conexao = mysql.connector.connect(
    host='localhost',
    username='root',
    password='Mnickol@s1983',
    database='dados_clientes'
)

# Verificar se a conexão foi estabelecida com sucesso
if conexao.is_connected():
    print('Conexão com sucesso')

# Criar um cursor para executar comandos SQL
cursor = conexao.cursor()

# Comando SQL para inserir dados na tabela
comando_inserir_dados = '''
INSERT INTO clientes (nome, idade, cidade) VALUES (%s, %s, %s)
'''

# Dados a serem inseridos na tabela
dados_cliente = ('João', 30, 'São Paulo')

# Executar o comando SQL para inserir os dados na tabela
cursor.execute(comando_inserir_dados, dados_cliente)


print('Dados inseridos com sucesso')

# Commit para salvar as mudanças no banco de dados
conexao.commit()

# Fechar o cursor
cursor.close()

# Fechar a conexão com o servidor MySQL
conexao.close()