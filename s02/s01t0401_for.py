"""
Escribir un programa que calcule 
la suma de los "n" numeros naturales.
Por ejemplo si n = 100, el programa 
calculará la suma del 1 al 100.
"""

# Importamos biblioteca time
import time
# Creando una marca de tiempo
timestamp_01 = time.time()

#Programa que calcula las suma
#de los n numeros naturales
n = 100
sum = 0

#Ciclo for 
for number  in range (1, n + 1):
    sum += number
print("La suma de los " + str(n) + " números naturales es: " + str(sum))