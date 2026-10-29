
def eliminar_repetidos(postres):

    if postres.esta_vacia():
        print("Error: no hay postres registrados.")
        return 0

  
    postres.ordenar()

    eliminados = 0
    i = 0

    while i < postres.tamanio - 1:
        actual = postres.datos[i]
        siguiente = postres.datos[i + 1]

        if actual.nombre == siguiente.nombre:
            repetido = postres.eliminar(i + 1)

            if repetido is not None:
                print(
                    f"Postre repetido eliminado: "
                    f"{repetido.nombre.title()}"
                )
                eliminados += 1

           
        else:
            i += 1

    if eliminados == 0:
        print("No se encontraron postres repetidos.")

    return eliminados

