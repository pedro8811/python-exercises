import numpy as np

numbers = np.array([2, 6, 7, 9, 0, 1, 2, 5, 6])
# print('Dimensões: ', numbers.ndim)
# print('Tamanho: ', numbers.shape)
# print(numbers.size)

M = np.array([[1, 3, 5], [2, 4, 6], [3, 5, 7]])
# print('Primeira coluna: ', M[:,0])
# print('Segunda coluna: ', M[:,1])
# print('Segunda linha: ', M[1,:])
# print('Dimensões: ', M.ndim)
# print('Tamanho: ', M.shape)
# print(M.size)

cubo = np.array([[[1, 4, 7], [3, 5, 2]], [[5, 6, 0], [7, 4, 1]], [[2, 8, 8], [0, 3, 6]]])
print(cubo.ndim)
print(cubo.shape)
print(cubo.size)

