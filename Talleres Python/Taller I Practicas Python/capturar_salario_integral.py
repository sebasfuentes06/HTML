
SMLV = float(input("Ingrese el salario mínimo legal vigente en Colombia (en COP): "))

salario_integral_min = 13 * SMLV

salario = float(input("Ingrese su salario en pesos colombianos (COP): "))

if salario >= salario_integral_min:
    print(f"Su salario es integral (es ≥ {salario_integral_min:,.0f} COP).")
else:
    print(f"Su salario NO es integral (es < {salario_integral_min:,.0f} COP).")
