import numpy as np

dtype = [('name', 'U10'), ('height', 'f4'), ('class', 'i4')]

data = np.array([
    ('Alice', 5.5, 2),
    ('Bob', 5.8, 1),
    ('Charlie', 5.7, 2),
    ('David', 5.6, 1),
], dtype=dtype)

sorted_data = np.sort(data, order=['class', 'height'])
print(sorted_data)
