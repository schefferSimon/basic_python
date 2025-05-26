"""Dada una lista que contiene tuplas con horarios (hora, minuto), eliminar los
horarios duplicados y ordenarlos de menor a mayor"""

horarios = [(8, 30), (9, 15), (8, 30), (10, 45), (9, 15)]

borrar_repetidos = set(horarios);
print(borrar_repetidos)

lista_horarios=list(borrar_repetidos);

lista_horarios.sort()



print(lista_horarios)

