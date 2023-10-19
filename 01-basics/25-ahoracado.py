import random

palabras = ["ruby", "java", "python", "javascript"] ## j _ _ a

indice_random = random.randint(0, len(palabras) - 1)
palabra_random = palabras[indice_random]

primera_letra = palabra_random[0]
ultima_letra = palabra_random[-1]

guiones_palabra_random = len(palabra_random)-2;

adivinar_palabra = primera_letra + " _ " * guiones_palabra_random + ultima_letra
print(f"la palabra es {adivinar_palabra}")
condicion = palabra_random == input("Cual es la palabra secreta: ")
if(condicion):
    print("Ganaste")
else:
    print("Perdiste")