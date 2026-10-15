# Importando el módulo array de
# la biblioteca array y renombrándolo como arr

from array import array as arr


def print_array(values):
    print("[", end="")
    for index, element in enumerate(values):
        if index > 0:
            print(", ", end="")
        print(element, end="")
    print("]")


my_array = arr('i', [2, 10, 15, 20])
print_array(my_array)

# Buscar el elemento 100
number_to_search = 100
found = False

for integer in my_array:
    if integer == number_to_search:
        found = True
        print(f"El numero {number_to_search} se encuentra en el arreglo")
        break

if not found:
    print(f"El numero {number_to_search} no se encuentra en el arreglo")
