paises = ("Colombia", "México", "Argentina", "Brasil", "Chile")
print("Tupla original:", paises)

# Intentar cambiar un valor (esto dará error porque las tuplas son inmutables)
# paises[2] = "Perú"   # ❌ Esto generará un TypeError

# Convertir la tupla a lista
paises_lista = list(paises)

# Modificar un valor (cambiamos "Argentina" por "Perú")
paises_lista[2] = "Perú"

# Convertir de nuevo a tupla
paises_modificada = tuple(paises_lista)

print("Tupla modificada:", paises_modificada)
