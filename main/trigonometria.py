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

entradas = input("Entradas (Operación [sqrt, log, sin, cos, tan, abs, round, exp]), (Valor): ")
entradas0 = entradas.split(',')
if len(entradas0) == 2:
    choice, a0 = entradas0[:2]
    choice = choice.strip()
    a0 = float(a0.strip())
    if choice == "sqrt":
        print(round(sr(a0), 5))
    elif choice == "log":
        print(round(lg(a0), 5))
    elif choice == "sin":
        print(round(sn(a0), 5))
    elif choice == "cos":
        print(round(co(a0), 5))
    elif choice == "tan":
        print(round(tn(a0), 5))
    elif choice == "abs":
        print(round(ab(a0), 5))
    elif choice == "round":
        print(rnd(a0))
    elif choice == "exp":
        print(round(ep(a0), 5))
    else:
        print("Valor no permitido.")
else:
    print("Debe ingresar 2 valores.")
