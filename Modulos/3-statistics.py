import statistics

# 1 - Aplicando a média
print(statistics.mean([3,2,3,8,9]))

# 2 - APlicando a mediana
print(statistics.median([1,2,4,7,8]))
print(statistics.median([21,4,561,61,6161,78,9]))

# 3 - Aplicando a moda
print(statistics.mode([2,5,67,8,9,0,0,0,9,8,7,6,5,4,4,4,4,3,1,1,1,1,1,23,4,2,4,5,6,6,5,7,98,9,9,9,9]))


# 4 - Desvio Padrão
"""
- Quanto mais próximo de 0 for o desvio padrão, significa que os dados do conjunto estão menos dispersos
"""

print(statistics.stdev([1, 1.5, 2, 2.5, 3, 4.41, 12, 124.21, 0, 8.1, 0.14, 0.932]))