def tabla_multiplicar(numero): #def define una funcion
    for i in range(1,11):
        print(f"{numero} x {i} = {numero*i}")

#solicitar numero al usuario
numero = int(input("ingrese un numero entero: "))
tabla_multiplicar(numero)