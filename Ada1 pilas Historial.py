class Pila:
    def __init__(self):
        self.items = []

    def push(self, elemento):         
        self.items.append(elemento)

    def pop(self):                    
        if self.esta_vacia():
            return None
        return self.items.pop()

    def peek(self):                   
        if self.esta_vacia():
            return None
        return self.items[-1]

    def esta_vacia(self):
        return len(self.items) == 0

    def tamanio(self):
        return len(self.items)

    def listar(self):                  
        return self.items[::-1]


class Navegador:
    def __init__(self):
        self.atras = Pila()
        self.adelante = Pila()
        self.actual = None

    def visitar(self, sitio):
        if self.actual is not None:
            self.atras.push(self.actual)
        self.actual = sitio
        self.adelante = Pila()         

    def regresar(self):
        if self.atras.esta_vacia():
            return False
        self.adelante.push(self.actual)
        self.actual = self.atras.pop()
        return True

    def avanzar(self):
        if self.adelante.esta_vacia():
            return False
        self.atras.push(self.actual)
        self.actual = self.adelante.pop()
        return True

    def mostrar_historial(self):
        if self.actual is None:
            print("El historial está vacío.")
            return
        print(f"Página actual: {self.actual}")
        print("Atrás (de más reciente a más vieja):", self.atras.listar())
        print("Adelante:", self.adelante.listar())

    def limpiar(self):
        self.atras = Pila()
        self.adelante = Pila()
        self.actual = None


def menu():
    nav = Navegador()
    while True:
        print("\n--- NAVEGADOR ---")
        print("1. Visitar sitio")
        print("2. Regresar")
        print("3. Avanzar")
        print("4. Ver historial")
        print("5. Limpiar historial")
        print("6. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            sitio = input("Escribe el sitio: ").strip()
            if sitio:
                nav.visitar(sitio)
                print(f"Visitando {sitio}")
            else:
                print("No escribiste nada.")
        elif opcion == "2":
            if nav.regresar():
                print(f"Regresaste a {nav.actual}")
            else:
                print("No hay páginas anteriores.")
        elif opcion == "3":
            if nav.avanzar():
                print(f"Avanzaste a {nav.actual}")
            else:
                print("No hay páginas adelante.")
        elif opcion == "4":
            nav.mostrar_historial()
        elif opcion == "5":
            nav.limpiar()
            print("Historial borrado.")
        elif opcion == "6":
            print("Hasta luego")
            break
        else:
            print("Opción inválida.")


menu()