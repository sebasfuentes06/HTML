#def : Se usa para definir una función
#tabla_multiplicar : Nombre de la función
#numero : Parámetro de la función
def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

#Solicitar número al usuario
numero = int(input("Introduce un número entero: "))
tabla_multiplicar(numero) #tabla_multiplicar: se invoca la función
