
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ListaIngredientes:
    def __init__(self):
        self.primero = None

    def insertar_final(self, ingrediente):
        nuevo = Nodo(ingrediente)

        if self.primero is None:
            self.primero = nuevo
            return

        actual = self.primero
        while actual.siguiente is not None:
            actual = actual.siguiente

        actual.siguiente = nuevo

    def esta_vacia(self):
        return self.primero is None

    def contiene(self, ingrediente):
        actual = self.primero
        while actual is not None:
            if actual.dato.lower() == ingrediente.lower():
                return True
            actual = actual.siguiente
        return False

    def mostrar(self):
        actual = self.primero

        if actual is None:
            print("No hay ingredientes registrados.")
            return

        while actual is not None:
            print(f"- {actual.dato}")
            actual = actual.siguiente


class Postre:
    def __init__(self, nombre):
        self.nombre = nombre.strip()
        self.ingredientes = ListaIngredientes()

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.insertar_final(ingrediente.strip())


class ListaArreglo:
    def __init__(self):
        self.datos = []
        self.tamanio = 0

    def esta_vacia(self):
        return self.tamanio == 0

    def insertar_final(self, postre):
        self.datos.append(postre)
        self.tamanio += 1

    def alta_postre(self, postre):
        # Permite registrar postres con el mismo nombre.
        # Se mantiene el arreglo ordenado alfabéticamente.
        posicion = 0

        while posicion < self.tamanio:
            if self.datos[posicion].nombre.lower() > postre.nombre.lower():
                break
            posicion += 1

        self.datos.insert(posicion, postre)
        self.tamanio += 1
        print(f"Postre '{postre.nombre}' registrado correctamente.")

    def baja_postre(self, nombre):
        for i in range(self.tamanio):
            if self.datos[i].nombre.lower() == nombre.strip().lower():
                eliminado = self.datos.pop(i)
                self.tamanio -= 1
                print(f"Postre '{eliminado.nombre}' eliminado correctamente.")
                return eliminado

        print("No se encontró el postre.")
        return None

    def eliminar(self, posicion):
        if posicion < 0 or posicion >= self.tamanio:
            return None

        eliminado = self.datos.pop(posicion)
        self.tamanio -= 1
        return eliminado

    def ordenar(self):
        self.datos.sort(key=lambda postre: postre.nombre.lower())

    def buscar(self, nombre):
        encontrados = []

        for postre in self.datos:
            if postre.nombre.lower() == nombre.strip().lower():
                encontrados.append(postre)

        return encontrados

    def mostrar_todos(self):
        if self.esta_vacia():
            print("No hay postres registrados.")
            return

        for i, postre in enumerate(self.datos, start=1):
            print(f"{i}. {postre.nombre}")


def pedir_ingredientes(postre):
    print("Escribe los ingredientes del postre.")
    print("Escribe 'fin' para terminar.")

    while True:
        ingrediente = input("Ingrediente: ").strip()

        if ingrediente.lower() == "fin":
            break

        if ingrediente:
            postre.agregar_ingrediente(ingrediente)



def agregar_ingredientes_postre(postres):
    if postres.esta_vacia():
        print("No hay postres registrados.")
        return

    nombre = input("Nombre del postre al que deseas agregar ingredientes: ").strip()
    encontrados = postres.buscar(nombre)

    if not encontrados:
        print("No se encontró ese postre.")
        return

    if len(encontrados) > 1:
        print("Hay varios postres con ese nombre.")
        print("Se agregarán los ingredientes al primer registro encontrado.")

    postre = encontrados[0]

    print(f"\nPostre seleccionado: {postre.nombre}")
    print("Ingresa los nuevos ingredientes.")
    print("Escribe 'fin' para terminar.")

    while True:
        ingrediente = input("Nuevo ingrediente: ").strip()

        if ingrediente.lower() == "fin":
            break

        if ingrediente:
            postre.agregar_ingrediente(ingrediente)
            print(f"Ingrediente '{ingrediente}' agregado.")



def menu():
    postres = ListaArreglo()

    while True:
        print("\n========== MENÚ DE POSTRES ==========")
        print("1. Mostrar ingredientes de un postre")
        print("2. Buscar postre")
        print("3. Mostrar ingredientes de todos los postres")
        print("4. Mostrar postres que contienen un ingrediente")
        print("5. Alta de postre")
        print("6. Baja de postre")
        print("7. Ordenar postres")
        print("8. Mostrar todos los postres")
        print("9.Agregar ingredientes a un postre existente.")
        print("10. Eliminar postres repetidos")
        print("0. Salir")
        print("=====================================")

        try:
            opcion = int(input("Selecciona una opción: "))
        except ValueError:
            print("Ingresa un número válido.")
            continue

        if opcion == 0:
            print("Programa finalizado.")
            break

        elif opcion == 1:
            nombre = input("Nombre del postre: ").strip()
            encontrados = postres.buscar(nombre)

            if not encontrados:
                print("No se encontró el postre.")
            else:
                for postre in encontrados:
                    print(f"\nIngredientes de {postre.nombre}:")
                    postre.ingredientes.mostrar()

        elif opcion == 2:
            nombre = input("Nombre del postre que deseas buscar: ").strip()
            encontrados = postres.buscar(nombre)

            if encontrados:
                print(f"Se encontraron {len(encontrados)} registro(s):")
                for postre in encontrados:
                    print(f"\nPostre: {postre.nombre}")
                    postre.ingredientes.mostrar()
            else:
                print("No se encontró el postre.")

        elif opcion == 3:
            if postres.esta_vacia():
                print("No hay postres registrados.")
            else:
                for postre in postres.datos:
                    print(f"\nIngredientes de {postre.nombre}:")
                    postre.ingredientes.mostrar()

        elif opcion == 4:
            ingrediente = input("Ingrediente que deseas buscar: ").strip()
            encontrados = []

            for postre in postres.datos:
                if postre.ingredientes.contiene(ingrediente):
                    encontrados.append(postre.nombre)

            if encontrados:
                print("Postres que contienen ese ingrediente:")
                for nombre in encontrados:
                    print(f"- {nombre}")
            else:
                print("Ningún postre contiene ese ingrediente.")

        elif opcion == 5:
            nombre = input("Nombre del postre: ").strip()

            if not nombre:
                print("El nombre no puede estar vacío.")
                continue

            nuevo_postre = Postre(nombre)
            pedir_ingredientes(nuevo_postre)
            postres.alta_postre(nuevo_postre)

        elif opcion == 6:
            nombre = input("Nombre del postre que deseas eliminar: ").strip()
            postres.baja_postre(nombre)

        elif opcion == 7:
            postres.ordenar()
            print("Postres ordenados alfabéticamente.")

        elif opcion == 8:
            postres.mostrar_todos()

        elif opcion == 9:
         agregar_ingredientes_postre(postres)

        elif opcion == 10:
            from Ejer2Postres import eliminar_repetidos

            eliminados = eliminar_repetidos(postres)
            if eliminados > 0:
                print(f"Total de postres repetidos eliminados: {eliminados}")

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()



