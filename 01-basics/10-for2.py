## for con range
for i in range(1,11):
    print(f"te saludo por {i} vez")

# numero = int(input("ingrese un numero: "))
# for i in range(1,11):
#     print(f"{numero} x {i} = {numero*i}")

## obtener las vocales de una palabra
contador = 0
for i in "Cristian":
    if i in "aeiou":
        print(i)
        contador+=1
print(contador)

## contar las vocales de una lista de palabras

lista_palabras = ["cristian", "maria", "juan", "pedro"]

for palabra in lista_palabras:
    contador = 0
    for letra in palabra:
        if letra in "aeiou":
            contador+=1
    print(f"la palabra {palabra} tiene {contador} vocales")
