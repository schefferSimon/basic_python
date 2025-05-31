"""Crear un diccionario catalogo con claves: nombre de película y valores como 
otro diccionario con claves internas: director, año, género. Acceder al género 
de una película específica. """

catalogo = {
    "nombre_de_pelicula" : {
        "director":"yo",
        "año":2022,
        "genero":"crack"
    },

}

#mostar el valor dentro de un diccionario dentro de otro
print(catalogo["nombre_de_pelicula"]["genero"])
