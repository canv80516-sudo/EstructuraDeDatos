
import tkinter as tk
from tkinter import ttk


# ==============================================
# DATOS DEL SISTEMA
# ==============================================

alumnos = [
    "Carlos", "Ana", "Luis", "Mariana",
    "Pedro", "Sofia", "Daniel", "Valeria"
]

matriculas = [
    1001, 1005, 1010, 1015, 1020,
    1025, 1030, 1035, 1040, 1045
]

productos = {
    "P001": {"nombre": "Teclado", "precio": 450, "stock": 10},
    "P002": {"nombre": "Mouse", "precio": 250, "stock": 15},
    "P003": {"nombre": "Monitor", "precio": 3200, "stock": 5},
    "P004": {"nombre": "Audifonos", "precio": 600, "stock": 8},
    "P005": {"nombre": "USB", "precio": 150, "stock": 20},
    "P006": {"nombre": "Laptop", "precio": 12500, "stock": 4},
    "P007": {"nombre": "Teclado gamer", "precio": 900, "stock": 7}
}


# ==============================================
# 1. BUSQUEDA SECUENCIAL
# ==============================================

def busqueda_secuencial(lista, buscado):

    for i in range(len(lista)):

        if lista[i].lower() == buscado.lower():
            return i

    return -1


# ==============================================
# 2. BUSQUEDA BINARIA
# ==============================================

def busqueda_binaria(lista, buscado):

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


# ==============================================
# 3. BUSQUEDA HASH
# ==============================================

def busqueda_hash(diccionario, clave):

    return diccionario.get(clave)


# ==============================================
# FUNCIONES DE LA INTERFAZ
# ==============================================

def mostrar_resultado(mensaje):

    salida.config(state="normal")
    salida.delete("1.0", tk.END)
    salida.insert(tk.END, mensaje)
    salida.config(state="disabled")


def limpiar():

    entrada.delete(0, tk.END)
    mostrar_resultado(
        "Escribe un dato y selecciona el metodo de busqueda."
    )


def buscar_secuencial():

    nombre = entrada.get().strip()

    if nombre == "":
        mostrar_resultado("Escribe el nombre de un alumno.")
        return

    resultado = busqueda_secuencial(alumnos, nombre)

    if resultado != -1:

        mensaje = (
            "BUSQUEDA SECUENCIAL\n\n"
            "Alumno encontrado: " + alumnos[resultado] + "\n"
            "Posicion: " + str(resultado + 1) + "\n\n"
            "Metodo utilizado: Secuencial\n"
            "Se recorrieron los elementos hasta encontrar "
            "el nombre solicitado."
        )

    else:

        mensaje = (
            "BUSQUEDA SECUENCIAL\n\n"
            "El alumno no se encuentra registrado."
        )

    mostrar_resultado(mensaje)


def buscar_binaria():

    dato = entrada.get().strip()

    if dato == "":
        mostrar_resultado("Escribe una matricula.")
        return

    try:

        numero = int(dato)

        resultado = busqueda_binaria(matriculas, numero)

        if resultado != -1:

            mensaje = (
                "BUSQUEDA BINARIA\n\n"
                "Matricula encontrada: "
                + str(matriculas[resultado]) + "\n"
                "Posicion: " + str(resultado + 1) + "\n\n"
                "Metodo utilizado: Binaria\n"
                "La lista se encuentra ordenada y "
                "se divide el rango de busqueda."
            )

        else:

            mensaje = (
                "BUSQUEDA BINARIA\n\n"
                "La matricula no se encuentra registrada."
            )

    except ValueError:

        mensaje = "Error: ingresa una matricula numerica."

    mostrar_resultado(mensaje)


def buscar_hash():

    codigo = entrada.get().strip().upper()

    if codigo == "":
        mostrar_resultado("Escribe el codigo del producto.")
        return

    resultado = busqueda_hash(productos, codigo)

    if resultado is not None:

        mensaje = (
            "BUSQUEDA HASH\n\n"
            "Producto encontrado\n\n"
            "Codigo: " + codigo + "\n"
            "Nombre: " + resultado["nombre"] + "\n"
            "Precio: $ " + str(resultado["precio"]) + "\n"
            "Existencias: " + str(resultado["stock"]) + "\n\n"
            "Metodo utilizado: Hash\n"
            "Se consulto el diccionario mediante la clave."
        )

    else:

        mensaje = (
            "BUSQUEDA HASH\n\n"
            "El producto no se encuentra registrado."
        )

    mostrar_resultado(mensaje)


