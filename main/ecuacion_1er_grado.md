# Ecuación de primer Grado
## $$a(b)c=x$$
```
# función

def ecu(a, b, c, x):  # 'x' es el número a la derecha de la igualdad
    if a == 0:  # 'a' no existe

        if c == 0:  # 'c' no existe
            return x / b
        else:  # 'c' existe
            if c < 0:  # 'c' es menor que 0
                return (x + c) / b
            else:  # 'c' es mayor que 0
                return (x - c) / b
    else:
        if a < 0:  # 'a' es menor que 0
            if c == 0:  # 'c' no existe

                return (x + a) / b
            elif c < 0:  # 'c' es menor que 0
                return (x + a + c) / b
            else:  # 'c' es mayor que 0
                return (x + a - c) / b

        else:  # 'a' es mayor que 0
            if c == 0:  # 'c' no existe
                return (x - a) / b

            elif c < 0:  # 'c' es menor que 0
                return (x - a + c) / b
            else:  # 'c' es mayor que 0
                return (x - a - c) / b


# entradas

entradas = input("(a, b(x), c, x): ")
entradas0 = entradas.split(',')
if len(entradas0) == 4:
    a0, b0, c0, x0 = entradas0[:4]
    a0 = int(a0.strip())
    b0 = int(b0.strip())
    c0 = int(c0.strip())
    x0 = int(x0.strip())
    print("b = " + str(float(ecu(a0, b0, c0, x0))))
else:
    print("Debe ingresar 4 valores.")
