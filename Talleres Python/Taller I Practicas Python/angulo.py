import math

# Solicita al usuario un ángulo en grados
angulo_grados = float(input("Ingresa un ángulo en grados: "))

# Convierte el ángulo a radianes
angulo_radianes = math.radians(angulo_grados)

# Calcula seno, coseno y tangente
seno = math.sin(angulo_radianes)
coseno = math.cos(angulo_radianes)

# Para evitar error con tangente indefinida (por ejemplo, 90°, 270°, etc.)
try:
    tangente = math.tan(angulo_radianes)
except:
    tangente = "Indefinida"

# Muestra los resultados
print(f"Seno: {seno}")
print(f"Coseno: {coseno}")

# Validamos si el coseno es cercano a 0 para evitar tangente muy grande
if abs(coseno) < 1e-10:
    print("Tangente: Indefinida (división por cero)")
else:
    print(f"Tangente: {tangente}")
