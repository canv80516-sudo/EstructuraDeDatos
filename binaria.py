
# BUSQUEDA BINARIA: MATRICULAS

matriculas = [
    1001, 1005, 1010, 1015, 1020,
    1025, 1030, 1035, 1040, 1045,
    1050, 1055, 1060, 1065, 1070
]

def buscar_matricula(lista, buscado):

    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:

        medio = (izquierda + derecha) // 2

        if lista[medio] == buscado:
            return medio

        elif buscado < lista[medio]:
            derecha = medio - 1

        else:
            izquierda = medio + 1

    return -1


print("=== BUSQUEDA BINARIA ===")

print("\nMatriculas disponibles:")
print(matriculas)

try:

    numero = int(input("\nIngrese la matricula a buscar: "))

    resultado = buscar_matricula(matriculas, numero)

    if resultado != -1:

        print("\nMatricula encontrada:", matriculas[resultado])
        print("Posicion:", resultado + 1)

    else:

        print("\nLa matricula no se encuentra registrada.")

except ValueError:

    print("\nError: ingrese una matricula numerica.")
