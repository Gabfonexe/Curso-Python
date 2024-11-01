# Lista de Filmes
movieList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - Iterando valores de uma lista de filmes usando while
index = 0 
print(len(movieList))

while index < len(movieList):
  print(movieList[index])
  index += 1

# 2 - QUando a condição for atendida, o Loop será encerrado
index = 0
while index < len(movieList):
  if movieList[index] == "Inception":
    break
  print(movieList[index])
  index += 1

# 3 - Quando a condição for atentida, o Loop vai para próxima iteração
index = 0
while index < len(movieList):
  if movieList[index] == "Inception":
    index += 1
    continue
  print(movieList[index])
  index += 1

# 4 - Avaliação do filme com While
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))
total = 0
count = 0

while count < movieRating:
  note = float(input("Digite a nota para o filme:\n"))
  total += note
  count += 1

if movieRating > 0:
  average = total / movieRating
else:
  average = 0

print(f"Média de avaliação do filme {movieName} é {average:.2f}")

