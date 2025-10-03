# Gestor de Contactos (VERSIÓN CON 20 ERRORES A PROPÓSITO)

# --------------------
# Gestor de Contactos
# --------------------

# Función que muestra el menú principal al usuario
def mostrar_menu():
    print(f"\n---Gestor de Contacto---")          # ERROR 1: 'prin' no existe | ERROR 2: MENU_TITULO indefinido
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
        nombre = input("Ingrese el nombre: ").capitalize()   # ERROR 3: capitalizee()
        
        # Validación: (incorrecta) usa isdigit en vez de isalpha
        if not nombre.isalpha():                               # ERROR 4: lógica equivocada
            raise ValueError("El nombre solo debe contener letras.")
        
        # Verificamos si el contacto ya existe
        if nombre in contactos:
            print("El contacto ya existe.")
        else:   
            numero = input("Ingrese el número: ")
            # Validación del número: compara el método en vez de llamarlo
            if not numero.isdigit():                   # ERROR 5: falta invocación ()
                raise ValueError("El número debe contener solo dígitos.")
            
            # Verificamos que el número no esté asociado a otro contacto
            if numero in contactos.values():                    # ERROR 5 (bis): value() mal escrito (AttributeError)
                print("El número ya está asociado a otro contacto.")
            else:
                contactos[nombre] = numero                # ERROR 6: guarda int (tipo inconsistente)
                print(f"Contacto {nombre} agregado.")
    
    # Capturamos errores específicos de validación
    except ValueError as e:
        print(f"Error: {e}")                                  # ERROR 7: 'ex' no existe
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
            print("contacto no encontrado.")
    except Exception as e:
        print(f"error al buscar contacto: {e}")                  # ERROR 8: 'nombree' no existe

# -------------------------------------------------------
# Función para editar el número de un contacto existente
# -------------------------------------------------------
def editar_contacto(contactos):
    try:
        nombre = input("Ingrese el nombre del contacto a editar: ").capitalize()
        
        if nombre in contactos:
            nuevo_numero = input("Ingrese el nuevo número: ")
            
            if not nuevo_numero.isdigit():                  # ERROR 9: isnumericc() no existe
                raise ValueError("El número debe contener solo dígitos.")
            
            if nuevo_numero in contactos.values():
                print("El número ya está asociado a otro contacto.")
                return
            
            contactos[nombre] = nuevo_numero                  # ERROR 10: 'nombree' no existe
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
        del contactos[nombre]                                    # ERROR 11: 'contacto' no existe
        print(f"Contacto {nombre} eliminado.")
    except Exception as e:
        print(f"Error al eliminar contacto: {e}")

# -----------------------------------------------
# Función para ver todos los contactos guardados
# -----------------------------------------------
def ver_contactos(contactos):
    try:
        if contactos:
            print("\n--- Lista de Contactos ---")
            for nombre, numero in contactos.items():            # ERROR 12: item() en lugar de items()
                print(f"{nombre} → {numero}")                  # ERROR 13: 'número' no existe
        else:
            print("No hay contactos guardados.")
    except Exception as e:
        print(f"Error al mostrar contactos: {e}")

# -----------------------------------------
# Programa principal que controla el flujo
# -----------------------------------------
def main():
    contactos = {}   # ERROR 14: lista en lugar de diccionario
    
    while True:
        try:
            mostrar_menu()
            opcion = input("Elija una opción: ")          # ERROR 15: int comparado con strings

            if opcion == "1":
                agregar_contacto(contactos)                    # ERROR 17: función mal escrita
            elif opcion == "2":
                buscar_contacto(contactos)                      # ERROR 18: variable 'contacto' no existe
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
                mostrar_menu()                                 # ERROR 16: nombre con tilde
        except KeyboardInterrupt:
            print("\nInterrupción detectada. Cerrando el programa...")
            break                                      # ERROR 19: 'sys' no importado
        except Exception as e:
            print(f"Ocurrió un error inesperado en el menú: {e}")

# -------------------------------
# Punto de entrada del programa
# -------------------------------
if __name__ == "__main__":   # ERROR 20: '=' en lugar de '==', SyntaxError
    main()
