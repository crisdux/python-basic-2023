def fibo(num):
    if(num == 0 or num == 1):
        return num
    else:
        return fibo(num-1) + fibo(num-2)

print(fibo(5))

# funcion que imprima los numeros de fibonacci hasta el numero ingresado en una lista

def fibo_list(num):
    fibo = [0, 1]
    for i in range(2, num): ## for(int i =2; i<=i; i++) 
        fibo.append(fibo[i-2] + fibo[i-1]) 
    return fibo

print(fibo_list(8))

## [0,1,1,2,3,5,8,13]







# 0 1 1 2 3 5 8 13 ...