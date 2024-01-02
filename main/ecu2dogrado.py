from math import sqrt  # importar biblioteca "Raíz Cuadrada"

# funciones


def x1(a, b, c):  # definir raíz 1
    discriminante = b ** 2 - 4 * a * c  # crear cálculo
    if discriminante < 0:  # lógica de error
        return "∆ < 0"
    else:
        return (-b + sqrt(discriminante)) / (2 * a)  # imprimir resultado


def x2(a, b, c):  # definir raíz 2
    discriminante = b ** 2 - 4 * a * c  # crear cálculo
    if discriminante < 0:  # lógica de error
        return "∆ < 0"
    else:
        return (-b - sqrt(discriminante)) / (2 * a)  # imprimir resultado


def det(a, b, c):  # definir discriminante
    discriminante = b ** 2 - 4 * a * c  # crear cálculo
    return discriminante  # imprimir resultado

# entradas y lógica

inputs = input("Ingrese los valores (a, b, c): ")  # solicitudes
inputs_sep = inputs.split(',')  # sistema de autocumplimiento de entradas
if len(inputs_sep) == 3:
    a0, b0, c0 = inputs_sep[:3]
    a0 = int(a0.strip())
    b0 = int(b0.strip())
    c0 = int(c0.strip())
    print("Raíz 1 = " + str(x1(a0, b0, c0)))  # llamar definición
    print("Raíz 2 = " + str(x2(a0, b0, c0)))  # llamar definición
    print("Discriminante = " + str(det(a0, b0, c0)))  # llamar definición
else:
    print("Debe ingresar 3 valores.")  # error
