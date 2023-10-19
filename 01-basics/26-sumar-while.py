## perdi la cantidad de numeros por input, y luego sumarlos

cantidad = int(input("Ingrese la cantidad de numeros a sumar: ")) #4
suma = 0;
i=0;
while i < cantidad:
    numero = int(input("Ingrese un numero: ")) #1,2,3,4
    suma+=numero;
    i = i+1;
print(suma)

