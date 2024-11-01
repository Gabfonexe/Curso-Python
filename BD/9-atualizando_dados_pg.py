from conexao_post import conn

cursor_obj = conn.cursor()

sql = """
    UPDATE games
    SET NAME = %s
    WHERE ID = %s
"""
                          # Passar o dado em tuplas
cursor_obj.execute(sql, ("Fifa 23", 3))
conn.commit()
print("Dados atualizados com Sucesso")
conn.close()
 