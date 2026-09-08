import random
import statistics

# 1. Generar 50 números aleatorios entre 1 y 100
numeros = [random.randint(150, 250) for _ in range(50)]

# 2. Cálculos estadísticos con el módulo estándar 'statistics'
media = statistics.mean(numeros)
mediana = statistics.median(numeros)
moda = statistics.multimode(numeros)  # Devuelve todas las modas si hay más de una

var_muestral = statistics.variance(numeros)
var_poblacional = statistics.pvariance(numeros)

std_muestral = statistics.stdev(numeros)
std_poblacional = statistics.pstdev(numeros)

# 3. Imprimir resultados
print("Lista de números:", numeros)
print(f"Media: {media:.2f}")
print(f"Mediana: {mediana:.2f}")
print(f"Moda: {moda}")
print(f"Varianza muestral (s²): {var_muestral:.2f}")
print(f"Varianza poblacional (σ²): {var_poblacional:.2f}")
print(f"Desviación estándar muestral (s): {std_muestral:.2f}")
print(f"Desviación estándar poblacional (σ): {std_poblacional:.2f}") 