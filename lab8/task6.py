import numpy as np

a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9],[10, 11, 12],[13, 14, 15]])
b = np.array([[1, 2],[3, 4],[5, 6]])

result = np.dot(a, b)
#result = matrix_a @ matrix_b
print(result)
