
n = int(input("Ingrese un número entero positivo: "))

for i in range(1, n+1):
    cuadrado = i ** 2
    if cuadrado % 2 == 0:
        print(f"{i}^2 = {cuadrado} (par)")
    else:
        print(f"{i}^2 = {cuadrado}")
        
