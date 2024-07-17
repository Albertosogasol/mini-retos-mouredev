"""
CONTADOR DE VOCALES
Crea un programa que cuente cuantas
vocales tiene una cadena de texto.
"""

vowels = "aeiou" # Cadena con vocales
counter = 0 # Contador

string = input("Introduzca una cadena de texto para contar sus vocales --> ")

for char in string.lower(): # Se pasa todo a minusculas. Python diferencia mayusculas de minusculas
    if char in vowels: # Comprobación de vocales
        counter += 1

print(f"La cadena introducida tiene: {counter} vocales")
