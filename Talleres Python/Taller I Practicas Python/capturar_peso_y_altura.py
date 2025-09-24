
peso = float(input("Ingrese su peso en kilogramos (kg): "))
altura = float(input("Ingrese su altura en metros (m): "))

imc = peso / (altura ** 2)

print(f"Su IMC es: {imc:.2f}")

if imc < 18.5:
    print("Clasificación: Desnutrición / Bajo peso")
elif 18.5 <= imc < 25:
    print("Clasificación: Peso normal")
elif 25 <= imc < 30:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
