## pedir que el usuario ingre sun numero positivo

numero_user = int(input("ingrese un numero positivo: "))

while numero_user < 0:
    numero_user = int(input("ingrese un numero positivo: "))
#5! = 5 x 4 x 3 x 2 x 1 = 120


i = 1;
resultado = 1;
while i <= numero_user:
    resultado*=i
    i = i + 1;
print(resultado)



