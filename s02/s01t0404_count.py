# Ejercicio Final 
# Creamos una lista de estudiantes
student_list_01 = ['Jordan','Pipen','Curry','Shack', 'Monroy', 'Arlet', 'Palestina'] # 0(1) -------- resp correcta 0(1) y esta no se toma en cuenta 

def random_function(students):
    first = students[0] # 0(n) ------ resp correcta 0(1) 
    total = 0 # 0(1) ------ resp correcta 0(1)
    new_list = [] # 0(1) ------ resp correcta 0(1)

    for student in students: # 0(n)
        print("Se le suma 1 al total")
        total += 1 # 0(1) ------ resp correcta 0(n)
        new_list.append(student) # 0(n) ------ resp correcta 0(n)

    print(new_list) # 0(1) ----- resp correcta 0(1)
    return total # 0(1) ----- resp correcta 0(1)

print(f"tamaño de lista: {len(student_list_01)}")
print(random_function(student_list_01))
print("")

# Calcular O(3n + 5 )= o(n) ------ resp correcta 0(2n) + 0(5) = y 0(2n + 5 )= 0(n)
# la complejidad de un forma siempre es 0(n)
# Y si dentro de un for hay otro for es 0(nˆ2)
 