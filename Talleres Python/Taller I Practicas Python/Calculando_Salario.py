# Capturar el salario del usuario
salario = float(input("Ingrese su salario: "))

# Calcular el aporte a salud (suponiendo 4% del salario)
aporte_salud = salario * 0.04

# Mostrar el resultado
print(f"El valor a pagar por salud es: ${aporte_salud:.2f}")
