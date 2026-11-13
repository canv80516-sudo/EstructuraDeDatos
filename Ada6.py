import io
import contextlib
from collections import deque


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierdoPtr = None
        self.derechoPtr = None



class Arbol:

    def __init__(self):
        self.__raizPtr = None

    

    def esVacio(self):
        return self.__raizPtr is None

    def insertarNodo(self, valor):
        if self.buscar(valor):
            return False

        self.__raizPtr = self.__insertar(self.__raizPtr, valor)
        return True

    def __insertar(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)

        if valor < nodo.dato:
            nodo.izquierdoPtr = self.__insertar(
                nodo.izquierdoPtr, valor
            )
        else:
            nodo.derechoPtr = self.__insertar(
                nodo.derechoPtr, valor
            )

        return nodo

    #  INSERTAR A LA IZQUIERDA O DERECHA 

    def insertarHijo(self, padreValor, lado, valor):

        if self.buscar(valor):
            return False, f"El {valor} ya existe. No se permiten repetidos."

        if self.esVacio():
            return False, "El árbol está vacío. Primero inserta la raíz."

        actual = self.__raizPtr

        # Buscar al padre siguiendo las reglas del ABB
        while actual is not None and actual.dato != padreValor:
            if valor < actual.dato:
                actual = actual.izquierdoPtr
            else:
                actual = actual.derechoPtr

        if actual is None:
            return False, (
                f"No se puede insertar {valor} debajo de {padreValor}: "
                "ese nodo no está en la ruta correspondiente del ABB."
            )

        debeIr = "izquierda" if valor < padreValor else "derecha"

        if lado != debeIr:
            return False, (
                f"El valor {valor} debe ir a la {debeIr} "
                f"del nodo {padreValor}, según las reglas del ABB."
            )

        if lado == "izquierda":

            if actual.izquierdoPtr is not None:
                return False, (
                    f"El nodo {padreValor} ya tiene hijo izquierdo. "
                    "Utiliza la inserción automática."
                )

            actual.izquierdoPtr = Nodo(valor)

        elif lado == "derecha":

            if actual.derechoPtr is not None:
                return False, (
                    f"El nodo {padreValor} ya tiene hijo derecho. "
                    "Utiliza la inserción automática."
                )

            actual.derechoPtr = Nodo(valor)

        else:
            return False, "Lado inválido."

        return True, f"Se insertó el {valor} a la {lado} del {padreValor}."

    # ---------- BUSCAR ----------

    def buscar(self, x):
        actual = self.__raizPtr

        while actual is not None:

            if x == actual.dato:
                return True

            if x < actual.dato:
                actual = actual.izquierdoPtr
            else:
                actual = actual.derechoPtr

        return False


    def mostrarAcostado(self):

        if self.esVacio():
            print("El árbol está vacío.")
            return

        self.__acostado(self.__raizPtr, 0)

    def __acostado(self, nodo, nivel):

        if nodo is None:
            return

        self.__acostado(nodo.derechoPtr, nivel + 1)

        print("      " * nivel + str(nodo.dato))

        self.__acostado(nodo.izquierdoPtr, nivel + 1)

    # ---------- COORDENADAS ----------

    def __coordenadas(self, nodo, nivel, coords):

        if nodo is None:
            return

        self.__coordenadas(nodo.izquierdoPtr, nivel + 1, coords)

        coords[nodo] = (len(coords), nivel)

        self.__coordenadas(nodo.derechoPtr, nivel + 1, coords)

    # ---------- GRAFICAR ARBOL ----------

    def graficarArbol(self):

        try:
            self.__graficarTk()

        except Exception as error:

            print(
                f"No se pudo abrir la ventana ({error}). "
                "Se dibuja en consola:\n"
            )

            if self.esVacio():
                print("El árbol está vacío.")
            else:
                self.__graficarConsola()

    def __graficarTk(self):

        import tkinter as tk

        dx, dy, radio, margen = 60, 80, 20, 40

        AMARILLO = "#fbbf24"
        AZUL = "#93c5fd"
        VERDE = "#4ade80"
        ROJO = "#f87171"
        MORADO = "#c084fc"

        ventana = tk.Tk()
        ventana.title("Simulador Visual de Árbol Binario de Búsqueda")
        ventana.geometry("1100x760")
        ventana.configure(bg="#f8fafc")

        resaltados = set()
        seleccion = [None]
        posiciones = []
        animacion = [None]

        estadisticas = tk.StringVar()
        textoSeleccion = tk.StringVar()

        # ---------- DIBUJAR ----------

        def dibujar():

            lienzo.delete("all")
            posiciones.clear()

            if seleccion[0] is not None and not self.buscar(seleccion[0]):
                seleccion[0] = None

            if seleccion[0] is not None:
                textoSeleccion.set(f"Seleccionado: {seleccion[0]}")
            else:
                textoSeleccion.set(
                    "Seleccionado: (haz clic en un nodo)"
                )

            coords = {}

            self.__coordenadas(self.__raizPtr, 0, coords)

            anchoArbol = len(coords) * dx + 2 * margen
            altoArbol = self.altura() * dy + 2 * margen

            anchoLienzo = max(lienzo.winfo_width(), anchoArbol)

            lienzo.configure(
                scrollregion=(
                    0, 0,
                    anchoLienzo,
                    max(altoArbol, lienzo.winfo_height())
                )
            )

            desplazamiento = (anchoLienzo - anchoArbol) // 2

            estadisticas.set(
                f"Altura: {self.altura()} | "
                f"Hojas: {self.contarHojas()} | "
                f"Nodos: {self.contarNodos()} | "
                f"Completo: {'SÍ' if self.esCompleto() else 'NO'} | "
                f"Lleno: {'SÍ' if self.esLleno() else 'NO'}"
            )

            if not coords:

                lienzo.create_text(
                    anchoLienzo // 2,
                    120,
                    text="Árbol vacío: inserta un valor",
                    font=("Arial", 14),
                    fill="#64748b"
                )

                return

            def centro(nodo):

                i, nivel = coords[nodo]

                return (
                    desplazamiento + margen + i * dx,
                    margen + nivel * dy
                )

            # Dibujar conexiones
            for nodo in coords:

                x, y = centro(nodo)

                for hijo in (
                    nodo.izquierdoPtr,
                    nodo.derechoPtr
                ):

                    if hijo is not None:

                        hx, hy = centro(hijo)

                        lienzo.create_line(
                            x, y, hx, hy,
                            width=2,
                            fill="#475569"
                        )

            # Dibujar nodos
            for nodo in coords:

                x, y = centro(nodo)

                posiciones.append((x, y, nodo.dato))

                if nodo.dato in resaltados:
                    color = ROJO

                elif nodo.dato == seleccion[0]:
                    color = MORADO

                elif nodo is self.__raizPtr:
                    color = AMARILLO

                elif (
                    nodo.izquierdoPtr is None
                    and nodo.derechoPtr is None
                ):
                    color = VERDE

                else:
                    color = AZUL

                lienzo.create_oval(
                    x - radio, y - radio,
                    x + radio, y + radio,
                    fill=color,
                    outline="#1e293b",
                    width=2
                )

                lienzo.create_text(
                    x, y,
                    text=str(nodo.dato),
                    font=("Arial", 11, "bold")
                )

        # ---------- SELECCIONAR NODO ----------

        def clicEnLienzo(evento):

            x = lienzo.canvasx(evento.x)
            y = lienzo.canvasy(evento.y)

            for cx, cy, dato in posiciones:

                if (x - cx) ** 2 + (y - cy) ** 2 <= radio ** 2:

                    seleccion[0] = dato
                    dibujar()
                    return

        # ---------- REGISTRO ----------

        def log(texto):

            registro.configure(state="normal")

            registro.insert("end", texto + "\n")
            registro.see("end")

            registro.configure(state="disabled")

        def detener():

            if animacion[0] is not None:

                ventana.after_cancel(animacion[0])
                animacion[0] = None

        def accion(texto, resaltar=()):

            detener()

            resaltados.clear()
            resaltados.update(resaltar)

            log(texto)
            dibujar()

        def leer():

            try:
                valor = int(entrada.get())

            except ValueError:

                accion("Escribe un número entero válido.")
                return None

            entrada.delete(0, "end")

            return valor

        # ---------- INSERTAR AUTOMATICAMENTE ----------

        def insertar():

            v = leer()

            if v is not None:

                ok = self.insertarNodo(v)

                accion(
                    f"Se insertó el {v}."
                    if ok else
                    f"El {v} ya existe.",
                    [v] if ok else []
                )

        # ---------- INSERTAR A UN LADO ----------

        def insertarLado(lado):

            if seleccion[0] is None:

                accion("Primero haz clic en el nodo que será el padre.")
                return

            v = leer()

            if v is not None:

                ok, mensaje = self.insertarHijo(
                    seleccion[0],
                    lado,
                    v
                )

                accion(mensaje, [v] if ok else [])

        # ---------- BUSCAR ----------

        def buscarNodo():

            v = leer()

            if v is not None:

                hallado = self.buscar(v)

                accion(
                    f"El {v} {'SÍ' if hallado else 'NO'} está en el árbol.",
                    [v] if hallado else []
                )

        # ---------- ELIMINAR ----------

        def eliminar(porPredecesor):

            v = leer()

            if v is not None:

                if porPredecesor:
                    ok = self.eliminarPredecesor(v)
                else:
                    ok = self.eliminarSucesor(v)

                accion(
                    f"Se eliminó el {v}."
                    if ok else
                    f"El {v} no está en el árbol."
                )

        # ---------- ANIMAR RECORRIDOS ----------

        def animar(lista, i):

            resaltados.clear()

            if i < len(lista):

                resaltados.add(lista[i])

                animacion[0] = ventana.after(
                    600,
                    animar,
                    lista,
                    i + 1
                )

            else:
                animacion[0] = None

            dibujar()

        def recorrer(nombre, funcion):

            detener()

            lista = funcion()

            log(f"{nombre}: {lista}")

            animar(lista, 0)

        # ---------- MOSTRAR ACOSTADO ----------

        def acostado():

            buffer = io.StringIO()

            with contextlib.redirect_stdout(buffer):
                self.mostrarAcostado()

            accion(
                "Árbol acostado:\n" +
                buffer.getvalue().rstrip()
            )

        # ---------- PODAR ----------

        def podar():

            self.podarArbol()

            seleccion[0] = None

            accion("Árbol eliminado.")

        # ---------- BOTONES ----------

        def boton(padre, texto, color, comando, fg="white"):

            tk.Button(
                padre,
                text=texto,
                command=comando,
                bg=color,
                fg=fg,
                activebackground=color,
                activeforeground=fg,
                relief="flat",
                font=("Arial", 10, "bold"),
                pady=6,
                cursor="hand2"
            ).pack(fill="x", padx=8, pady=3)

        def seccion(titulo):

            marco = tk.LabelFrame(
                izquierda,
                text=titulo,
                font=("Arial", 10, "bold"),
                bg="#f8fafc",
                padx=4,
                pady=4
            )

            marco.pack(fill="x", padx=8, pady=6)

            return marco

        izquierda = tk.Frame(
            ventana,
            bg="#f8fafc",
            width=270
        )

        izquierda.pack(side="left", fill="y")

        s1 = seccion("1. Nodos")

        tk.Label(
            s1,
            text="Valor:",
            bg="#f8fafc",
            fg="#475569",
            anchor="w"
        ).pack(fill="x", padx=8)

        entrada = tk.Entry(
            s1,
            font=("Arial", 11),
            bg="#f1f5f9",
            relief="flat"
        )

        entrada.pack(fill="x", padx=8, pady=4, ipady=4)
        entrada.focus()

        entrada.bind("<Return>", lambda e: insertar())

        boton(s1, "[1] Insertar automáticamente", "#2563eb", insertar)

        tk.Label(
            s1,
            textvariable=textoSeleccion,
            bg="#f8fafc",
            fg="#7c3aed",
            font=("Arial", 9, "bold"),
            anchor="w"
        ).pack(fill="x", padx=8, pady=(6, 0))

        boton(
            s1,
            "[14] Insertar a la IZQUIERDA",
            "#7c3aed",
            lambda: insertarLado("izquierda")
        )

        boton(
            s1,
            "[15] Insertar a la DERECHA",
            "#7c3aed",
            lambda: insertarLado("derecha")
        )

        boton(s1, "[4] Buscar nodo", "#0284c7", buscarNodo)

        boton(
            s1,
            "[8] Eliminar por Predecesor",
            "#dc2626",
            lambda: eliminar(True)
        )

        boton(
            s1,
            "[9] Eliminar por Sucesor",
            "#e11d48",
            lambda: eliminar(False)
        )

        s2 = seccion("2. Recorridos del Árbol")

        gris = "#e2e8f0"
        texto = "#1e293b"

        boton(
            s2, "[5] PreOrden (Raíz - Izq - Der)",
            gris, lambda: recorrer("PreOrden", self.preOrden), texto
        )

        boton(
            s2, "[6] InOrden (Ascendente)",
            gris, lambda: recorrer("InOrden", self.inOrden), texto
        )

        boton(
            s2, "[7] PostOrden (Izq - Der - Raíz)",
            gris, lambda: recorrer("PostOrden", self.postOrden), texto
        )

        boton(
            s2, "[10] Por Niveles (Amplitud)",
            gris, lambda: recorrer("Por niveles", self.recorridoNiveles), texto
        )

        s3 = seccion("3. Utilidades")

        boton(s3, "[2] Mostrar Acostado", "#475569", acostado)

        boton(s3, "[18] Vaciar / Podar Árbol", "#991b1b", podar)

        # ---------- PANEL DERECHO ----------

        derecha = tk.Frame(ventana, bg="#f8fafc")

        derecha.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 8),
            pady=8
        )

        tk.Label(
            derecha,
            textvariable=estadisticas,
            bg="#1e293b",
            fg="white",
            font=("Arial", 11, "bold"),
            pady=12
        ).pack(side="top", fill="x")

        registro = tk.Text(
            derecha,
            height=8,
            bg="#0f172a",
            fg="#38bdf8",
            font=("Consolas", 10),
            relief="flat",
            padx=10,
            pady=8,
            state="disabled"
        )

        registro.pack(side="bottom", fill="x", pady=(8, 0))

        leyenda = tk.Frame(derecha, bg="white")
        leyenda.pack(side="top", fill="x", pady=(8, 0))

        for nombre, color in [
            ("Raíz", AMARILLO),
            ("Rama", AZUL),
            ("Hoja", VERDE),
            ("Seleccionado", MORADO),
            ("Resaltado", ROJO)
        ]:

            tk.Label(
                leyenda,
                text="●",
                fg=color,
                bg="white",
                font=("Arial", 14)
            ).pack(side="left", padx=(10, 0))

            tk.Label(
                leyenda,
                text=nombre,
                bg="white",
                fg="#475569",
                font=("Arial", 9, "bold")
            ).pack(side="left", padx=(2, 6))

        marco = tk.Frame(
            derecha,
            bg="white",
            highlightbackground="#cbd5e1",
            highlightthickness=1
        )

        marco.pack(side="top", fill="both", expand=True)

        lienzo = tk.Canvas(
            marco,
            bg="white",
            highlightthickness=0
        )

        barraX = tk.Scrollbar(
            marco,
            orient="horizontal",
            command=lienzo.xview
        )

        barraY = tk.Scrollbar(
            marco,
            orient="vertical",
            command=lienzo.yview
        )

        lienzo.configure(
            xscrollcommand=barraX.set,
            yscrollcommand=barraY.set
        )

        barraX.pack(side="bottom", fill="x")
        barraY.pack(side="right", fill="y")

        lienzo.pack(side="left", fill="both", expand=True)

        lienzo.bind("<Configure>", lambda e: dibujar())
        lienzo.bind("<Button-1>", clicEnLienzo)

        log(
            "Listo. Inserta el primer valor y haz clic en un nodo "
            "para elegir izquierda o derecha."
        )

        dibujar()

        print("Ventana interactiva abierta. Ciérrala para volver al menú.")

        ventana.mainloop()


    def __graficarConsola(self):

        coords = {}

        self.__coordenadas(self.__raizPtr, 0, coords)

        ancho = max(len(str(n.dato)) for n in coords) + 2

        filas = 3 * (self.altura() - 1) + 1

        lienzo = [
            [" "] * (len(coords) * ancho + ancho)
            for _ in range(filas)
        ]

        def col(nodo):
            return (
                coords[nodo][0] * ancho
                + len(str(nodo.dato)) // 2
            )

        for nodo, (i, nivel) in coords.items():

            fila = 3 * nivel

            for k, c in enumerate(str(nodo.dato)):
                lienzo[fila][i * ancho + k] = c

            hijos = [
                h for h in (
                    nodo.izquierdoPtr,
                    nodo.derechoPtr
                ) if h
            ]

            if hijos:

                cols = [col(h) for h in hijos] + [col(nodo)]

                for c in range(min(cols), max(cols) + 1):
                    lienzo[fila + 1][c] = "-"

                lienzo[fila + 1][col(nodo)] = "+"

                for h in hijos:

                    lienzo[fila + 1][col(h)] = "+"
                    lienzo[fila + 2][col(h)] = "|"

        for linea in lienzo:
            print("".join(linea).rstrip())

    # ---------- RECORRIDOS ----------

    def preOrden(self):

        resultado = []

        self.__pre(self.__raizPtr, resultado)

        return resultado

    def __pre(self, nodo, res):

        if nodo:

            res.append(nodo.dato)

            self.__pre(nodo.izquierdoPtr, res)
            self.__pre(nodo.derechoPtr, res)

    def inOrden(self):

        resultado = []

        self.__in(self.__raizPtr, resultado)

        return resultado

    def __in(self, nodo, res):

        if nodo:

            self.__in(nodo.izquierdoPtr, res)

            res.append(nodo.dato)

            self.__in(nodo.derechoPtr, res)

    def postOrden(self):

        resultado = []

        self.__post(self.__raizPtr, resultado)

        return resultado

    def __post(self, nodo, res):

        if nodo:

            self.__post(nodo.izquierdoPtr, res)
            self.__post(nodo.derechoPtr, res)

            res.append(nodo.dato)

    def recorridoNiveles(self):

        resultado = []

        if self.esVacio():
            return resultado

        cola = deque([self.__raizPtr])

        while cola:

            nodo = cola.popleft()

            resultado.append(nodo.dato)

            if nodo.izquierdoPtr:
                cola.append(nodo.izquierdoPtr)

            if nodo.derechoPtr:
                cola.append(nodo.derechoPtr)

        return resultado

   

    def altura(self):
        return self.__altura(self.__raizPtr)

    def __altura(self, nodo):

        if nodo is None:
            return 0

        return 1 + max(
            self.__altura(nodo.izquierdoPtr),
            self.__altura(nodo.derechoPtr)
        )

    def contarNodos(self):
        return self.__nodos(self.__raizPtr)

    def __nodos(self, nodo):

        if nodo is None:
            return 0

        return (
            1
            + self.__nodos(nodo.izquierdoPtr)
            + self.__nodos(nodo.derechoPtr)
        )

    def contarHojas(self):
        return self.__hojas(self.__raizPtr)

    def __hojas(self, nodo):

        if nodo is None:
            return 0

        if (
            nodo.izquierdoPtr is None
            and nodo.derechoPtr is None
        ):
            return 1

        return (
            self.__hojas(nodo.izquierdoPtr)
            + self.__hojas(nodo.derechoPtr)
        )

    # ---------- ELIMINAR POR PREDECESOR O SUCESOR ----------

    def eliminarPredecesor(self, x):

        if not self.buscar(x):
            return False

        self.__raizPtr = self.__eliminar(
            self.__raizPtr,
            x,
            True
        )

        return True

    def eliminarSucesor(self, x):

        if not self.buscar(x):
            return False

        self.__raizPtr = self.__eliminar(
            self.__raizPtr,
            x,
            False
        )

        return True

    def __eliminar(self, nodo, x, usarPredecesor):

        if nodo is None:
            return None

        if x < nodo.dato:

            nodo.izquierdoPtr = self.__eliminar(
                nodo.izquierdoPtr,
                x,
                usarPredecesor
            )

        elif x > nodo.dato:

            nodo.derechoPtr = self.__eliminar(
                nodo.derechoPtr,
                x,
                usarPredecesor
            )

        else:

            # Caso 1: no tiene hijo izquierdo
            if nodo.izquierdoPtr is None:
                return nodo.derechoPtr

            # Caso 2: no tiene hijo derecho
            if nodo.derechoPtr is None:
                return nodo.izquierdoPtr

            # Caso 3: tiene dos hijos
            if usarPredecesor:

                reemplazo = nodo.izquierdoPtr

                while reemplazo.derechoPtr:
                    reemplazo = reemplazo.derechoPtr

                nodo.dato = reemplazo.dato

                nodo.izquierdoPtr = self.__eliminar(
                    nodo.izquierdoPtr,
                    reemplazo.dato,
                    True
                )

            else:

                reemplazo = nodo.derechoPtr

                while reemplazo.izquierdoPtr:
                    reemplazo = reemplazo.izquierdoPtr

                nodo.dato = reemplazo.dato

                nodo.derechoPtr = self.__eliminar(
                    nodo.derechoPtr,
                    reemplazo.dato,
                    False
                )

        return nodo

    # ---------- TIPOS DE ARBOL ----------

    def esCompleto(self):

        if self.esVacio():
            return True

        cola = deque([self.__raizPtr])

        huboVacio = False

        while cola:

            nodo = cola.popleft()

            if nodo is None:

                huboVacio = True

            else:

                if huboVacio:
                    return False

                cola.append(nodo.izquierdoPtr)
                cola.append(nodo.derechoPtr)

        return True

    def esLleno(self):

        if self.esVacio():
            return True

        return self.contarNodos() == 2 ** self.altura() - 1

    # ---------- VACIAR ARBOL ----------

    def podarArbol(self):
        self.__raizPtr = None


