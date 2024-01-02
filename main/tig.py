from math import *  # importar biblioteca "Matemática"

# función


def tig(n, i):  # definir tig
    res = (n + 1 ) * (i / 2)
    print("g = " + str(res))

# entradas y lógica

entradas = input("Entradas (n, i): ")  # solicitudes
entradas0 = entradas.split(',')  # sistema de autocumplimiento de entradas
if len(entradas0) == 2:
    n0, i0 = entradas0[:2]
    n0 = int(n0.strip())
    i0 = int(i0.strip())
    print(tig(n0, i0))  # imprimir definición
else:
    print("Debe ingresar 3 valores.")  # error
