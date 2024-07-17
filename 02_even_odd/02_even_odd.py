"""
PAR O IMPAR
Crea un programa que compruebe si
un número entero es par o impar.
"""

def even_odd (number):
    if (number % 2 == 0):
        print("El número es par")
    else:
        print("El número es impar")

# Bucle del prgrama principal
while True:
    number = int(input("Introduzca un número para saber si es par o impar (0 = Salir) --> "))
    if (number != 0):
        even_odd(number)
    else:
        break