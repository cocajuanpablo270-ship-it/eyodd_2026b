
from array import array as array

table = [
    array('i',[1, 2, 3]),
    array('i',[4, 5, 6]),
    array('i',[7, 8, 9]),
]
# Impresión de una tabla 
def print_table(input_table):
    # Imprimiendo cada elemento
    for row in input_table:
        for column in row:
            print(column, end=' ')
        print("", end='\b')
        print()



print_table(table)
#Inserción

row = 1
column = 2
value = 99
 # Insertar en la fila 1 columna 2 el valor 99
table[row].insert(column, value)

# Imprimiendo mensaje 
print("----------- Despues de la inserción -----------")
print_table(table) # DRY

# Insertando una fila completa 
new_row = array('i',[100, 200, 300])
pos = 1
table.insert(pos, new_row)

# Imprimiendo mensaje
print("----------- Despues de la inserción de una fila completa -----------")
print_table(table) # DRY

# Eliminando elementos 
del table[2]

# Imprimiendo mensaje
print("----------- Despues de la eliminación de la fila 2-----------")
print_table(table) # DRY