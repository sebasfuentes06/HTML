
# Gestor de Contactos con diccionario

def mostrar_menu():
    print("\n--- Gestor de Contactos ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("5. Ver todos los contactos")
    print("6. Salir")

def agregar_contacto(contactos):
    nombre = input("Ingrese el nombre: ").capitalize()
    if nombre in contactos:
        print("El contacto ya existe.")
    else:   
        numero = input("Ingrese el número: ")
        if numero in contactos.values():
            print("El número ya está asociado a otro contacto.")
        else:
            contactos[nombre] = numero
            print(f"Contacto {nombre} agregado.")

def buscar_contacto(contactos):
    nombre = input("Ingrese el nombre a buscar: ").capitalize()
    if nombre in contactos:
        print(f"{nombre} → {contactos[nombre]}")
    else:
        print("Contacto no encontrado.")

def editar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a editar: ").capitalize()
    if nombre in contactos:
        nuevo_numero = input("Ingrese el nuevo número: ")
        if nuevo_numero in contactos.values():
            print("El número ya está asociado a otro contacto.")
            return
        contactos[nombre] = nuevo_numero
        print(f"Contacto {nombre} actualizado.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto(contactos):
    nombre = input("Ingrese el nombre del contacto a eliminar: ").capitalize()
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto {nombre} eliminado.")
    else:
        print("Contacto no encontrado.")

def ver_contactos(contactos):
    if contactos:
        print("\n--- Lista de Contactos ---")
        for nombre, numero in contactos.items():
            print(f"{nombre} → {numero}")
    else:
        print("No hay contactos guardados.")

# Programa principal
def main():
    contactos = {}
    while True:
        mostrar_menu()
        opcion = input("Elija una opción: ")

        if opcion == "1":
            agregar_contacto(contactos)
        elif opcion == "2":
            buscar_contacto(contactos)
        elif opcion == "3":
            editar_contacto(contactos)
        elif opcion == "4":
            eliminar_contacto(contactos)
        elif opcion == "5":
            ver_contactos(contactos)
        elif opcion == "6":
            print("Saliendo del programa... ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
    