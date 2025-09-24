matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz 3x3:")
for fila in matriz:
    print(fila)

suma_diagonal = sum(matriz[i][i] for i in range(3))
print("\nSuma de la diagonal principal:", suma_diagonal)

suma_columna2 = sum(fila[1] for fila in matriz)
print("Suma de la segunda columna:", suma_columna2)
