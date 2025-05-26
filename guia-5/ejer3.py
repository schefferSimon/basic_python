"""Diseñar un programa que lea por teclado las 5 notas obtenidas
por un alumno"""
notas =[];
notas.append((float(input("ingrese su nota: "))))
notas.append((float(input("ingrese su nota: "))))
notas.append((float(input("ingrese su nota  "))))
notas.append((float(input("ingrese su nota  "))))
notas.append((float(input("ingrese su nota  "))))

"""crear una lista llamada lista_estadisticas que contengan : la nota
promedio, la mas alta y la mas baja.
mostrar los valores de la lista por pantalla """
nota_promedio= sum(notas)/len(notas);
nota_alta=max(notas)
nota_baja=min(notas)

lista_estadisticas= [nota_promedio,nota_alta,nota_baja];

print("/n Lista de promedios /n")

print("nota promedio : ", lista_estadisticas[0]);
print("nota mas alta : ", lista_estadisticas[1]);
print("nota mas baja : ", lista_estadisticas[2]);


