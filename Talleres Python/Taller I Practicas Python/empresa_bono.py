
salario = float(input("Ingrese el salario del empleado: "))
estrato = int(input("Ingrese el estrato del empleado (1-6): "))

if estrato == 1:
    porcentaje = 0.35
elif estrato == 2:
    porcentaje = 0.30
elif estrato == 3:
    porcentaje = 0.25
elif estrato == 4:
    porcentaje = 0.20
elif estrato in [5, 6]:
    porcentaje = 0.10

bono = salario * porcentaje
total = salario + bono

print(f"\nSalario base: {salario:,.0f} COP")
print(f"Bono ({porcentaje*100:.0f}%): {bono:,.0f} COP")
print(f"Total a pagar: {total:,.0f} COP")
