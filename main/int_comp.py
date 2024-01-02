# función


def monto(vp, ip, n):  # definir monto
    return (((1 + (ip / 100)) ** (12 * n)) - 1) * vp  # crear cálculo

# entradas

entradas = input("Valores establecidos (Valor presente, Tasa de interés (%), Períodos): ")  # solicitudes
entradas0 = entradas.split(',')  # sistema de autocumplimiento de entradas
if len(entradas0) == 3:
    vp0, ip0, n0 = entradas0[:3]
    vp0 = float(vp0.strip())
    ip0 = float(ip0.strip())
    n0 = float(n0.strip())
    print("El interés ganado asciende a $" + str(round(monto(vp0, ip0, n0), 2)))  # imprimir definición
else:
    print("Debe ingresar 3 valores.")  # error
