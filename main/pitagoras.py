from math import *

# funciones


def side_a(b, h):
    return sqrt(h ** 2 - b ** 2)


def side_b(a, h):
    return sqrt(h ** 2 - a ** 2)


def hypotenuse(a, b):
    return sqrt(a ** 2 + b ** 2)


# entradas y lógica

choice = input("(Incógnita [cateto A (a), cateto B (b), hipotenusa (h)]): ")
if choice == "a":
    inputs = input("(cateto B, hipotenusa): ")
    inputs_sep = inputs.split(',')
    if len(inputs_sep) == 2:
        b0, h0 = inputs_sep[:2]
        b0 = int(b0.strip())
        h0 = int(h0.strip())
        print("a = " + str(round(side_a(b0, h0), 3)))
    else:
        print("Debe ingresar 2 valores.")
        exit(0)

elif choice == "b":
    inputs = input("(cateto A, hipotenusa): ")
    inputs_sep = inputs.split(',')
    if len(inputs_sep) == 2:
        a0, h0 = inputs_sep[:2]
        a0 = int(a0.strip())
        h0 = int(h0.strip())
        print("b = " + str(round(side_b(a0, h0), 3)))
    else:
        print("Debe ingresar 2 valores.")
        exit(0)

elif choice == "h":
    inputs = input("(cateto A, cateto B): ")
    inputs_sep = inputs.split(',')
    if len(inputs_sep) == 2:
        a0, b0 = inputs_sep[:2]
        a0 = int(a0.strip())
        b0 = int(b0.strip())
        print("h = " + str(round(hypotenuse(a0, b0), 3)))
    else:
        print("Debe ingresar 2 valores.")
        exit(0)

else:
    print("Valor no permitido.")
