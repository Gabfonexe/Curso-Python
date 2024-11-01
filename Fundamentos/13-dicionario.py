filmMoana = {
  "title": "Moana",
  "yearRelease": 2017,
  "imdbRating": 9.1,
  "genre": ["fantasy", "Action"]
}
print(filmMoana)
print(len(filmMoana))
print(type(filmMoana))

# 1 - Recuperar um elemento do dicionário
print(filmMoana['genre'])
print(filmMoana.get('imdbRating')) # através do get

# 2 - Buscar apenas as chaves do dicionário
print(filmMoana.keys())

# 3 - Buscar apenas os valores do dicionário
print(filmMoana.values())

# 4 - Buscar itens do dicionário com chave e valor
print(filmMoana.items())

# 5 - Adicionar itens no dicionário 
filmMoana["director"] = "Carla Moanuz"
print(filmMoana)


# 6 - Atualizar itens no dicionário
filmMoana.update({"imdbRating":9.3})
print(filmMoana)

# 7 - Remover item no dicionário
filmMoana.pop("director")
print(filmMoana)
