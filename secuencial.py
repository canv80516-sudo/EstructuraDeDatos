
# BUSQUEDA SECUENCIAL: BIBLIOTECA

libros = [
    "Cien años de soledad",
    "El principito",
    "Don Quijote",
    "Harry Potter",
    "La metamorfosis",
    "Orgullo y prejuicio",
    "Los juegos del hambre",
    "Coraline"
]

def buscar_libro(lista, nombre):

    for i in range(len(lista)):

        if lista[i].lower() == nombre.lower():
            return i

    return -1


print("=== BUSQUEDA DE LIBROS ===")

print("\nLibros disponibles:")
for libro in libros:
    print("-", libro)

nombre = input("\nIngrese el nombre del libro: ")

resultado = buscar_libro(libros, nombre)

if resultado != -1:

    print("\nLibro encontrado:", libros[resultado])
    print("Posicion:", resultado + 1)

else:

    print("\nEl libro no se encuentra en la biblioteca.")
