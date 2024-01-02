from math import *  # importar biblioteca "Matemática"

# funciones


def side_a(b, h):  # definir side_a
    return sqrt(h ** 2 - b ** 2)  # crear cálculo


def side_b(a, h):  # definir side_b
    return sqrt(h ** 2 - a ** 2)  # crear cálculo


def hypotenuse(a, b):  # definir hypotenuse
    return sqrt(a ** 2 + b ** 2)  # crear cálculo


# entradas y lógica

choice = input("Incógnita (cateto A [a], cateto B [b], hipotenusa [h]): ")  # solicitudes
if choice == "a":
    inputs = input("Valores establecidos (cateto B, hipotenusa): ")  # solicitudes
    inputs_sep = inputs.split(',')  # sistema de autocumplimiento de entradas
    if len(inputs_sep) == 2:
        b0, h0 = inputs_sep[:2]
        b0 = int(b0.strip())
        h0 = int(h0.strip())
        print("a = " + str(round(side_a(b0, h0), 3)))  # imprimir definición
    else:
        print("Debe ingresar 2 valores.")  # error 1
        exit(0)

elif choice == "b":
    inputs = input("Valores establecidos (cateto A, hipotenusa): ")  # solicitudes
    inputs_sep = inputs.split(',')  # sistema de autocumplimiento de entradas
    if len(inputs_sep) == 2:
        a0, h0 = inputs_sep[:2]
        a0 = int(a0.strip())
        h0 = int(h0.strip())
        print("b = " + str(round(side_b(a0, h0), 3)))
    else:
        print("Debe ingresar 2 valores.")  # error 2
        exit(0)

elif choice == "h":
    inputs = input("Valores establecidos (cateto A, cateto B): ")  # solicitudes
    inputs_sep = inputs.split(',')  # sistema de autocumplimiento de entradas
    if len(inputs_sep) == 2:
        a0, b0 = inputs_sep[:2]
        a0 = int(a0.strip())
        b0 = int(b0.strip())
        print("h = " + str(round(hypotenuse(a0, b0), 3)))
    else:
        print("Debe ingresar 2 valores.")  # error 3
        exit(0)

else:
    print("Valor no permitido.")  # error 4
