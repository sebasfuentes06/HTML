estudiantes = [
    {"nombre": "Ana", "edad": 20, "nota": 4.5},
    {"nombre": "Luis", "edad": 22, "nota": 3.8},
    {"nombre": "María", "edad": 21, "nota": 4.9}
]

print("Nombres de los estudiantes:")
for est in estudiantes:
    print(est["nombre"])

suma_notas = sum(est["nota"] for est in estudiantes)
promedio = suma_notas / len(estudiantes)
print("\nPromedio de notas:", round(promedio, 2))

mejor_estudiante = max(estudiantes, key=lambda x: x["nota"])
print("\nEstudiante con la nota más alta:", mejor_estudiante["nombre"], "-", mejor_estudiante["nota"])
