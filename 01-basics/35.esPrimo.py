
def perdirDatos():
    num = int(input("Enter a number mayor a 1: "))

    while num < 1:
        num = int(input("Enter a number mayor a 1: "))

def isPrimo(num):
    contador = 0;
    for i in range(2, num): # 2 -> 6 
        if(num % i == 0):
            contador += 1;
        if(contador > 0):
            break;

    if(contador == 0):
        print("El numero es primo")
    else:
        print("El numero no es primo")

print(perdirDatos())
print(isPrimo(7))