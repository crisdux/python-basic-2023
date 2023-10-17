nombre = "Cris";
print(nombre[0]) # C

pais = "Bolivia";
# print(pais[10]); # error

# cortar una tajada

print(pais[0:3]) # Bol

print(len(pais)) # 7

mensaje = "Hola mundo, como estas el dia de hoy?";
# Hola, como estas hoy?

str1 = mensaje[:4]; # desde el inicio hasta la posicion 4
str2 = mensaje[10:22]; # desde la posicion 10 hasta la posicion 22
str3 = mensaje[32:] # desde la posicion 32 hasta el final

print((str1 + str2 + str3)) # concatenamos para tener el resultado

mensaje = "Hola mundo, como estas el dia de hoy?";
# Hola, como estas hoy?

comunicado = "Hoy es martes, y juega Bolivia";

print(comunicado[::2]) # desde el inicio hasta el final, saltando de 2 en 2
