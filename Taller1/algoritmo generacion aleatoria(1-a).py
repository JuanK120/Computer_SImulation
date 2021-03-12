# Algoritmo para el punto 1-a : 
# Generar un Algoritmo que genere una secuencia aleatoria entre 0 y 9 
# sin usar funciones aleatorias que pertenezcan a las librerías del lenguaje usado
import time;
ran = input("ingrese numero maximo: ");
ran = int(ran);
cant = input("ingrese cantidad de numeros: ")
cant = int(cant);
seed = time.time_ns();
resp = [];
cont = 0;
while len(resp) < cant:
    aux = (seed**(7/8));
    seed = aux;
    aux = aux % 13;
    if aux < ran :
        resp.append(round(aux));
        cont = cont + 1;
        if seed < 13:
            seed = time.time_ns();
for i in range(len(resp)):
    print(str(resp[i])+" ");


