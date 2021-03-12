#metodo de congruencia lineal

xn = int(5430) #Semilla o valor inicial


for i in range(10): 
    xn1 = (1103515245 * xn + 123) % 32768
    print(xn1)
    xn = xn1
    
'''
En este algoritmo se eligen 4 numero enteros, m como modulo (32768) a como multi
plicador (1103515245) , c como incremento (123) y xn como la semilla.
basicamente se realizara la operacion xn = (a*xn+c)mod m que genera los 10 numeros
aleatorios correspondientemente.
'''
