# Função Anônima, com sintaxe mais reduzida


# Função de potência de um número
power = lambda num: num ** 2

# Função que verifica se o número é par
is_even = lambda x: x % 2 == 0

# Função que divide um número por outro
div_num = lambda x,y: x / y

# Função que inverte uma string
reverse_string = lambda s: s[::-1]

print(power(5))
print(power(9))
print(is_even(5))
print(is_even(7))
print(div_num(10, 2))
print(div_num(5, 2))
print(reverse_string("Python"))
print(reverse_string("Cavalo"))


# Funcionalidades relacionadas aos filmes: 

movie_list = ["Moana", "Harry Potter", "Jumper"]
ratings = {
  "Moana": [8.1, 7.9, 9.5],
  "Harry Potter": [9.1, 7.2, 9.8],
  "Jumper" : [6.1, 7.6, 8.5]
}

# Função para calcular a média de avaliações de um film
average_rating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

print(f'Média de avaliação do filme Moana: {average_rating("Moana")}')


# Função que verifica se um filme está na Lista
check_movie = lambda movie_name: movie_name in movie_list

print(f'Inception está na lista? {check_movie("Inception")}')

# Função para recomendar um filme com base na avaliação média
recommend_movie = lambda movie_name: f"Recomendo assistir {movie_name} com média de {average_rating(movie_name):.2f}"

print(f'{recommend_movie("Jumper")}')




