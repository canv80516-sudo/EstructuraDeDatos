NUM_MESES = 12
NUM_DEPARTAMENTOS = 3

MESES = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

DEPARTAMENTOS = ["Ropa", "Deportes", "Jugueteria"]


def crear_matriz():
    """Crea la matriz de 12 meses x 3 departamentos, iniciada en 0."""
    matriz = [[0 for _ in range(NUM_DEPARTAMENTOS)] for _ in range(NUM_MESES)]
    return matriz


def insertar_venta(matriz, mes, departamento, cantidad):
    """Inserta (o actualiza) una venta en un mes y departamento especifico."""
    if 0 <= mes < NUM_MESES and 0 <= departamento < NUM_DEPARTAMENTOS:
        matriz[mes][departamento] = cantidad
        print(f"Venta registrada: {MESES[mes]} - {DEPARTAMENTOS[departamento]}: {cantidad}")
        return True
    print("Datos invalidos: mes o departamento fuera de rango")
    return False


def buscar_venta(matriz, valor_buscar):
    """Busca todas las coincidencias de un valor de venta en la matriz."""
    coincidencias = []
    for m in range(NUM_MESES):
        for d in range(NUM_DEPARTAMENTOS):
            if matriz[m][d] == valor_buscar:
                coincidencias.append({
                    "mes": MESES[m],
                    "departamento": DEPARTAMENTOS[d],
                    "valor": matriz[m][d]
                })
    return coincidencias


def eliminar_venta(matriz, mes, departamento):
    """Elimina una venta en particular (la regresa a 0)."""
    return insertar_venta(matriz, mes, departamento, 0)


def mostrar_matriz(matriz):
    """Imprime la matriz completa de forma legible."""
    for m in range(NUM_MESES):
        print(f"{MESES[m]}: {matriz[m]}")


def pedir_mes():
    """Muestra la lista de meses y pide al usuario que elija uno."""
    for i, nombre in enumerate(MESES):
        print(f"{i}: {nombre}")
    return int(input("Elige el numero de mes: "))


def pedir_departamento():
    """Muestra la lista de departamentos y pide al usuario que elija uno."""
    for i, nombre in enumerate(DEPARTAMENTOS):
        print(f"{i}: {nombre}")
    return int(input("Elige el numero de departamento: "))


def menu():
    ventas = crear_matriz()

    while True:
        print("\n--- Menu de Ventas ---")
        print("1. Insertar venta")
        print("2. Buscar venta")
        print("3. Eliminar venta")
        print("4. Ver matriz completa")
        print("5. Salir")
        opcion = input("Elige una opcion: ")

        match opcion:
            case "1":
                mes = pedir_mes()
                depto = pedir_departamento()
                cantidad = int(input("Cantidad de venta: "))
                insertar_venta(ventas, mes, depto, cantidad)

            case "2":
                valor = int(input("Valor de venta a buscar: "))
                resultados = buscar_venta(ventas, valor)
                if resultados:
                    print("Coincidencias encontradas:")
                    for r in resultados:
                        print(r)
                else:
                    print("No se encontraron coincidencias.")

            case "3":
                mes = pedir_mes()
                depto = pedir_departamento()
                eliminar_venta(ventas, mes, depto)

            case "4":
                mostrar_matriz(ventas)

            case "5":
                print("Saliendo del programa...")
                break

            case _:
                print("Opcion invalida, intenta de nuevo.")


if __name__ == "__main__":
    menu()