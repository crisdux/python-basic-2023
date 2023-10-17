temp = int(input("Escribe una temperatura: "));
if(temp<=0):
    print("Me congelo");
elif(temp>0 and temp<=10):
    print("que frio");
elif(temp > 11 and temp <= 20):
    print("templado");
elif(temp > 21 and temp <= 30):
    print("que calor")
elif(temp > 31 and temp <= 40):
    print("me derrito")
else:
    print("jaja")
    