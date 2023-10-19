number_user = int(input("Enter a number: ")) # 12345

contador_pares = 0;
contador_impares = 0;

while number_user > 0:
    ultimo_digito = number_user % 10; # 5
    number_user = number_user // 10; # 1234
    if ultimo_digito % 2 == 0:
        contador_pares += 1;
    if(ultimo_digito % 2 != 0):
        contador_impares += 1;
print(contador_pares)
print(contador_impares)