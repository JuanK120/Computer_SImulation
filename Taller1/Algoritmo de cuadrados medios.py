# Algoritmo de cuadrados medios, obtenido en https://naps.com.mx 
semilla = input("Escriba semilla: ") # Semilla = numero de 4 o mas digitos 
tam1 = len(semilla) #longitud del valor de la semilla
print("Cantidad de dígitos: ", tam1)
numero1 = int(semilla) #valor semilla(entero)
for i in range(10):
	numero2 = numero1**2 #numero2 = semilla al cuadrado (entero)
	snumero2 = str(numero2) #snumero2 = semilla al cuadrado  (caracter)
	tam2 = len(snumero2) #longitud del valor de la semilla al cuadrado
	primerc = int((tam2 - tam1) / 2) #calcula el 1er caracter a extraer
 
	snumero3 = snumero2[primerc:primerc+tam1] #n digitos de la mitad (Caracter) 
	print ("{}.  {}".format(i,snumero3))
	numero1 = int(snumero3)

'''
Para el proceso, se extrae la cantidad de digitos de la semilla,
luego se convierte  este valor en entero, para en el rango producir 10 numeros
pseudo aleatorios, despues se eleva el numero inicial al cuadrado,
este valor se convierte en caracter , se cuenta la cantidad de digitos que tiene
dicho valor y se calcula el primer caracter en extraer restando ambas longitudes
y dividiendolo entre 2,se extraen n caracteres de la mitad (dependiendo el procedimiento
anterior y se convierte el valor extraido en numero. Luego se repite el proceso nuevamente.
'''

