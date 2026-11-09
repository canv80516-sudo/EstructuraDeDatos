def warshall(matriz_adyacencia):
    """
    Calcula la clausura transitiva de un grafo dirigido (matriz de conectividad).
    
    :param matriz_adyacencia: Matriz booleana o binaria (1 si hay arista, 0 si no).
    :return: Matriz de clausura transitiva (1 si existe algun camino, 0 en caso contrario).
    """
    n = len(matriz_adyacencia)
    # Crear una copia profunda de la matriz de entrada
    C = [fila[:] for fila in matriz_adyacencia]
    
    # Actualizacion iterativa basada en algebra booleana
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Operacion booleana: C[i][j] O (C[i][k] Y C[k][j])
                C[i][j] = C[i][j] or (C[i][k] and C[k][j])
                
    return C