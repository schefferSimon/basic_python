""" Tres artículos tienen listas de palabras clave. Mostrar: 
a. Palabras que aparecen en al menos dos artículos. 
b. Palabras exclusivas de solo uno. 
art1 = ["inteligencia", "artificial", "datos"] 
art2 = ["datos", "aprendizaje", "modelo"] 
art3 = ["modelo", "patrones", "datos"] """ 

art1 = ["inteligencia", "artificial", "datos"] 
art2 = ["datos", "aprendizaje", "modelo"] 
art3 = ["modelo", "patrones", "datos"]

art1, art2, art3 = set(art1),set(art2), set(art3)

#obtener palabra en comun
enComun = art1 & art2 & art3
print(enComun)

#obtenr palabra unica
unicos = art1 ^ art2 ^ art3 ^ enComun
print(unicos)
