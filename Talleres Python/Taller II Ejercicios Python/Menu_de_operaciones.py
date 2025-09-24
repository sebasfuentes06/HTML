#Programa 3: Menú de operaciones
def menu_de_operaciones():
    print("Menú de operaciones")

while True:
    print("Menú de operaciones")
    print("a. Suma")
    print("b. Resta")
    print("c. Multiplicación")
    print("d. División")
    print("e. Salir")

    opcion = input("Ingrese una opción: ").lower()

    if opcion == "e":
        print("Saliendo del programa...")
        break  

    numero1 = float(input("Ingrese primer número: "))
    numero2 = float(input("Ingrese segundo número: "))

    if opcion == "a":
        print("El resultado de", numero1, "+", numero2, "es", numero1 + numero2)
    elif opcion == "b":
        print("El resultado de", numero1, "-", numero2, "es", numero1 - numero2)
    elif opcion == "c":
        print("El resultado de", numero1, "*", numero2, "es", numero1 * numero2)
    elif opcion == "d":
        if numero2 != 0:
            print("El resultado de", numero1, "/", numero2, "es", numero1 / numero2)
        else:
            print("No se puede dividir por cero")
    else:
        print("Opción invalida")

#Ejecturar menu de operaciones
menu_de_operaciones()
    