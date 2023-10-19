numero = int(input("Digite um número inteiro: ")) # 598654

contador_pares = 0;
contador_impares = 0;

while numero > 0:
    ultimo_digito = numero % 10; # 4
    if ultimo_digito % 2 == 0:
        contador_pares += 1;
    if ultimo_digito % 2 != 0:
        contador_impares += 1;
    numero = numero // 10

print("Dígitos pares:", contador_pares)
print("Dígitos impares:", contador_impares)
