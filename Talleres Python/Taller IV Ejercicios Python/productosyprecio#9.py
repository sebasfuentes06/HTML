productos = {
    "Arroz": 2500,
    "Leche": 3800,
    "Pan": 1500,
    "Huevos": 12000,
    "Café": 8000
}

producto_buscar = input("Ingrese un producto: ")
if producto_buscar in productos:
    print(f"El precio de {producto_buscar} es: {productos[producto_buscar]}")
else:
    print("El producto no existe en la lista.")

total = sum(productos.values())
print("\nPrecio total de todos los productos:", total)

mas_caro = max(productos, key=productos.get)
mas_barato = min(productos, key=productos.get)

print("\nProducto más caro:", mas_caro, "-", productos[mas_caro])
print("Producto más barato:", mas_barato, "-", productos[mas_barato])
