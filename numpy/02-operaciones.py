import numpy as np

numeros1 = [25,41,36,72];
numeros2 = [5,9,6,7];

## sumar ambos arreglos de anera paralela

i = 0;
resultado = []
for i in range(len(numeros1)):
    a = numeros1[i];
    b = numeros2[i];
    resultado.append(a+b);
print(resultado)

## sumar con numpy 
numeros1Numpy = np.array(numeros1)
numeros2Numpy = np.array(numeros2)
print(numeros1Numpy + numeros2Numpy)


## sumar arr con numero
edades = np.array([25,41,36,72]);
edadesMasDiez = edades + 10;
print(edadesMasDiez)

pesos = [72,62, 80, 65];
alturas = [1.71, 1.62, 1.72, 1.59];
## peso / (altura ** 2);

## antes:

i = 0;
IMC = [];
for i in range(len(pesos)):
    peso = pesos[i];
    altura = alturas[i];
    IMC.append(peso / (altura ** 2));
print(IMC)

## con numpy 
pesosNumpy = np.array(pesos);
alturasNumpy = np.array(alturas);

salida = pesosNumpy / (alturasNumpy ** 2);
print(salida)

