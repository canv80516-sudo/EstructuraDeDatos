"""
Ejercicio: Una estación meteorológica registra las temperaturas máximas (en °C) de distintos días en una lista: [29, 10, 14, 37, 13].
El sistema debe insertar cada nueva medición en la sublista ordenada manteniendo los registros de menor a mayor.
"""
def ordenamientoPorInsercion(unaLista):
    for indice in range(1, len(unaLista)):
        valorActual = unaLista[indice]
        posicion = indice

        while posicion > 0 and unaLista[posicion - 1] > valorActual:
            unaLista[posicion] = unaLista[posicion - 1]
            posicion = posicion - 1

        unaLista[posicion] = valorActual


temperaturas = [29, 10, 14, 37, 13]
ordenamientoPorInsercion(temperaturas)
print("2. Ordenamiento por Inserción:", temperaturas)
