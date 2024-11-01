movieName = "Top Gun"
movieDescription = """
  Top Gun Maverick, é um filme de aviação e aventura,
  muito consagrado na indústria
"""

print(movieName.upper()) # Tudo maiúsculo
print(movieName.lower()) # Tudo minúsculo
print(movieName.capitalize()) # Primeira Letra maiúscula
print(movieName.title()) # Primeira letra de cada palavra em maiúsculo
print(movieName.center(10, '-')) # Retorna string centralizada com caractere de preenchimento
print(movieName.find("u")) # Encontra a letra no índice
print(movieDescription.count("a")) # Conta a quantidade de letras
print(movieName.replace("Top", "Matrix")) # Troca de lugar
print(movieDescription.split(",")) # Splita em relação ao parâmetro sinalizado