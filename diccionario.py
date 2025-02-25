d1 = {"Nombre": "samanta", "Edad":27,"Direccion":"tepeji", "e_mail": "sama@.gamil.com"}
d2 = {"Nombre": "maria", "Edad":30,"Direccion":"tula", "e_mail": "maria35@.gamil.com"}
d3 = {"Nombre": "jose", "Edad":25,"Direccion":"jilotepec", "e_mail": "pepe@.gamil.com"}
print(d1)
print(d2)
print(d3)

print (d1['Nombre']) #samanta
print(d1.get('Direccion'))  #consultar direccion

#para modificar un elemento usar [] usando key y asiganar un valor nuevo 
d2['Nombre']= "Laura"
print (d2)

#si el key no existe lo añade
d1 ['cp']=54240
print(d1)

#value().-devuelve los valores del diccionario 
print(list(d1.values()))

#popitem.- elimina el ultimo elemento del diccionario 
d1.popitem()

#pop se puede eliminar un elemento en particular 
salida=d1.pop('Edad')
print (d1)

#update.- llama un diccionario y tiene como entrada otro diccionario 
t1= {'a': 100, 'b':200}
t2 = {'e':50, 'd':400}
t1.update(t2)
print (t1)