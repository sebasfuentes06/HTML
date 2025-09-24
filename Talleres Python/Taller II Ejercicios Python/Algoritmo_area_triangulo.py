#Diseñar un algoritmo con función para calcular el área de un triángulo 
def area_triangulo(base, altura):
        area = (base * altura) / 2
        print("El área del triángulo es:", area)
   
#Ejecutar la función    
base = float(input("Ingrese la base del triángulo: "))
altura = float(input("Ingrese la altura del triángulo: "))
area_triangulo(base, altura)
