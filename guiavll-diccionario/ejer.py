#crear un diccionario con las claves : nombre,precio,stock

product = {
    "nombre" : "",
    "precio": 0,
    "stock" :0
}

#agregando nuevas claves
product["categoria"] = ""

#ingresar valores a claves por teclado
product["nombre"] = input("ingrese un valor:  ");
product["precio"] = float(input("ingrese valor: ")) 
product["stock"]= int(input("ingrese su stock " ))
product["categoria"]= input("ingrese su categoria ")

print(product)