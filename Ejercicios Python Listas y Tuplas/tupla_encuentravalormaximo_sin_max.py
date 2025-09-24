numeros=(15,28,3,50,7,42)
maximo=numeros[0]
minimo=numeros[0]
for num in numeros:
    if num > maximo:
        maximo = num
    if num < minimo:
        minimo = num
print("maximo:", maximo)
print("minimo", minimo)

