silabas = ["ba", "be", "bi", "ba", "bo", "bu", "be"];

#eliminar duplicados convirtiendo en un conjunto/set
silabas_simplificadas= set(silabas)


#convertir el set en lista para iterar
lista_silabas= list(silabas_simplificadas)


#ordenar la lista alfabeticamente
lista_silabas.sort()


#lista ordenada alfabeticamente al reves
lista_silabas.reverse()


#lista convertida en tupla
tupla_lista= tuple(lista_silabas)
print(tupla_lista)