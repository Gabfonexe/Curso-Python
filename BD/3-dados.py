import sqlite3

# 1 - Conectando no BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Inserindo Dados
cursor.execute(
  """
      INSERT INTO filmes(nome, ano, nota)
      VALUES ('Super Mario Bros', 2022, 9.5)
  """
)

conexao.commit()
conexao.close()
print("Dados inseridos na tabela")

