elementos=[1,2,2,3,4,4,5,6,6,7]
unicos=[] # esto es una lista vacia
for elemento in elementos: 
    if elemento not in unicos: #not in = no esta dentro de
        unicos.append(elemento) # agregar elementos en la lista llamada: unicos
print("lista sin duplicados", unicos)

