def sumar(a,b):
    return a+b;
print(sumar(2,2))

def getOperaciones(tipo, a,b):
    if(tipo == "suma"):
        return a+b;
    elif(tipo == "resta"):
        return a-b;
    elif(tipo == "mulp"):
        return a*b;
    elif(tipo == "div"):    
        if(b == 0):
            return "No se puede dividir por cero";
        return a / b;

print(getOperaciones("suma",2,2))
print(getOperaciones("resta", 5,4))
print(getOperaciones("mulp", 2,10))
print(getOperaciones("div", 10,2))
print(getOperaciones("div", 2,0))