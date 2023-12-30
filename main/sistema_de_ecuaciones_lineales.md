# Sistema de ecuaciones lineales
![Sistema de ecuaciones lineales](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPV3zbGnABP6IkJglHE7tyW6WQWDuW9riTL9K0q92r9m1BoNlfjV5aFR6YozqN2hkfzA&usqp=CAU)
```
import numpy as np


coefficients = []
for i in range(3):
    equation_coeffs = input(f"Ingrese los coeficientes de la ecuación {i + 1} separados por espacios: ")
    coefficients.append([float(x) for x in equation_coeffs.split()])


matrix = np.array(coefficients)


results = []
for i in range(3):
    result = float(input(f"Ingrese el resultado de la ecuación {i + 1}: "))
    results.append(result)


vector_results = np.array(results)


solution = np.linalg.solve(matrix, vector_results)


print("\nLa solución para las variables x, y, z es:")
print(f"x = {round(solution[0], 4)}")
print(f"y = {round(solution[1], 4)}")
print(f"z = {round(solution[2], 4)}")
