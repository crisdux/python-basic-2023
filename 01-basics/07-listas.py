nombres = ["Juan", "Pedro", "Maria", "Luisa"];

## agregar items
nombres.append("Cris");
print(nombres);

nombres.insert(1, "Roberto");
print(nombres);

## eliminar items
nombres.remove("Maria");
print(nombres);

## actualizar item
nombres[2] = "Lia";
print(nombres);


edades = [25,26,17,20,30];
if(17 in edades):
    print("si esta");
    edades.remove(17);
print(edades);


numeros = [1,2,3,4,5,6,7,8,9,10];
res = numeros.count(10);
print(res)
print(numeros.reverse());

##sacar el ultimo elmento, dar la vuelta, y caoncatenar con otro arrglo
arr1 = [1,2,3];
arr2 = [4,5,6];

arr1.pop(); ## 3
arr1.reverse(); ## [2,1]
arr1.extend(arr2); ## [2,1,4,5,6]

print(arr1);
# recorrer el arr1

for i in arr1:
    print(i)