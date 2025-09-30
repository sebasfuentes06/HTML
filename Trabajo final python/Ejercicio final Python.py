# --------------------
# Gestor de Contactos
# --------------------

# Función que muestra el menú principal al usuario
def mostrar_menu():
    print("\n--- Gestor de Contactos ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Editar contacto")
    print("4. Eliminar contacto")
    print("5. Ver todos los contactos")
    print("6. Salir")

# ------------------------------------------------------
# Función para agregar un nuevo contacto al diccionario
# ------------------------------------------------------
def agregar_contacto(contactos):
    try:
        nombre = input("Ingrese el nombre: ").capitalize()
        
        # Validación: el nombre debe contener solo letras
        if not nombre.isalpha():
            raise ValueError("El nombre solo debe contener letras.")
        
        # Verificamos si el contacto ya existe
        if nombre in contactos:
            print("El contacto ya existe.")
        else:   
            numero = input("Ingrese el número: ")
            
            # Validación: el número debe contener solo dígitos
            if not numero.isdigit():
                raise ValueError("El número debe contener solo dígitos.")
            
            # Verificamos que el número no esté asociado a otro contacto
            if numero in contactos.values():
                print("El número ya está asociado a otro contacto.")
            else:
                contactos[nombre] = numero
                print(f"Contacto {nombre} agregado.")
    
    # Capturamos errores específicos de validación
    except ValueError as e:
        print(f"Error: {e}")
    # Capturamos cualquier otro error inesperado
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# -------------------------------------------
# Función para buscar un contacto por nombre
# -------------------------------------------
def buscar_contacto(contactos):
    try:
        nombre = input("Ingrese el nombre a buscar: ").capitalize()
        if nombre in contactos:
            print(f"{nombre} → {contactos[nombre]}")
        else:
            print("Contacto no encontrado.")
    except Exception as e:
        print(f"Error al buscar contacto: {e}")

# -------------------------------------------------------
# Función para editar el número de un contacto existente
# -------------------------------------------------------
def editar_contacto(contactos):
    try:
        nombre = input("Ingrese el nombre del contacto a editar: ").capitalize()
        
        # Verificamos si el contacto existe
        if nombre in contactos:
            nuevo_numero = input("Ingrese el nuevo número: ")
            
            # Validamos que el número tenga solo dígitos
            if not nuevo_numero.isdigit():
                raise ValueError("El número debe contener solo dígitos.")
            
            # Evitamos duplicados de números
            if nuevo_numero in contactos.values():
                print("El número ya está asociado a otro contacto.")
                return
            
            contactos[nombre] = nuevo_numero
            print(f"Contacto {nombre} actualizado.")
        else:
            print("Contacto no encontrado.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# --------------------------------------------
# Función para eliminar un contacto existente
# --------------------------------------------
def eliminar_contacto(contactos):
    try:
        nombre = input("Ingrese el nombre del contacto a eliminar: ").capitalize()
        
        # Verificamos si el contacto existe
        if nombre in contactos:
            del contactos[nombre]
            print(f"Contacto {nombre} eliminado.")
        else:
            print("Contacto no encontrado.")
    
    except Exception as e:
        print(f"Error al eliminar contacto: {e}")

# -----------------------------------------------
# Función para ver todos los contactos guardados
# -----------------------------------------------
def ver_contactos(contactos):
    try:
        if contactos:
            print("\n--- Lista de Contactos ---")
            for nombre, numero in contactos.items():
                print(f"{nombre} → {numero}")
        else:
            print("No hay contactos guardados.")
    except Exception as e:
        print(f"Error al mostrar contactos: {e}")

# -----------------------------------------
# Programa principal que controla el flujo
# -----------------------------------------
def main():
    contactos = {}  # Diccionario vacío para almacenar los contactos
    
    # Bucle infinito hasta que el usuario decida salir
    while True:
        try:
            mostrar_menu()
            opcion = input("Elija una opción: ")

            # Dependiendo de la opción, llamamos a la función correspondiente
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
        
        # Permite salir con Ctrl+C sin que el programa se caiga
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Cerrando el programa...")
            break
        
        # Capturamos cualquier error inesperado en el menú principal
        except Exception as e:
            print(f"Ocurrió un error inesperado en el menú: {e}")

# -------------------------------
# Punto de entrada del programa
# -------------------------------
if __name__ == "__main__":
    main()
