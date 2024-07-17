"""
IMC
Crea una calculadora del
índice de masa corporal.
"""


print("Calculadora de IMC")

while True:
    height = float(input("Introduzca la altura en m --> "))
    weight = float(input("Introduzca el peso en kg --> "))
    if (height > 0 and weight > 0):
        imc = weight / (height ** 2)

        print(f"IMC = {imc:,.2f}") # 2 decimales

        if imc < 18.5:
            print("Peso bajo")
        elif 18.5 <= imc < 24.9:
            print("Peso normal")
        elif 25 <= imc < 29.9:
            print("Sobrepeso")
        else:
            print("Obesidad")
    else:
        print("Introduzca unos valores correctos")
        continue


