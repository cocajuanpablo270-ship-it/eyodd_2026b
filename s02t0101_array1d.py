# Array 
import array as arr

# Creación de un arreglo 
#i: Entero con signo
#I: Entero sin signo
#f: Número decimal
#d: Número decimal doble
#u: Caracteres unicode

my_array = arr.array('i',[10,22,300,3,7,40,55,455,233,245,567])

# Interación automatica
for num in my_array:    
    print(num)
# Acesso individual a los numeros
print(my_array[0]) #primer elemento
print(my_array[1]) #Segundo elemento
print(my_array[1]) #Tercer elemento

#Tamaño de arrgelo
#Length
print(len(my_array))

#interacción por indices

for i in range(len(my_array)):
    print(f"i: {i+1}: {my_array[i]}")