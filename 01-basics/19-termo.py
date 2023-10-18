import math

radio = float(input("Ingrese el radio en cm: "))
altura = float(input("Ingrese la altura en cm: "))

mi_termo = 300;
volumen = (math.pi * math.pow(radio, 2) * altura) > mi_termo
print(volumen)


