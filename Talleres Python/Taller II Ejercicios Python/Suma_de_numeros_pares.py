#Programa 2: Suma de números pares hasta n
n= float(input("Ingrese un número: "))
suma= 0
for i in range(2, n+1, 2):
    suma += i
print("La suma de los números pares hasta", n, "es:", suma)
