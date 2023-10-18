## for para cadenas
for i in "hola mundo":
    print(i,end=".")

## for para arreglos
for i in [1,2,5,9,3]:
    print(f"el numero es:{i}")

## for para diccionarios
persona = {
    "nombre": "Cris",
    "edad":27,
    "sexo": "M",
}
for i in persona:
    print(f"la llave es: {i} para {persona[i]}")

for values in persona.values():
    print(f"el valor es: {values}")

for key,values in persona.items():
    print(f"la llave es: {key} y el valor es: {values}")

