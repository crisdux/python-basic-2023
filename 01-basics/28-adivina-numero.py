import random
## adiviar el numero random

numero_usuario  = int(input("Ingrese un numero: ")) # 50
numero_random = random.randint(1,100) # 42

print(f"entrada: {numero_usuario}")
print(f"el random es {numero_random}")

intentos = 0;
while numero_usuario != numero_random:
    if(numero_usuario < numero_random):
        print("El numero es mas grande")
        numero_usuario = int(input("Ingrese un numero: "))
        intentos+=1
    elif(numero_usuario > numero_random):
        print("El numero es mas pequeño")
        numero_usuario = int(input("Ingrese un numero: "))
        intentos+=1;



    

    
        
