"""Crear un diccionario a partir de un set de nombres y una lista de edades, 
asegurando el orden. Convertir el set a lista y luego combinar con zip() y 
dict(). 
nombres = {"Ana", "Pedro", "Lucía"}    # set sin orden garantizado 
edades = [25, 30, 22]   # lista con orden definido """

nombres = {"Ana", "Pedro", "Lucía"} 

edades = [25, 30, 22]

nombres_ordenados = sorted(nombres)
edades.sort()
#combinacion de lista y set 
combinacion = zip(nombres_ordenados, edades)

#convertir zip en diccionario
lista_combinada =dict(combinacion)
print(lista_combinada)