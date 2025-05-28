""" Dada una tupla con una secuencia de bases nitrogenadas ("A", "T", "C", "G"), 
convertirla a lista, reemplazar una base, y luego mostrar las bases presentes 
sin repetir. Previamente, escribir el pseudocódigo. 
# A: adenina, T: timina, C: citocina, G: guanina, bases que forman el ADN 
secuencia = ("A", "T", "C", "G", "A", "G", "T") """

secuencia = ("A", "T", "C", "G", "A", "G", "T") 

#conversiona a lista
lista_secuencia= list(secuencia);

#remplazar una base 
lista_secuencia[0] =["A"]

#eliminar repetidos
secuencias_set=set(lista_secuencia);

print(secuencias_set)
