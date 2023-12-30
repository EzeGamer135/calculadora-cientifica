# Fórmula cuadrática ([Bhaskara](https://es.wikipedia.org/wiki/Ecuación_de_segundo_grado))
## $$ax^2+bx+c=0\iff a\neq 0$$
## $$x=\frac{-b±\sqrt{b^2-4ac}}{2a}$$
```
from math import sqrt

# funciones


def x1(a, b, c):
    discriminante = b ** 2 - 4 * a * c
    if discriminante < 0:
        return "∆ < 0"
    else:
        return (-b + sqrt(discriminante)) / (2 * a)


def x2(a, b, c):
    discriminante = b ** 2 - 4 * a * c
    if discriminante < 0:
        return "∆ < 0"
    else:
        return (-b - sqrt(discriminante)) / (2 * a)


def det(a, b, c):
    discriminante = b ** 2 - 4 * a * c
    return discriminante


# entradas y lógica

inputs = input("(a, b, c): ")
inputs_sep = inputs.split(',')
if len(inputs_sep) == 3:
    a0, b0, c0 = inputs_sep[:3]
    a0 = int(a0.strip())
    b0 = int(b0.strip())
    c0 = int(c0.strip())
    print("Raíz 1 = " + str(x1(a0, b0, c0)))
    print("Raíz 2 = " + str(x2(a0, b0, c0)))
    print("Discriminante = " + str(det(a0, b0, c0)))
else:
    print("Debe ingresar 3 valores.")
