import random
import time

def crear_matriz(num_alumnos, num_materias):
    return [
        [random.randint(60, 100) for _ in range(num_materias)]
        for _ in range(num_alumnos)
    ]


def buscar_calificacion(matriz, alumno, materia):
    inicio = time.perf_counter()
    calif = matriz[alumno - 1][materia - 1]
    fin = time.perf_counter()
    tiempo = fin - inicio
    return calif, tiempo


def buscar_alumno_completo(matriz, alumno, num_materias):
    fila = []
    for materia in range(1, num_materias + 1):
        calif, _ = buscar_calificacion(matriz, alumno, materia)
        fila.append(calif)
    return fila




def mostrar_tabla(matriz, num_alumnos, num_materias, alumno_inicio=1, alumno_fin=None):
    if alumno_fin is None:
        alumno_fin = num_alumnos

    # Encabezado
    encabezado = f"{'Alumno':<10}"
    for m in range(1, num_materias + 1):
        encabezado += f"Materia{m:<5}"
    print(encabezado)

    # Filas
    for alumno in range(alumno_inicio, alumno_fin + 1):
        fila = buscar_alumno_completo(matriz, alumno, num_materias)
        linea = f"{alumno:<10}"
        for calif in fila:
            linea += f"{calif:<12}"
        print(linea)


if __name__ == "__main__":
    NUM_ALUMNOS = 10000
    NUM_MATERIAS = 100000

    calificaciones = crear_matriz(NUM_ALUMNOS, NUM_MATERIAS)

    calif, tiempo = buscar_calificacion(calificaciones, 321, 5)
    print(f"Alumno 321 - Materia 5 -> Calificación: {calif}")
    print(f"Tiempo de búsqueda: {tiempo:.8f} segundos\n")

    # Tabla completa
    print(f"Tabla de calificaciones ({NUM_ALUMNOS} alumnos, {NUM_MATERIAS} materias):")
    mostrar_tabla(calificaciones, NUM_ALUMNOS, NUM_MATERIAS)
