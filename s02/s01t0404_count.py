# Ejercicio Final 
# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack'] # 0(1)

def random_function(students):
    first = students[0] # 0(1) 
    total = 0 # 0(1)
    new_list = [] # 0(1)

    for student in students: # 0(n)
        total += 1 # 0(1)
        new_list.append(student) # 0(1)

    print(new_list) # 0(n)
    return total # 0(1)

print(random_function(student_list_01))

# Calcular O(n)