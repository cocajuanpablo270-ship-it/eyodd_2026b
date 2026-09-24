"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculará la suma del 1 al 100.
"""

# Importamos biblioteca time
import time

# Funcion que suma los primeros n numeros naturales
def sum_of_n(n):

    total_sum = 0
    for number in range(1, n + 1):
        total_sum = total_sum + number
    return total_sum

# Variable para guardar el data set
dataset = []  # [(n, time, sum), (n, time, sum)]

# Repetimos el calculo con valores de 500 en 500
for repetition in range(1, 11):
    # Tomamos el tiempo inicial
    timestamp_01 = time.time()

    # Sumamos los n numeros
    n = repetition * 500
    result = sum_of_n(n)

    # Tomamos el tiempo final
    timestamp_02 = time.time()
    elapsed_time = round((timestamp_02 - timestamp_01) * 1e6, 2)

    # Agregamos la tripleta de los datos al dataset
    dataset.append((n, elapsed_time, result))

# Imprimimos el dataset
for tup in dataset:
    print(tup)