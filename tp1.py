import sys

def esPrimo(n):
    #filtramos los casos especiales
    if n == 1:
        return "no"
    if n <= 3: 
        return "sí"
    #filtramos todos los pares porque no son primos.
    if n % 2 == 0:
        return "no"
    #buscamos los divisores si tiene algun otro para los impares
    i = 5
    while i < n // 2 + 1:
        if n % i == 0:
            return "no"
        i = i + 2
    return "si"

if  sys.argv[1] == "esPrimo":
    print(esPrimo(int(sys.argv[2])))
    