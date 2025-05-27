silabas = ["ba", "be", "bi", "ba", "bo", "bu", "be"];

#eliminar duplicados convirtiendo en un conjunto/set
silabas_simplificadas= set(silabas)
print(silabas_simplificadas)

#convertir el set en lista para iterar
lista_silabas= list(silabas_simplificadas)
print(lista_silabas)

#ordenar la lista alfabeticamente
lista_silabas.sort()
print(lista_silabas)

#lista ordenada alfabeticamente al reves
lista_silabas.reverse()
print(lista_silabas)

#lista convertida en tupla
tupla_lista= tuple(lista_silabas)
print(tupla_lista)