"""Crear un diccionario empleados donde las claves sean nombres y los 
valores sean sets con habilidades. Verificar si "python" está entre las 
habilidades de uno de ellos. """ 

Empleados={
    "simon":{"javascript","sql","python"},
    "sofi":{"pyhton","java"}
}

print("python" in Empleados["simon"])