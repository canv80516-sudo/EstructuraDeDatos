
def mezclar(lista, inicio, mitad, fin):
    izquierda = lista[inicio:mitad]
    derecha = lista[mitad:fin]

    i = 0
    j = 0
    k = inicio

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            lista[k] = izquierda[i]
            i = i + 1
        else:
            lista[k] = derecha[j]
            j = j + 1
        k = k + 1

    while i < len(izquierda):
        lista[k] = izquierda[i]
        i = i + 1
        k = k + 1

    while j < len(derecha):
        lista[k] = derecha[j]
        j = j + 1
        k = k + 1


def mezclaDirecta(unaLista):
    tamaño = 1
    n = len(unaLista)
    pasada = 1

    while tamaño < n:
        print("\nPasada", pasada)
        inicio = 0

        while inicio < n:
            mitad = min(inicio + tamaño, n)
            fin = min(inicio + 2 * tamaño, n)

            if mitad < fin:
                print("Dividir:", unaLista[inicio:mitad],
                      unaLista[mitad:fin])

                mezclar(unaLista, inicio, mitad, fin)

                print("Mezclar:", unaLista[inicio:fin])

            inicio = inicio + 2 * tamaño

        tamaño = tamaño * 2
        pasada = pasada + 1

    return unaLista


unaLista = [54, 26, 93, 17, 77, 31, 44, 55, 20]

print("Lista original:", unaLista)

mezclaDirecta(unaLista)

print("\nLista ordenada:", unaLista)
