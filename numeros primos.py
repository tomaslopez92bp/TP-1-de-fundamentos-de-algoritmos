
import sys

def esPrimo(n):
    # Filtramos los primeros casos cuyo comportamiento es diferente
    if n == 1:
        return "no"
    if n <= 3:
        return "sí"
    # Si el numero es par > 2 no es primo.
    if n % 2 == 0:
        return "no"
    # Buscamos los divisores, si tiene algun otro divisor, no es primo
    i = 3
    while i < n:
        if n % i == 0:
            return "no"
        i += 2
    return "sí"

def iesimoPrimo(i):
    # Filtramos los primeros casos cuyo comportamiento es diferente
    if i <= 2:
        return [2,3][i - 1]
    # Buscamos el iesimo numero primo
    primoNum = 3
    n = 5
    while True:
        if (esPrimo(n) == "sí") & (primoNum == i):
            return n
        elif esPrimo(n) == "sí":
            primoNum += 1
        n += 2

def cantidadPrimosMenoresOIguales(n):
    # Filtramos los primeros casos cuyo comportamiento es diferente
    if n <= 3:
        return n - 1
    # Buscamos los numeros primos menores o iguales a n
    cantidad = 2
    i = 5
    while i <= n:
        if esPrimo(i) == "sí":
            cantidad += 1
        i += 2
    return cantidad

def cantidadDivisoresPrimos(n):
    cantidad = 0
    cantidad += n % 2 == 0
    i = 3
    while i <= n:
        if (esPrimo(i) == "sí") & (n % i == 0):
            cantidad += 1
        i += 2
    return cantidad      

def iesimoDivisorPrimo(n, i):
    # Filtramos caso que se busque el primer divisor primo de un numero par
    if (n % 2 == 0) & (i == 1):
        return 2
    # Buscamos el iesimo divisor primo de n
    primoNum = 1
    primoNum += n % 2 == 0
    k = 3
    while k < n:
        if (esPrimo(k) == "sí") & (n % k == 0) & (primoNum == i):
            return k
        elif (esPrimo(k) == "sí") & (n % k == 0):
            primoNum += 1
        k += 2
    return str(n) + " no tiene " + str(i) + " divisores primos"

def sumaPrimerosPrimos(n):
    i = 3
    primoNum = 1
    suma = 2
    while primoNum < n:
        if esPrimo(i) == "sí":
            suma += i
            primoNum += 1
        i += 2
    return suma
 
if sys.argv[1] == "esPrimo":
    print(esPrimo(int(sys.argv[2])))
elif sys.argv[1] == "iesimoPrimo":
    print(iesimoPrimo(int(sys.argv[2])))
elif sys.argv[1] == "cantidadPrimosMenoresOIguales":
    print(cantidadPrimosMenoresOIguales(int(sys.argv[2])))
elif sys.argv[1] == "cantidadDivisoresPrimos":
    print(cantidadDivisoresPrimos(int(sys.argv[2])))
elif sys.argv[1] == "iesimoDivisorPrimo":
    print(iesimoDivisorPrimo(int(sys.argv[2]), int(sys.argv[3])))
elif sys.argv[1] == "sumaPrimerosPrimos":
    print(sumaPrimerosPrimos(int(sys.argv[2])))
