numero_user = int(input("Digite un número positivo: "))

while numero_user < 0:
    print("El numero debe ser positivo");
    numero_user = int(input("Digite um número positivo: "))

# Por ejemplo, si el usuario ingresa el número 6, el programa debe calcular la suma 2+4+6=12 y mostrar 12 como resultado.

suma = 0;
i = 0;
while i <= numero_user: # 0 < 6
    suma+=i;
    i+=2;
print(suma)
 
