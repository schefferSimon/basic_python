"""Se tienen 3 tuplas con ingredientes que utilizan tres chefs, escribir el 
pseudocódigo y desarrollar un programa que permita mostrar los ingredientes 
que tienen en común los tres, y los ingredientes únicos de cada uno:"""

chef1 = ("sal", "pimienta", "ajo")
chef2 = ("ajo", "cebolla", "sal")
chef3 = ("pimienta", "limón", "ajo")

chef1 = set(chef1)
chef2 = set(chef2)
chef3 =set(chef3)

ingredientes_comunes = chef1 & chef2 & chef3;
print("Los ingredientes que usan en comun los chef son : ", ingredientes_comunes)

ingrediente_unico1= chef1 - chef2 - chef3
ingrediente_unico2 = chef2 - chef1 - chef3
ingrediente_unico3 = chef3-chef1-chef2

print(ingrediente_unico1)
print(ingrediente_unico2)
print(ingrediente_unico3)