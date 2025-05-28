"""Tres centros logísticos registran en tuplas los productos enviados. Unificar todos 
los productos, eliminando duplicados, y mostrar cuántos productos únicos hay y 
sus nombres ordenados. 
centro1 = ("leche", "pan", "queso") 
centro2 = ("pan", "aceite", "harina") 
centro3 = ("queso", "fideos", "harina")"""

centro1 = ("leche", "pan", "queso") 
centro2 = ("pan", "aceite", "harina") 
centro3 = ("queso", "fideos", "harina")

centro1,centro2,centro3 = set(centro1), set(centro2),set(centro3);

#unificando set
listaEntera = centro1 | centro2 |centro3

#conversion de lista para ordenar
listafinal = list(listaEntera)

#ordenar lista
listafinal.sort()

print(listafinal)


