
import time;
fib0 = 0;
fib1 = 1;
aux3 = str(time.time_ns());
aux1 = (len(aux3)) - 1;
aux2 = aux1 - 10;
aux3 = aux3[aux2:aux1];
seed = int(aux3);
aux4 = int(input("cantidad de numeros: "));
cont = 0;
while cont < aux4:
    aux5 = fib1;
    fib1 = fib0 + fib1;
    fib0 = aux5;
    res = (fib0 + fib1) % seed;    
    print(str(res)+" ")
    cont = cont + 1;
