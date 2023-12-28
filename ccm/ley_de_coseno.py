from math import *

# función


def coseno(b, c, A):
    return sqrt((b ** 2 + c ** 2) - (2 * b * c * cos(A)))
# entradas

inputs = input("Valores establecidos (lado b, lado c, ángulo A): ")
inputs_sep = inputs.split(',')
if len(inputs_sep) == 3:
    b0, c0, A0 = inputs_sep[:3]
    b0 = int(b0.strip())
    c0 = int(c0.strip())
    A0 = int(A0.strip())
    print("Lado A = " + str(round(coseno(b0, c0, A0), 4)))
else:
    print("Debe ingresar 3 valores.")
