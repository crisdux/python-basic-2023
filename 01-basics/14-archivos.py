with open("./hola.txt", "r") as file:
    for line in file:
        print(line)

notas = {
    "pepe": "10",
    "juan": "8",
    "maria": "9"
}
with open("./notas-estudiantes.txt", "a") as file:
    for nombres, notas in notas.items():
        file.write(f"{nombres} - {notas}\n")
