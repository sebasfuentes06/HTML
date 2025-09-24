
aprobadas = 0
reprobadas = 0

for i in range(5):
    nota = float(input(f"Ingrese la nota {i+1} (0 a 5): "))
    
    if nota >= 3.0:
        print(f"Nota {nota} → Aprobada")
        aprobadas += 1
    else:
        print(f"Nota {nota} → Reprobada")
        reprobadas += 1

print("\nResumen final:")
print(f"Total de aprobadas: {aprobadas}")
print(f"Total de reprobadas: {reprobadas}")
