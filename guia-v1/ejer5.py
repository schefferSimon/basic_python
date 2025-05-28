"""Las siguientes listas representan los elementos químicos involucrados en tres 
reacciones químicas diferentes: 

reaccion1 = ["H", "O", "Cl"] 
reaccion2 = ["O", "H"] 
reaccion3 = ["N", "Cl", "O"] 

a- Plantear el pseudocódigo,  
b- Verificar si en una reacción hay un subconjunto de otra."""

reaccion1 = ["H", "O", "Cl"] 
reaccion2 = ["O", "H"] 
reaccion3 = ["N", "Cl", "O"] 

r1 =set(reaccion1)
r2 =set(reaccion2)
r3 =set(reaccion3)

es_conjunto = r1.issubset(r2)
print(es_conjunto)
es_conjunto =r1.issubset(r3)
print(es_conjunto)

superconjunto=r1.issuperset(r2)
print(superconjunto)
superconjunto=r1.issuperset(r3)
print(superconjunto)

no_comparte=r1.isdisjoint(r2)
print(no_comparte)
no_comparte=r1.isdisjoint(r3)
print(no_comparte)

