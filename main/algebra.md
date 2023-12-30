# Álgebra básica
## $$\int x(x)^n=\frac{x^{n+1}}{n+1}$$ $$y'=xn^{x-1}$$
```
# funciones


def intg(x, n):  # integral
    res = x ** (n + 1) / (n + 1)
    print("∫" + str(x) + "x ^" + str(n) + " = " + str(res))


def deriv(x, n):  # derivada
    res1 = x * n
    res2 = n - 1
    print("y' = (" + str(x) + " * " + str(n) + ") ^(" + str(x) + " - 1) = " + str(res1) + " ^" + str(res2))

# entradas y lógica

entradas = input("(Operación [intg, deriv], x, potencia): ")
entradas0 = entradas.split(',')
if len(entradas0) == 3:
    choice, x0, n0 = entradas0[:3]
    choice = choice.strip()
    x0 = int(x0.strip())
    n0 = int(n0.strip())
    if choice == "intg":
        print(intg(x0, n0))
    elif choice == "deriv":
        print(deriv(x0, n0))
    else:
        print("Valor no permitido.")
else:
    print("Debe ingresar 3 valores.")
