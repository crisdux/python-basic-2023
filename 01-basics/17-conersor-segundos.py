cantidad_segundos = int(input("Ingrese la cantidad de segundos: "))

## 3665 -> 1h 1min 5seg

# 1h -> 3600seg
# 1min -> 60seg

horas = cantidad_segundos // 3600

minutos = (cantidad_segundos % 3600) // 60

segundos = (cantidad_segundos % 3600) % 60

print(horas, minutos, segundos)
