from math import *


def logs(x, b):
    return log10(b) / log10(x)

entradas = input("(Base, Argumento): ")
entradas0 = entradas.split(',')
if len(entradas0) == 2:
    x0, b0 = entradas0[:2]
    x0 = int(x0.strip())
    b0 = int(b0.strip())
    print("x = " + str(logs(x0, b0)))
else:
    print("Debe ingresar 2 valores.")
