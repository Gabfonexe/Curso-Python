filmsList = ["Bob esponja", "Os simpsons", "Meu malvado favorito", "Carros", "Cinderela", "Bela e a Fera", "Elementos", "Frozen", "Moana", "Star Wars", "Harry Potter", "A lenda dos guardiões", "Uma noite no Museu", "Jumper"]

# 1 - Tamanho da Lista
print(len(filmsList))

# 2 - Recuperar um item da Lista pelo nome (mostrando seu index)
print(filmsList.index("Jumper"))

# 3 - Adicionar item ao final da Lista
filmsList.append("The Lord of the Rings")
print(filmsList)

# 4 - Ordenar a Lista
filmsList.sort()
print(filmsList)

# 5 - Copiar os itens de uma Lista para outra
filmsCopy = filmsList.copy()
filmsCopy.remove("Moana") # Remove o item
print(filmsCopy)

# 6 - Remover tods os itens da Lista

filmsList.clear()
print(filmsList)