#diseñar un algoritmo utilizando funciones para sumar, restar, multiplicar y dividir

def menu_operaciones():
    while True:
        print("\n--- Menú de Operaciones ---")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        
        opcion = int(input("Elige una opción: "))

        if opcion == 5:
            print("Saliendo del programa...")
            break
        
        if opcion in [1, 2, 3, 4]:
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

            if opcion == 1:
                print(f"Resultado: {num1} + {num2} = {num1 + num2}")
            elif opcion == 2:
                print(f"Resultado: {num1} - {num2} = {num1 - num2}")
            elif opcion == 3:
                print(f"Resultado: {num1} * {num2} = {num1 * num2}")
            elif opcion == 4:
                if num2 != 0:
                    print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                else:
                    print("Error: División entre cero.")
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar menú de operaciones
menu_operaciones()
