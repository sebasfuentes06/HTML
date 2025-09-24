palabra = input("Ingrese una palabra: ")
letra = input("Ingrese una letra: ")
contador = 0
for caracter in palabra:
    if caracter.lower() == letra.lower():
        contador += 1
    
if contador > 0:
        print(f"La letra '{letra}' aparece {contador} veces en la palabra '{palabra}'.")    
else:
        print(f"La letra '{letra}' no aparece en la palabra '{palabra}'.")