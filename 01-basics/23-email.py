web_empresarial = input("ingrese la web empresarial") #www.facebook.com
primer_nombre = input("ingrese su primer nombre")
segundo_nombre = input("ingrese su segundo nombre")
primer_apellido = input("ingrese su primer apellido").lower()
anio_nacimiento = input("ingrese su año de nacimiento")

primer_nombre_resultado = primer_nombre[0].lower();
segundo_nombre_resultado = segundo_nombre[0].lower();
anio_nacimiento_resultado = anio_nacimiento[2:] # 1996
web_empresarial_resultado = web_empresarial[4:-4] # www.facebook.com

print(f"{primer_nombre_resultado}{segundo_nombre_resultado}{primer_apellido}{anio_nacimiento_resultado}@{web_empresarial_resultado}.com")