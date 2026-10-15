from array import array as arr

#Iimportando una función array
# del modulo array y renombrando 
# como arr
from  import print_array

my_array = arr('i', [5,10,15,20])

print("--- Antes de la inserción ---")
print_array(my_array)

# Inserción
my_array.insert(1, 90)  # Insertar 90 en el índice 1
print("--- Después de la inserción ---")
print_array(my_array)