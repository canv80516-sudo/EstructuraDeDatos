
def intercalacion(lista1, lista2):
    resultado = []
    i = 0
    j = 0

    
    while i < len(lista1) and j < len(lista2):
        if lista1[i] <= lista2[j]:
            resultado.append(lista1[i])
            i += 1
        else:
            resultado.append(lista2[j])
            j += 1

    # Agregar los elementos restantes de lista1
    while i < len(lista1):
        resultado.append(lista1[i])
        i += 1

    # Agregar los elementos restantes de lista2
    while j < len(lista2):
        resultado.append(lista2[j])
        j += 1

    return resultado



lista1 = [60, 70, 80, 90]
lista2 = [65, 75, 85, 95]

resultado = intercalacion(lista1, lista2)

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Lista intercalada:", resultado)
