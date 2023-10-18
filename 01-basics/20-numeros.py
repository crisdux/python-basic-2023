import math

numero_grande = int(input("Digite un numero de 3 digitos: "))
numero_chico = int(input("Digite un numero de 1 digito: "))

dos_ultimos_digitos = numero_grande % 100

condicion1 = (dos_ultimos_digitos % numero_chico == 0)

condicion2 = (math.pow(numero_chico, 2)) < dos_ultimos_digitos

if(condicion1 and condicion2):
    print(True)
else:
    print(False)

    