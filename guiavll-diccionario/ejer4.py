"""A partir de la lista de tuplas pares = [("a", 1), ("b", 2), ("c", 3)], convertirla en
un diccionario y acceder al valor asociado a la clave "b"."""

pares = [("a", 1), ("b", 2), ("c", 3)]

#convirtiendo a la lista de tuplas en un diccionario
diccionario = dict(pares);

#accediendo al valor de la clave b
print(diccionario.get("b"))

