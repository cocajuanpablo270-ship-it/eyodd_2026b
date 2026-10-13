# Immportando el modulo array de 
# la biblioteca array y renombrando como arr

from array import array as arr

def print_array(input):
    print("[", end="]")
    for element in input:
        print(element, end=',')
    print("\b]")
        
my_array = arr('i', [2,10,15,20])
print_array(my_array)

# Buscar el elemento 15
number_to_search = 100
for integer in my_array:
    if integer == number_to_search:
        print(f"El numero {number_to_search} se encuentra en el arreglo")
        break

#Incrementamos contador
        counter += 1
if counter == len(my_array):
    print("numero no encontrado")
else:
    print(f"El numero {number_to_search} no se encuentra en el arreglo") 
