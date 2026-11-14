"""
Ejercicio: Una plataforma de comercio electrónico requiere ordenar los precios (en dólares) de un catálogo de artículos: [64, 25, 12, 22, 11].
 El algoritmo busca repetidamente el precio mínimo de la porción no ordenada y lo intercambia con la primera posición disponible.
"""
def ordenamientoPorSeleccion(arr):
    n = len(arr)
    for i in range(n):
       
        indice_minimo = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
          
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

precios_catalogo = [64, 25, 12, 22, 11]
ordenamientoPorSeleccion(precios_catalogo)
print("3. Ordenamiento por Selección:", precios_catalogo)
