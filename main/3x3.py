import numpy as np  # importar biblioteca "NumPy"


coefficients = []  # establecer tupla de coeficientes
for i in range(3):  # repetir 3 veces
    equation_coeffs = input(f"Ingrese los coeficientes de la ecuación {i + 1} separados por espacios: ")  # solicitudes
    coefficients.append([float(x) for x in equation_coeffs.split()])  # agregar valores insertados por el usuario a la tupla


matrix = np.array(coefficients)  # convertir tupla a lista de NumPy


results = []  # establecer tupla de resultados
for i in range(3):  # repetir 3 veces
    result = float(input(f"Ingrese el resultado de la ecuación {i + 1}: "))  # solicitudes
    results.append(result)  # calcular


vector_results = np.array(results)  # establecer la lista de NumPy en una variable legible


solution = np.linalg.solve(matrix, vector_results)  # establecer resultados legibles


print("\nLa solución para las variables x, y, z es:")  # imprimir soluciones
print(f"x = {round(solution[0], 4)}")  # sol{1}
print(f"y = {round(solution[1], 4)}")  # sol{2}
print(f"z = {round(solution[2], 4)}")  # sol{3}
