# funciones


def deriv(x, n):  # definir derivada
    res1 = x * n  # crear cálculo 1
    res2 = n - 1  # crear cálculo 2
    print("y' = (" + str(x) + " * " + str(n) + ") ^(" + str(x) + " - 1) = " + str(res1) + " ^" + str(res2))  # imprimir resultado

# entradas y lógica

entradas = input("Entradas (x, n(potencia)): ")  # solicitudes
entradas0 = entradas.split(',')  # sistema de autocumplimiento de entradas
if len(entradas0) == 2:
    x0, n0 = entradas0[:2]
    x0 = int(x0.strip())
    n0 = int(n0.strip())
    print(deriv(x0, n0))  # imprimir definición
else:
    print("Debe ingresar 3 valores.")  # error
