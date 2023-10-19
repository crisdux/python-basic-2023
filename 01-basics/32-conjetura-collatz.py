# Solicita al usuario ingresar un número entero positivo mayor que 1
while True:
    try:
        numero = int(input("Ingrese un número entero positivo mayor que 1: "))
        if numero > 1:
            break
        else:
            print("Por favor, ingrese un número mayor que 1.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

# Implementa la Conjetura de Collatz y cuenta las operaciones
operaciones = 0
while numero != 1:
    if numero % 2 == 0:
        numero //= 2
    else:
        numero = 3 * numero + 1
    operaciones += 1

# Muestra el número de operaciones necesarias para llegar a 1
print(f"Se necesitaron {operaciones} operaciones para llegar a 1 utilizando la Conjetura de Collatz.")
