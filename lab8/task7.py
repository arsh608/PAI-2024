import numpy as np

arr= np.random.rand(1000)

average = np.mean(arr)
variance = np.var(arr)
std_deviation = np.std(arr)

print(f"Average: {average}")
print(f"Variance: {variance}")
print(f"Standard Deviation: {std_deviation}")

with open('task7.txt', 'w') as file:
    file.write(f"Average: {average}\n")
    file.write(f"Variance: {variance}\n")
    file.write(f"Standard Deviation: {std_deviation}\n")

print("Results saved to task7.txt")
