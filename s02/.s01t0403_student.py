'''''
Notas:

1. Identifico el tamaño de la entrada "n"
El tamaño de la entrada es el numero
de estudiante 
2. Es ver cuanto crece el numero de operaciones 
en mi algoritmo conforme crecen el tamaño de la entrada
Agrego las bigo identificadas
Teniendo en cuenta la cota superior asintotica
 0(n) + 0(4) = 0(n+4) = 0(n)




'''


# Creando una lista de estudiantes

student_list_01 = ['Jordan', 'Pipen', 'Curry', 'Shack']
student_list_02 = ['Mike', 'Saul', 'Walter', 'Jessy']

# Verificando presencia de estudiante 

def check_student(input_student, student_list):
    for student in student_list:
        if input_student == student: # 0(n)
            print ("✅ Estudiante encontrado") # 0(1)

# Si el estudiante no es encontrado, se imprime un mensaje de error

    print ( "❌ Estudiante no encontrado") # 0(1)
    return None

# Probando algoritmo

check_student('Walter', student_list_02)

