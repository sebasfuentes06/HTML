numeros=[34,12,5,99,67,43,21] #esto es un array [arreglo]
#ordenar en orden ascendente (de menor a mayor)
for i in range(len(numeros)): #len significa: longitud del array
    for j in range(i + 1, len(numeros)): #ciclo anidado
        if numeros[1] > numeros[j]:
            numeros[i], numeros[j] = numeros[j], numeros[i] #intercambiar posiciones

print("orden ascendente", numeros)


