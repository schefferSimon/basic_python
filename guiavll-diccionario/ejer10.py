"""Se desea construir una lista llamada productos, en la que cada elemento 
contenga los datos de un producto de un comercio: nombre del producto, 
precio del producto, cantidad disponible, rubro al que pertenece  Crear una lista con tres productos distintos y 
mostrar por pantalla: 
a) toda la lista productos, 
b) el nombre y precio del segundo producto,  
c) el stock del primer producto 
d) la categoría del tercer producto."""

#crear una lista de productos

productos=[
    {
        "producto":"papel",
        "precio":2,
        "stock":3,
        "categoria":"papelera"
     },
    {
        "producto": "celular",
        "precio": 200,
        "stock" : 22,
        "categoria":"tienda tecnologica"
    },
    {
        "producto": "cuaderno",
        "precio": 30,
        "stock": 3,
        "categoria": "libreria"
    }
];

#mostrar el nombre y el precio del segundo producto

print("el nombre del producto es: ",productos[1]["producto"],"y su precio es",productos[1]["precio"]);

#mostrar el stock del primer producto
print("el stock que tiene el primer producto es : ",productos[0]["stock"])

#mostrar la categoria del tercer productos
print("la categoria del tercer producto es : ", productos[2]["categoria"])