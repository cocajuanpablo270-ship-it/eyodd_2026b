from array import array as arr 

# Parametros de mi cuadricula 

rows = 8
columns = 2 * rows - 1

# Creando la reticula 2D
matrix = []

# Contruyendo el grid 
for row in range(rows):
    # Creando una fila
    new_row = arr('i', [0] * columns)
    # Agregando la fila a la matriz
    matrix.append(new_row)

    # validando la construcción del grid
    print("cantidad de filas : ", len(matrix))
    print("cantidad de columnas : ", len(matrix[0]) if matrix else 0)

    for row in matrix:
        print("list(row)")