def mostrar_registros():

    mensaje = "REGISTROS DEL SISTEMA\n\n"

    mensaje += "ALUMNOS:\n"

    for alumno in alumnos:
        mensaje += "- " + alumno + "\n"

    mensaje += "\nMATRICULAS:\n"

    for matricula in matriculas:
        mensaje += "- " + str(matricula) + "\n"

    mensaje += "\nPRODUCTOS:\n"

    for codigo, datos in productos.items():

        mensaje += (
            codigo + " | " + datos["nombre"]
            + " | Precio: $ " + str(datos["precio"])
            + " | Stock: " + str(datos["stock"])
            + "\n"
        )

    mostrar_resultado(mensaje)


# ==============================================
# VENTANA PRINCIPAL
# ==============================================

ventana = tk.Tk()

ventana.title("Sistema de Metodos de Busqueda")
ventana.geometry("760x650")
ventana.minsize(650, 550)
ventana.configure(bg="#EAF2F8")


# ==============================================
# TITULO
# ==============================================

titulo = tk.Label(
    ventana,
    text="SISTEMA DE METODOS DE BUSQUEDA",
    font=("Arial", 18, "bold"),
    bg="#EAF2F8",
    fg="#17365D"
)

titulo.pack(pady=15)


subtitulo = tk.Label(
    ventana,
    text="Selecciona un metodo e ingresa el dato a buscar",
    font=("Arial", 11),
    bg="#EAF2F8",
    fg="#34495E"
)

subtitulo.pack(pady=5)


# ==============================================
# FRAME DE BUSQUEDA
# ==============================================

frame_busqueda = tk.Frame(
    ventana,
    bg="#EAF2F8"
)

frame_busqueda.pack(pady=15)


etiqueta = tk.Label(
    frame_busqueda,
    text="Dato a buscar:",
    font=("Arial", 12, "bold"),
    bg="#EAF2F8"
)

etiqueta.grid(row=0, column=0, padx=10, pady=5)


entrada = tk.Entry(
    frame_busqueda,
    font=("Arial", 12),
    width=30
)

entrada.grid(row=0, column=1, padx=10, pady=5)


# ==============================================
# BOTONES DE BUSQUEDA
# ==============================================

frame_botones = tk.Frame(
    ventana,
    bg="#EAF2F8"
)

frame_botones.pack(pady=10)


boton_secuencial = tk.Button(
    frame_botones,
    text="Busqueda Secuencial",
    command=buscar_secuencial,
    width=22,
    height=2,
    bg="#2874A6",
    fg="white",
    font=("Arial", 10, "bold")
)

boton_secuencial.grid(row=0, column=0, padx=8, pady=8)


boton_binaria = tk.Button(
    frame_botones,
    text="Busqueda Binaria",
    command=buscar_binaria,
    width=22,
    height=2,
    bg="#117864",
    fg="white",
    font=("Arial", 10, "bold")
)

boton_binaria.grid(row=0, column=1, padx=8, pady=8)


boton_hash = tk.Button(
    frame_botones,
    text="Busqueda Hash",
    command=buscar_hash,
    width=22,
    height=2,
    bg="#7D3C98",
    fg="white",
    font=("Arial", 10, "bold")
)

boton_hash.grid(row=1, column=0, padx=8, pady=8)


boton_registros = tk.Button(
    frame_botones,
    text="Mostrar Registros",
    command=mostrar_registros,
    width=22,
    height=2,
    bg="#D68910",
    fg="white",
    font=("Arial", 10, "bold")
)

boton_registros.grid(row=1, column=1, padx=8, pady=8)


boton_limpiar = tk.Button(
    frame_botones,
    text="Limpiar",
    command=limpiar,
    width=22,
    height=2,
    bg="#566573",
    fg="white",
    font=("Arial", 10, "bold")
)

boton_limpiar.grid(row=2, column=0, padx=8, pady=8)


boton_salir = tk.Button(
    frame_botones,
    text="Salir",
    command=ventana.destroy,
    width=22,
    height=2,
    bg="#C0392B",
    fg="white",
    font=("Arial", 10, "bold")
)

boton_salir.grid(row=2, column=1, padx=8, pady=8)


# ==============================================
# AREA DE RESULTADOS
# ==============================================

etiqueta_resultado = tk.Label(
    ventana,
    text="Resultados de la busqueda:",
    font=("Arial", 12, "bold"),
    bg="#EAF2F8",
    fg="#17365D"
)

etiqueta_resultado.pack(pady=10)


salida = tk.Text(
    ventana,
    width=75,
    height=15,
    font=("Consolas", 11),
    wrap="word",
    bg="white",
    fg="#17202A",
    relief="solid",
    borderwidth=1
)

salida.pack(padx=20, pady=10, fill="both", expand=True)

salida.insert(
    tk.END,
    "Escribe un dato y selecciona el metodo de busqueda."
)

salida.config(state="disabled")


ventana.mainloop()
