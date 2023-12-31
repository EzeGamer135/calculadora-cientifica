# Sistema gráfico
## Ejemplos
### Lineal
![image](https://github.com/EzeGamer135/calculadora-cientifica/assets/73393487/c5f4750a-64fc-4b26-9b15-2d1cfc6598cc)
### Circular
![image](https://github.com/EzeGamer135/calculadora-cientifica/assets/73393487/267fcedf-7e7f-468f-b3bf-ee933ac232c3)
### Barras
![image](https://github.com/EzeGamer135/calculadora-cientifica/assets/73393487/a912a781-9fe7-4b60-a4ad-5d441f7862e2)
```
import matplotlib.pyplot as plt
import pandas as pd


def graficar(tipo_grafica, tipo_eje_x):
    lista = []    # editar categorías
    vals = []    # editar valores respectivamente a sus categorías
    
    if tipo_grafica == 'linea':
        if tipo_eje_x == 'fechas':
            x = pd.date_range('20230101', periods=10)    # edita la centidad de días en la sección 'periods=10' y la fecha de inicio del gráfico en '20230101' en formato AAAAMMDD
        else:
            x = list(range(10))
        y = [3, 7, 2, 5, 8, 4, 6, 1, 9, 10]    # edita los valores del gráfico (la cantidad de valores coincidir con el valor insertado en 'periods=10')

        plt.figure(figsize=(13, 6))
        plt.plot(x, y)
        plt.title('Gráfica')    # editar título del gráfico
        plt.xlabel('Fecha' if tipo_eje_x == 'fechas' else 'Iteraciones')
        plt.ylabel('Valores')    # editar etiqueta del eje Y
        plt.grid(True)    # 'true' para activar cuadrícula, 'false' para desactivarla
        plt.show()

    elif tipo_grafica == 'circular':
        labels = lista
        sizes = vals

        plt.figure(figsize=(8, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%')
        plt.title('Gráfica')    # editar título del gráfico
        plt.show()

    elif tipo_grafica == 'barras':
        categories = lista
        values = vals

        plt.figure(figsize=(8, 6))
        plt.bar(categories, values)
        plt.title('Gráfica')    # editar título del gráfico
        plt.xlabel('Categorías')    # editar etiqueta del eje X
        plt.ylabel('Valores')    # editar etiqueta del eje Y
        plt.show()

    else:
        print('Tipo de gráfica no válido. Por favor, elige entre "linea", "circular" o "barras".')

tipo_grafica_elegida = input('Elige el tipo de gráfica (linea, circular o barras): ').lower()

if tipo_grafica_elegida == 'linea':
    tipo_eje_x_elegido = input('Elige el tipo de eje X (fecha o iteraciones): ').lower()
    graficar(tipo_grafica_elegida, tipo_eje_x_elegido)
else:
    graficar(tipo_grafica_elegida, None)
```
