"""Dadas dos listas, generar un diccionario donde las claves sean los nombres
asignados a cada lista (como strings) y los valores sean las listas. Luego,
mostrar el diccionario generado.
frutas = ["manzana", "pera", "banana"]
verduras = ["lechuga", "zanahoria", "apio"]"""

frutas = ["manzana", "pera", "banana"]
verduras = ["lechuga", "zanahoria", "apio"]

#claves para el diccionario
lista_frutas = "frutas";
lista_verduras = "verduras";

#creando diccionario
diccionario={ 
    lista_frutas : frutas,
    lista_verduras: verduras
}

print(diccionario)