"""
Ejercicio: Un sistema de inventario necesita ordenar los códigos numéricos de una 
 serie de productos que llegaron al almacén: [54, 26, 93, 17, 77, 31, 44, 55, 20]. 
 Se utiliza la versión optimizada ("burbuja corto") documentada en el libro oficial, 
la cual detiene el algoritmo si detecta que la lista ya quedó ordenada antes de terminar todas las pasadas 
"""
def ordenamientoBurbujaCorto(unaLista):
    intercambios = True
    numPasada = len(unaLista) - 1
    while numPasada > 0 and intercambios:
        intercambios = False
        for i in range(numPasada):
            if unaLista[i] > unaLista[i + 1]:
                intercambios = True
                unaLista[i], unaLista[i + 1] = unaLista[i + 1], unaLista[i]
        numPasada = numPasada - 1


codigos_productos = [54, 26, 93, 17, 77, 31, 44, 55, 20]
ordenamientoBurbujaCorto(codigos_productos)
print("1. Ordenamiento Burbuja:", codigos_productos)
#