"""Se tiene una lista de combinaciones de seguridad representadas como tuplas 
(número, letra), eliminar duplicados y verificar si una combinación dada por el 
usuario está entre las válidas. 
 """

combinaciones = [(1, 'A'), (2, 'B'), (1, 'A'), (3, 'C')] 

#eliminacion de duplicados
eliminar_duplicado = set(combinaciones)

combinacion_usuario = (2, 'B')

#verificacion si existe 
verificacion = combinacion_usuario in eliminar_duplicado;

print(verificacion)


