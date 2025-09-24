# Programa que pide 5 números enteros y cuenta positivos, negativos y ceros

positivos = 0
negativos = 0
ceros = 0

for i in range(5):
    numero = int(input(f"Ingrese el número {i+1}: "))
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        ceros += 1

print("\nResultados:")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")
print(f"Ceros: {ceros}")
