# funciones


def intg(x, n):  # definir integral
    res = x ** (n + 1) / (n + 1)  # crear cálculo
    print("∫" + str(x) + "x ^" + str(n) + " = " + str(res))  # imprimir resultado

# entradas y lógica

entradas = input("Entradas (x, n(potencia)): ")  # solicitudes
entradas0 = entradas.split(',')  # sistema de autocumplimiento de entradas
if len(entradas0) == 2:
    x0, n0 = entradas0[:2]
    x0 = int(x0.strip())
    n0 = int(n0.strip())
    print(intg(x0, n0))  # imprimir definición
else:
    print("Debe ingresar 3 valores.")  # error
