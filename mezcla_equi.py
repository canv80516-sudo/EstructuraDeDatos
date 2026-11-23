
def obtenerSecuencias(unaLista):
    secuencias = []

    if len(unaLista) == 0:
        return secuencias

    secuencia = [unaLista[0]]

  
    for i in range(1, len(unaLista)):
        if unaLista[i] >= unaLista[i - 1]:
            secuencia.append(unaLista[i])
        else:
            secuencias.append(secuencia)
            secuencia = [unaLista[i]]

    secuencias.append(secuencia)

    print("Particion:", secuencias)
    return secuencias


def intercalar(izquierda, derecha):
    resultado = []
    i = 0
    j = 0

    print("Dividir:", izquierda, derecha)

    
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:
            resultado.append(izquierda[i])
            i = i + 1
        else:
            resultado.append(derecha[j])
            j = j + 1

    
    while i < len(izquierda):
        resultado.append(izquierda[i])
        i = i + 1

    while j < len(derecha):
        resultado.append(derecha[j])
        j = j + 1

    print("Mezclar:", resultado)
    return resultado


def mezclaEquilibrada(unaLista):
    secuencias = obtenerSecuencias(unaLista)

    # Fusionar las secuencias
    while len(secuencias) > 1:
        nuevasSecuencias = []

        for i in range(0, len(secuencias), 2):
            if i + 1 < len(secuencias):
                resultado = intercalar(
                    secuencias[i], secuencias[i + 1]
                )
                nuevasSecuencias.append(resultado)
            else:
                nuevasSecuencias.append(secuencias[i])

        secuencias = nuevasSecuencias
        print("Nueva particion:", secuencias)

    if len(secuencias) == 0:
        return []

    return secuencias[0]



unaLista = [9, 75, 14, 68, 29, 17, 31, 25, 4, 5, 13, 18, 72, 46, 61]

print("Lista original:", unaLista)

resultado = mezclaEquilibrada(unaLista)

print("Lista ordenada:", resultado)
