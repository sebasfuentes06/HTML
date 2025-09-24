
limite = int(input("Ingrese el número límite: "))

print(f"\nNúmeros primos entre 1 y {limite}:")

for num in range(2, limite + 1):
    es_primo = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num, end=" ")

