# funciones


def add(a, b):  # suma
    return a + b


def res(a, b):  # resta
    return a - b


def mul(a, b):  # multiplicación
    return a * b


def div(a, b):  # división
    if b == 0:
        print("No se puede dividir entre cero.")
    else:
        return a / b


def av(a, b):  # promedio
    return (a + b) / 2

# entradas y lógica

entradas = input("(Operación [add, res, mul, div, av]), (Valor 1), (Valor 2): ")
entradas0 = entradas.split(',')
if len(entradas0) == 3:
    choice, a0, b0 = entradas0[:3]
    choice = choice.strip()
    a0 = float(a0.strip())
    b0 = float(b0.strip())
    if choice == "add":
        print(round(add(a0, b0), 5))
    elif choice == "res":
        print(round(res(a0, b0), 5))
    elif choice == "mul":
        print(round(mul(a0, b0), 5))
    elif choice == "div":
        print(round(div(a0, b0), 5))
    elif choice == "av":
        print(round(av(a0, b0), 5))
    else:
        print("Valor no permitido.")
else:
    print("Debe ingresar 3 valores.")