# ==================================================
# MENU PRINCIPAL
# ==================================================

MENU = """
===== ARBOL BINARIO DE BUSQUEDA =====

 1. Insertar elemento (automatico)
 2. Mostrar arbol completo acostado
 3. Graficar arbol completo (ventana interactiva)
 4. Buscar un elemento
 5. Recorrer en PreOrden
 6. Recorrer en InOrden
 7. Recorrer en PostOrden
 8. Eliminar un nodo (PREDECESOR)
 9. Eliminar un nodo (SUCESOR)
10. Recorrer por niveles (Amplitud)
11. Altura del arbol
12. Cantidad de hojas
13. Cantidad de nodos
14. Insertar hijo a la IZQUIERDA
15. Insertar hijo a la DERECHA
16. Revisar si es arbol binario completo
17. Revisar si es arbol binario lleno
18. Eliminar el arbol

 0. Salir
"""


def pedirEntero(mensaje):

    while True:

        try:
            return int(input(mensaje))

        except ValueError:
            print("Entrada invalida: escribe un numero entero.")


# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================

def main():

    arbol = Arbol()

    while True:

        print(MENU)

        try:
            opcion = int(input("Elige una opcion: "))

        except ValueError:
            print("Opcion invalida: escribe un numero del menu.")
            continue

        except (EOFError, KeyboardInterrupt):
            print("\nHasta luego.")
            break

        if opcion == 0:

            print("Hasta luego.")
            break

        # INSERTAR AUTOMATICAMENTE
        elif opcion == 1:

            valor = pedirEntero("Valor a insertar: ")

            if arbol.insertarNodo(valor):
                print(f"Se inserto el {valor}.")

            else:
                print(f"El {valor} ya existe, no se permiten repetidos.")

        # MOSTRAR ACOSTADO
        elif opcion == 2:

            arbol.mostrarAcostado()

        # GRAFICAR
        elif opcion == 3:

            arbol.graficarArbol()

        # BUSCAR
        elif opcion == 4:

            x = pedirEntero("Valor a buscar: ")

            print(
                f"El {x} "
                f"{'SI' if arbol.buscar(x) else 'NO'} "
                "esta en el arbol."
            )

        # PREORDEN
        elif opcion == 5:

            print("PreOrden:", arbol.preOrden())

        # INORDEN
        elif opcion == 6:

            print("InOrden:", arbol.inOrden())

        # POSTORDEN
        elif opcion == 7:

            print("PostOrden:", arbol.postOrden())

        # ELIMINAR POR PREDECESOR O SUCESOR
        elif opcion in (8, 9):

            x = pedirEntero("Valor a eliminar: ")

            if opcion == 8:
                eliminado = arbol.eliminarPredecesor(x)
            else:
                eliminado = arbol.eliminarSucesor(x)

            print(
                f"Se elimino el {x}."
                if eliminado
                else f"El {x} no esta en el arbol."
            )

        # RECORRIDO POR NIVELES
        elif opcion == 10:

            print("Por niveles:", arbol.recorridoNiveles())

        # ALTURA
        elif opcion == 11:

            print("Altura (en niveles):", arbol.altura())

        # CANTIDAD DE HOJAS
        elif opcion == 12:

            print("Cantidad de hojas:", arbol.contarHojas())

        # CANTIDAD DE NODOS
        elif opcion == 13:

            print("Cantidad de nodos:", arbol.contarNodos())

        # INSERTAR A LA IZQUIERDA
        elif opcion == 14:

            if arbol.esVacio():

                print("Primero debes insertar la raiz del arbol.")

            else:

                padre = pedirEntero(
                    "Ingresa el valor del nodo padre: "
                )

                valor = pedirEntero(
                    "Ingresa el valor del nuevo nodo: "
                )

                exito, mensaje = arbol.insertarHijo(
                    padre,
                    "izquierda",
                    valor
                )

                print(mensaje)

        # INSERTAR A LA DERECHA
        elif opcion == 15:

            if arbol.esVacio():

                print("Primero debes insertar la raiz del arbol.")

            else:

                padre = pedirEntero(
                    "Ingresa el valor del nodo padre: "
                )

                valor = pedirEntero(
                    "Ingresa el valor del nuevo nodo: "
                )

                exito, mensaje = arbol.insertarHijo(
                    padre,
                    "derecha",
                    valor
                )

                print(mensaje)

        # ARBOL COMPLETO
        elif opcion == 16:

            print(
                "¿Es completo?",
                "SI" if arbol.esCompleto() else "NO"
            )

        # ARBOL LLENO
        elif opcion == 17:

            print(
                "¿Es lleno?",
                "SI" if arbol.esLleno() else "NO"
            )

        # ELIMINAR TODO EL ARBOL
        elif opcion == 18:

            arbol.podarArbol()

            print("Arbol eliminado correctamente.")

        else:

            print("Opcion fuera del menu.")




if __name__ == "__main__":
    main()
