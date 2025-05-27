chef1 = ("sal", "pimienta", "ajo")
chef2 = ("ajo", "cebolla", "sal")
chef3 = ("pimienta", "limón", "ajo")

chef1 = set(chef1)
chef2 = set(chef2)
chef3 =set(chef3)

ingredientes_comunes = chef1 & chef2 & chef3;
print("Los ingredientes que usan en comun los chef son : ", ingredientes_comunes)

diferencia_uno = [chef1 - chef2- chef3];
print(diferencia_uno)