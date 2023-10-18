persona = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 28
}

print(persona["nombre"]);

## agregar
persona["sexo"] = "M";
print(persona)

## actualizar 
persona["edad"] = 30;
print(persona)

## eliminar
del persona["apellido"]
print(persona)