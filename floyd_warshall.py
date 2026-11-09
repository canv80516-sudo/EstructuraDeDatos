def floyd_warshall(grafo_matriz):
    """
    Calcula los caminos mas cortos entre todos los pares de vertices.
    
    :param grafo_matriz: Matriz de adyacencia (lista de listas). 
                         Usar float('inf') si no existe arista directa y 0 en la diagonal.
    :return: Matriz con las distancias minimas entre todos los pares.
    """
    num_vertices = len(grafo_matriz)
    # Copiar la matriz para evitar modificar la original
    dist = [fila[:] for fila in grafo_matriz]
    
    # Algoritmo principal de Programacion Dinamica
    for k in range(num_vertices):
        for i in range(num_vertices):
            for j in range(num_vertices):
                # Si pasar por el nodo k ofrece un camino mas corto, actualizar
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    
    # Deteccion opcional de ciclos de peso negativo
    for i in range(num_vertices):
        if dist[i][i] < 0:
            raise ValueError("El grafo contiene un ciclo de peso negativo.")
            
    return dist