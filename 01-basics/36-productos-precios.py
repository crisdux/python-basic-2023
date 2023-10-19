productos = ["monitor", "mouse", "teclado", "microfono", "camara"];
precios = [200, 15, 25, 5, 40];

# nombre del producto con el menor precio

precio_min = min(precios) #5 
index_precio_min = precios.index(precio_min) #3
producto_mas_barato = productos[index_precio_min] #microfono
print(producto_mas_barato)

# precio del mouse

index_mouse = productos.index("mouse")
precio_mouse =precios[index_mouse]
print(precio_mouse)

## ordenar de mayor a menor
i=0;
while i < 5:
    indice_max = precios.index(max(precios));
    producto = productos[indice_max];
    print(producto, precios[indice_max]);
    del precios[indice_max];
    del productos[indice_max];
    i+=1;




