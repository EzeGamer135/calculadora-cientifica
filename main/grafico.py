import matplotlib.pyplot as plt
import pandas as pd


def graficar(tipo_grafica, tipo_eje_x):
    # editar categorías
    lista = []
    # editar valores respectivamente de sus categorías
    vals = []
    
    if tipo_grafica == 'linea':
        if tipo_eje_x == 'fechas':
            x = pd.date_range('20230101', periods=10)
        else:
            x = list(range(10))

        y = [3, 7, 2, 5, 8, 4, 6, 1, 9, 10]

        plt.figure(figsize=(8, 6))
        plt.plot(x, y)
        plt.title('Gráfica de Línea')
        plt.xlabel('Fechas' if tipo_eje_x == 'fechas' else 'Números')
        plt.ylabel('Valores')
        plt.grid(True)
        plt.show()

    elif tipo_grafica == 'circular':
        labels = lista
        sizes = vals

        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Gráfica Circular')
        plt.show()

    elif tipo_grafica == 'barras':
        categories = lista
        values = vals

        plt.figure(figsize=(8, 6))
        plt.bar(categories, values)
        plt.title('Gráfica de Barras')
        plt.xlabel('Categorías')
        plt.ylabel('Valores')
        plt.show()

    else:
        print('Tipo de gráfica no válido. Por favor, elige entre "linea", "circular" o "barras".')

tipo_grafica_elegida = input('Elige el tipo de gráfica (linea, circular o barras): ').lower()

if tipo_grafica_elegida == 'linea':
    tipo_eje_x_elegido = input('Elige el tipo de eje X (fechas o numeros): ').lower()
    graficar(tipo_grafica_elegida, tipo_eje_x_elegido)
else:
    graficar(tipo_grafica_elegida, None)
