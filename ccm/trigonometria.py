from math import *

# funciones


def sr(a):  # raíz cuadrada
    return sqrt(a)


def lg(a):  # logarítmo
    return log(a)


def sn(a):  # seno
    return sin(a)


def co(a):  # coseno
    return cos(a)


def tn(a):  # tangente
    return tan(a)


def ab(a):  # absoluto
    return abs(a)


def rnd(a):  # redondeo
    return round(a, 5)


def ep(a):  # exponente
    return exp(a)

# entradas y lógica

entradas = input("Entradas (Operación [sr, lg, sn, co, tn, ab, rnd, ep]), (Valor): ")
entradas0 = entradas.split(',')
if len(entradas0) == 2:
    choice, a0 = entradas0[:2]
    choice = choice.strip()
    a0 = float(a0.strip())
    if choice == "sr":
        print(round(sr(a0), 5))
    elif choice == "lg":
        print(round(lg(a0), 5))
    elif choice == "sn":
        print(round(sn(a0), 5))
    elif choice == "co":
        print(round(co(a0), 5))
    elif choice == "tn":
        print(round(tn(a0), 5))
    elif choice == "ab":
        print(round(ab(a0), 5))
    elif choice == "rnd":
        print(rnd(a0))
    elif choice == "ep":
        print(round(ep(a0), 5))
    else:
        print("Valor no permitido.")
else:
    print("Debe ingresar 2 valores.")
