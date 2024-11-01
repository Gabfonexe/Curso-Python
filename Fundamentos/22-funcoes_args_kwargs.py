"""
*args - Utilizamos ele quando não temos certeza de quantos argumentos queremos ter numa função.

- Os argumentos são passados como uma tupla

**kwargs - Além dos valores podemos passar também as respctivas chaves para cada argumento

- Os argumentos são passados como dicionário
"""

# 1 - Soma de números
def sum(*num):
  sum_total = 0
  for n in num:
    sum_total += n
  print(f'Soma é {sum_total}')

sum(7)
sum(7, 9, 10)
sum(7, 9, 11, 8)
sum(7, 9, 1, 14, 12, 29)


# 2 - Apresentação de Cursos
def presentation(**data):
  for key, value in data.items():
    print(f"{key} = {value}")

print("Lista de Cursos:")
presentation(nome="Python", category="Backend", level="Iniciante")
presentation(nome="Visão Computacional com Python", category="IA", level="Avançado")
presentation(nome="Dashboard com Dash", category="Data Science", level="Intermediário")
