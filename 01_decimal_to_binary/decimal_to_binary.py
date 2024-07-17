"""
DECIMAL A BINARIO
Crea un programa se encargue de
transformar un número decimal a binario.
"""

decimal = int(input("Introduzca un número decimal para pasarlo a binario --> "))

binary = ""

while decimal > 0:
    binary = f"{decimal % 2}{binary}"
    decimal //= 2

print(f"El número {decimal} en binario se escribe: {binary}")