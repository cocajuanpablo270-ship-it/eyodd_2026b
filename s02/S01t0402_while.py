"""
Escribir un programa que calcule
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa
calculará la suma del 1 al 100
usando un bucle while.
"""

import time


def sum_of_n(n):
    """Calcula la suma de los primeros n números naturales usando while."""
    total_sum = 0
    current_number = 1

    while current_number <= n:
        total_sum += current_number
        current_number += 1

    return total_sum


dataset = []

for repetition in range(1, 11):
    timestamp_01 = time.time()

    n = repetition * 500
    result = sum_of_n(n)

    timestamp_02 = time.time()
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)
    dataset.append((n, elapsed_time, result))

for tup in dataset:
    print(tup)

n = 100
the_sum = 0
counter = 1

start_time = time.time()
while counter <= n:
    the_sum += counter
    counter += 1
end_time = time.time()

print(f"La suma es {the_sum}")

elapsed_time = round((end_time - start_time) * 1e6, 2)
print(f"Tiempo de ejecución: {elapsed_time} microsegundos")

