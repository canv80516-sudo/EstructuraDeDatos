
import tkinter as tk
from tkinter import messagebox


FONDO = "#121212"
TARJETA = "#212121"
ROJO = "#D32F2F"
ROJO_OSCURO = "#8b0000"
AMARILLO = "#FFDE00"
BLANCO = "#FFFFFF"
GRIS = "#A0A0A0"
VERDE = "#4CAF50"


def shell_sort(lista):
    n = len(lista)
    salto = n // 2

    while salto > 0:
        for i in range(salto, n):
            temporal = lista[i]
            j = i

            while j >= salto and lista[j - salto] > temporal:
                lista[j] = lista[j - salto]
                j -= salto

            lista[j] = temporal

        salto //= 2

    return lista


def quick_sort(lista):

    def ordenar(inicio, fin):
        if inicio < fin:
            pivote = lista[fin]
            i = inicio - 1

            for j in range(inicio, fin):
                if lista[j] <= pivote:
                    i += 1
                    lista[i], lista[j] = lista[j], lista[i]

            lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
            posicion = i + 1

            ordenar(inicio, posicion - 1)
            ordenar(posicion + 1, fin)

    ordenar(0, len(lista) - 1)
    return lista


def heap_sort(lista):
    n = len(lista)

    def crear_monticulo(n, i):
        mayor = i
        izquierda = 2 * i + 1
        derecha = 2 * i + 2

        if izquierda < n and lista[izquierda] > lista[mayor]:
            mayor = izquierda

        if derecha < n and lista[derecha] > lista[mayor]:
            mayor = derecha

        if mayor != i:
            lista[i], lista[mayor] = lista[mayor], lista[i]
            crear_monticulo(n, mayor)

    for i in range(n // 2 - 1, -1, -1):
        crear_monticulo(n, i)

    for i in range(n - 1, 0, -1):
        lista[0], lista[i] = lista[i], lista[0]
        crear_monticulo(i, 0)

    return lista


def radix_sort(lista):

    if not lista:
        return lista

    if any(numero < 0 for numero in lista):
        raise ValueError("No se permiten numeros negativos.")

    maximo = max(lista)
    posicion = 1

    while maximo // posicion > 0:
        cubetas = [[] for _ in range(10)]

        for numero in lista:
            digito = (numero // posicion) % 10
            cubetas[digito].append(numero)

        lista = []

        for cubeta in cubetas:
            lista.extend(cubeta)

        posicion *= 10

    return lista


ventana = tk.Tk()
ventana.title("Pokedex Sort - Centro de Entrenamiento")
ventana.configure(bg=FONDO)

# Maximizar ventana
try:
    ventana.state("zoomed")
except tk.TclError:
    ventana.geometry("1200x850")

ventana.minsize(850, 650)

campos = []

def actualizar_texto(widget, texto):

    widget.config(state="normal")
    widget.delete("1.0", tk.END)
    widget.insert("1.0", texto)
    widget.config(state="disabled")


def formatear_numeros(lista):

    lineas = []

    # Mostrar 10 numeros por linea
    for i in range(0, len(lista), 10):
        grupo = lista[i:i + 10]
        lineas.append("   |   ".join(map(str, grupo)))

    return "\n".join(lineas)

def crear_campos():

    global campos

    for widget in contenedor_pokemon.winfo_children():
        widget.destroy()

    campos = []

    try:
        cantidad = int(entrada_cantidad.get())

        if cantidad < 1 or cantidad > 100:
            messagebox.showwarning(
                "Cantidad incorrecta",
                "Ingresa una cantidad entre 1 y 100."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Error",
            "Ingresa una cantidad valida."
        )
        return

    for i in range(cantidad):

        fila = i // 3
        columna = i % 3

        tarjeta = tk.Frame(
            contenedor_pokemon,
            bg="#394154",
            padx=15,
            pady=12
        )

        tarjeta.grid(
            row=fila,
            column=columna,
            padx=12,
            pady=10,
            sticky="ew"
        )

        tk.Label(
            tarjeta,
            text=f"POKEMON {i + 1}",
            font=("Arial", 11, "bold"),
            bg="#394154",
            fg=AMARILLO
        ).pack(anchor="w", pady=4)

        entrada = tk.Entry(
            tarjeta,
            font=("Arial", 13),
            bg="#252B3A",
            fg=BLANCO,
            insertbackground=BLANCO,
            relief="flat",
            justify="center"
        )

        entrada.pack(fill="x", pady=5, ipady=5)

        campos.append(entrada)

    for columna in range(3):
        contenedor_pokemon.grid_columnconfigure(
            columna, weight=1
        )

    etiqueta_estado.config(
        text=f"Se crearon {cantidad} espacios para tu equipo.",
        fg=VERDE
    )

    actualizar_texto(
        resultado_original, "Esperando datos..."
    )

    actualizar_texto(
        resultado_ordenado,
        "Selecciona un metodo de ordenamiento."
    )

    etiqueta_metodo.config(text="METODO: NINGUNO")


def obtener_numeros():

    if not campos:
        messagebox.showwarning(
            "Atencion",
            "Primero debes crear tu equipo."
        )
        return None

    numeros = []

    for i, campo in enumerate(campos):

        try:
            numero = int(campo.get())

            if numero < 0:
                raise ValueError

            numeros.append(numero)

        except ValueError:
            messagebox.showerror(
                "Dato incorrecto",
                f"El PC del Pokemon {i + 1} debe ser un entero positivo o cero."
            )
            return None

    return numeros


def ejecutar_ordenamiento(nombre, metodo):

    numeros = obtener_numeros()

    if numeros is None:
        return

    original = numeros.copy()

    try:
        resultado = metodo(numeros.copy())

    except ValueError as error:
        messagebox.showerror("Error", str(error))
        return
    
    actualizar_texto(
        resultado_original,
        formatear_numeros(original)
    )

    
    actualizar_texto(
        resultado_ordenado,
        formatear_numeros(resultado)
    )

    etiqueta_metodo.config(
        text=f"METODO UTILIZADO: {nombre}"
    )

    etiqueta_estado.config(
        text="¡Entrenamiento completado correctamente!",
        fg=VERDE
    )


def limpiar():

    global campos

    entrada_cantidad.delete(0, tk.END)

    for campo in campos:
        campo.delete(0, tk.END)

    for widget in contenedor_pokemon.winfo_children():
        widget.destroy()

    campos = []

    actualizar_texto(
        resultado_original, "Esperando datos..."
    )

    actualizar_texto(
        resultado_ordenado,
        "Selecciona un metodo de ordenamiento."
    )

    etiqueta_metodo.config(text="METODO: NINGUNO")

    etiqueta_estado.config(
        text="Registra tu equipo para comenzar.",
        fg=GRIS
    )


def salir():

    respuesta = messagebox.askyesno(
        "Salir",
        "¿Deseas salir del Centro de Entrenamiento Pokemon?"
    )

    if respuesta:
        ventana.destroy()



encabezado = tk.Frame(
    ventana,
    bg=ROJO,
    padx=25,
    pady=15
)
encabezado.pack(fill="x")

fila_encabezado = tk.Frame(
    encabezado,
    bg=ROJO
)
fila_encabezado.pack(fill="x")

tk.Label(
    fila_encabezado,
    text="POKEDEX SORT",
    font=("Arial", 27, "bold"),
    bg=ROJO,
    fg=BLANCO
).pack(side="left", padx=10)

tk.Button(
    fila_encabezado,
    text="✖ SALIR",
    command=salir,
    bg=ROJO_OSCURO,
    fg=BLANCO,
    font=("Arial", 11, "bold"),
    relief="flat",
    padx=20,
    pady=8,
    cursor="hand2"
).pack(side="right", padx=10)

tk.Label(
    encabezado,
    text="CENTRO DE ENTRENAMIENTO POKEMON",
    font=("Arial", 11, "bold"),
    bg=ROJO,
    fg=AMARILLO
).pack(anchor="w", padx=12, pady=5)


marco_principal = tk.Frame(
    ventana,
    bg=FONDO
)
marco_principal.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=10
)

lienzo = tk.Canvas(
    marco_principal,
    bg=FONDO,
    highlightthickness=0
)

barra = tk.Scrollbar(
    marco_principal,
    orient="vertical",
    command=lienzo.yview
)

lienzo.configure(yscrollcommand=barra.set)

barra.pack(side="right", fill="y")
lienzo.pack(side="left", fill="both", expand=True)

contenido = tk.Frame(
    lienzo,
    bg=FONDO
)

ventana_contenido = lienzo.create_window(
    (0, 0),
    window=contenido,
    anchor="nw"
)


def actualizar_area(event=None):

    lienzo.configure(
        scrollregion=lienzo.bbox("all")
    )


def ajustar_ancho(event):

    lienzo.itemconfigure(
        ventana_contenido,
        width=event.width
    )


contenido.bind("<Configure>", actualizar_area)
lienzo.bind("<Configure>", ajustar_ancho)


tk.Label(
    contenido,
    text="¡Bienvenido, entrenador!",
    font=("Arial", 20, "bold"),
    bg=FONDO,
    fg=BLANCO
).pack(pady=(10, 5))

tk.Label(
    contenido,
    text="Organiza los puntos de combate de tu equipo Pokemon.",
    font=("Arial", 12),
    bg=FONDO,
    fg=GRIS
).pack(pady=(0, 18))

# REGISTRO DE EQUIPO

seccion_registro = tk.Frame(
    contenido,
    bg=TARJETA,
    padx=25,
    pady=20
)
seccion_registro.pack(
    fill="x",
    padx=25,
    pady=12
)

tk.Label(
    seccion_registro,
    text="1. REGISTRO DE TU EQUIPO",
    font=("Arial", 15, "bold"),
    bg=TARJETA,
    fg=AMARILLO
).pack(anchor="w", pady=8)

tk.Label(
    seccion_registro,
    text="¿Cuantos Pokemon deseas registrar? (1 a 100)",
    font=("Arial", 12),
    bg=TARJETA,
    fg=BLANCO
).pack(anchor="w", pady=8)

fila_cantidad = tk.Frame(
    seccion_registro,
    bg=TARJETA
)
fila_cantidad.pack(anchor="w", pady=5)

entrada_cantidad = tk.Entry(
    fila_cantidad,
    font=("Arial", 13),
    width=12,
    justify="center"
)
entrada_cantidad.pack(side="left", padx=(0, 15), ipady=5)

tk.Button(
    fila_cantidad,
    text="CREAR EQUIPO",
    command=crear_campos,
    bg=ROJO,
    fg=BLANCO,
    font=("Arial", 11, "bold"),
    relief="flat",
    padx=22,
    pady=10,
    cursor="hand2"
).pack(side="left")


# ==========================================
# ENTRADAS DE POKEMON
# ==========================================

seccion_campos = tk.Frame(
    contenido,
    bg=TARJETA,
    padx=25,
    pady=20
)
seccion_campos.pack(
    fill="x",
    padx=25,
    pady=12
)

tk.Label(
    seccion_campos,
    text="2. PUNTOS DE COMBATE (PC)",
    font=("Arial", 15, "bold"),
    bg=TARJETA,
    fg=AMARILLO
).pack(anchor="w", pady=8)

tk.Label(
    seccion_campos,
    text="Introduce los puntos de combate de cada Pokemon.",
    font=("Arial", 11),
    bg=TARJETA,
    fg=GRIS
).pack(anchor="w", pady=5)

contenedor_pokemon = tk.Frame(
    seccion_campos,
    bg=TARJETA
)
contenedor_pokemon.pack(fill="x", pady=10)

# METODOS DE ORDENAMIENTO


seccion_metodos = tk.Frame(
    contenido,
    bg=TARJETA,
    padx=25,
    pady=20
)
seccion_metodos.pack(
    fill="x",
    padx=25,
    pady=12
)

tk.Label(
    seccion_metodos,
    text="3. ELIGE TU METODO DE ORDENAMIENTO",
    font=("Arial", 15, "bold"),
    bg=TARJETA,
    fg=AMARILLO
).pack(anchor="w", pady=10)

fila_botones = tk.Frame(
    seccion_metodos,
    bg=TARJETA
)
fila_botones.pack(fill="x", pady=10)

metodos = [
    ("SHELL SORT", shell_sort),
    ("QUICKSORT", quick_sort),
    ("HEAPSORT", heap_sort),
    ("RADIX SORT", radix_sort)
]

for nombre, metodo in metodos:

    tk.Button(
        fila_botones,
        text=nombre,
        command=lambda n=nombre, m=metodo:
            ejecutar_ordenamiento(n, m),
        bg=ROJO,
        fg=BLANCO,
        font=("Arial", 11, "bold"),
        relief="flat",
        padx=12,
        pady=15,
        cursor="hand2"
    ).pack(
        side="left",
        expand=True,
        fill="x",
        padx=7
    )

# RESULTADOS


seccion_resultados = tk.Frame(
    contenido,
    bg=TARJETA,
    padx=25,
    pady=20
)
seccion_resultados.pack(
    fill="x",
    padx=25,
    pady=12
)

tk.Label(
    seccion_resultados,
    text="4. RESULTADOS DEL ENTRENAMIENTO",
    font=("Arial", 15, "bold"),
    bg=TARJETA,
    fg=AMARILLO
).pack(anchor="w", pady=10)

etiqueta_metodo = tk.Label(
    seccion_resultados,
    text="METODO: NINGUNO",
    font=("Arial", 11, "bold"),
    bg=TARJETA,
    fg=AMARILLO
)
etiqueta_metodo.pack(anchor="w", pady=8)

tk.Label(
    seccion_resultados,
    text="PC ORIGINALES:",
    font=("Arial", 11, "bold"),
    bg=TARJETA,
    fg=GRIS
).pack(anchor="w", pady=5)

# Area de resultados originales
marco_original = tk.Frame(
    seccion_resultados,
    bg=TARJETA
)
marco_original.pack(fill="x", pady=5)

resultado_original = tk.Text(
    marco_original,
    height=5,
    font=("Consolas", 11),
    bg="#394154",
    fg=BLANCO,
    relief="flat",
    wrap="word",
    padx=12,
    pady=10,
    state="disabled"
)

scroll_original = tk.Scrollbar(
    marco_original,
    command=resultado_original.yview
)

resultado_original.configure(
    yscrollcommand=scroll_original.set
)

scroll_original.pack(side="right", fill="y")
resultado_original.pack(side="left", fill="both", expand=True)


tk.Label(
    seccion_resultados,
    text="PC ORDENADOS DE MENOR A MAYOR:",
    font=("Arial", 11, "bold"),
    bg=TARJETA,
    fg=GRIS
).pack(anchor="w", pady=(15, 5))

# Area de resultados ordenados
marco_ordenado = tk.Frame(
    seccion_resultados,
    bg=TARJETA
)
marco_ordenado.pack(fill="x", pady=5)

resultado_ordenado = tk.Text(
    marco_ordenado,
    height=6,
    font=("Consolas", 12, "bold"),
    bg="#263D32",
    fg="#8AFFA0",
    relief="flat",
    wrap="word",
    padx=12,
    pady=10,
    state="disabled"
)

scroll_ordenado = tk.Scrollbar(
    marco_ordenado,
    command=resultado_ordenado.yview
)

resultado_ordenado.configure(
    yscrollcommand=scroll_ordenado.set
)

scroll_ordenado.pack(side="right", fill="y")
resultado_ordenado.pack(side="left", fill="both", expand=True)

# ESTADO DEL PROGRAMA

etiqueta_estado = tk.Label(
    contenido,
    text="Registra tu equipo para comenzar.",
    font=("Arial", 11, "bold"),
    bg=FONDO,
    fg=GRIS
)
etiqueta_estado.pack(pady=15)

# BOTONES FINALES

fila_final = tk.Frame(
    contenido,
    bg=FONDO
)
fila_final.pack(pady=15)

tk.Button(
    fila_final,
    text="LIMPIAR Y NUEVO EQUIPO",
    command=limpiar,
    bg="#3D536D",
    fg=BLANCO,
    font=("Arial", 11, "bold"),
    relief="flat",
    padx=25,
    pady=12,
    cursor="hand2"
).pack(side="left", padx=12)

tk.Button(
    fila_final,
    text="SALIR DEL PROGRAMA",
    command=salir,
    bg=ROJO_OSCURO,
    fg=BLANCO,
    font=("Arial", 11, "bold"),
    relief="flat",
    padx=25,
    pady=12,
    cursor="hand2"
).pack(side="left", padx=12)


def desplazar(event):

    lienzo.yview_scroll(
        int(-1 * (event.delta / 120)),
        "units"
    )


lienzo.bind_all("<MouseWheel>", desplazar)


ventana.mainloop()
