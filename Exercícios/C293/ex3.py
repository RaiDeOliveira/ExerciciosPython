# EX 3

import numpy as np

soma = 0

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

for i in range(0,matriz.shape[0]):
  print(matriz[i])
  for j in range(0,matriz.shape[1]):
    soma = soma + matriz[i][j]

print(f"\nA soma de todos os elementos da matriz é igual a {soma}.")

