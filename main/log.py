from math import *  # importar biblioteca "Matemática"

# funciones


def logs(x, b):  # definir logs
    return log10(b) / log10(x)  # crear cálculo

# lógica y entradas

entradas = input("Valores establecidos (Base, Argumento): ")  # solicitudes
entradas0 = entradas.split(',')  # sistema de autocumplimiento de entradas
if len(entradas0) == 2:
    x0, b0 = entradas0[:2]
    x0 = int(x0.strip())
    b0 = int(b0.strip())
    print("x = " + str(logs(x0, b0)))  # imprimir definición
else:
    print("Debe ingresar 2 valores.")  # error
