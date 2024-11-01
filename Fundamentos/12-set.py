filmsSet = {"Bob esponja", "Os simpsons", "Meu malvado favorito", "Carros", "Cinderela", "Bela e a Fera", "Elementos", "Frozen", "Moana", "Star Wars", "Harry Potter", "A lenda dos guardiões", "Uma noite no Museu", "Jumper"}

print(type(filmsSet))

# 1 - buscar o tamando do Set
print(len(filmsSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"Carros", True, 1, 8.7}
print(exampleSet)

# 3 - Adicionar item de outro set
filmsSet.update(exampleSet)
print((filmsSet))

# 4 - Remover um item do set
filmsSet.remove(True)
filmsSet.remove(8.7)
print(filmsSet)