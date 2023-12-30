# Interés Compuesto
## $$M = VP \left(1 + \frac{ip}{n}\right)^{n}$$
Esta fórmula permite calcular el monto final después de un periodo de tiempo, incluyendo tanto el capital inicial como los intereses generados y acumulados.
```
# función


def monto(vp, ip, n):
    return (((1 + (ip / 100)) ** (12 * n)) - 1) * vp


# entradas

entradas = input("(Valor presente, Tasa de interés (%), Períodos): ")
entradas0 = entradas.split(',')
if len(entradas0) == 3:
    vp0, ip0, n0 = entradas0[:3]
    vp0 = float(vp0.strip())
    ip0 = float(ip0.strip())
    n0 = float(n0.strip())
    print("El interés ganado asciende a $" + str(round(monto(vp0, ip0, n0), 2)))
else:
    print("Debe ingresar 3 valores.")
