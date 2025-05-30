#crando u diccionario con claves : nombre,materias(lista de tres materias)y edad

alumno={};

#solicitar al usuario los datos del alumno
alumno["nombre"]=input("cual es tu nombre: ")
alumno["materias"]=[]
alumno["edad"]=int(input("cual es tu nombre: "))

#ingresar una lista de tres materias a la clave materias
alumno["materias"]=[
    input("primera materia: "),
    input("segunda materia: "),
    input("tercera materia")
]

alumno["materias"].append("filosofia")

print(alumno)
#comprobar si matematicas existe en el valor de la clave materias
print("matematica" in alumno["materias"] )

