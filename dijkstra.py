import heapq

def dijkstra(grafo, origen):
    """
    Calcula el camino mas corto desde un vertice origen a todos los demas
    en un grafo con pesos no negativos utilizando Dijkstra.
    
    :param grafo: Diccionario donde las claves son nodos y los valores son diccionarios de vecinos y pesos.
                  Ejemplo: {'A': {'B': 4, 'C': 2}, 'B': {'C': 1, 'D': 5}, ...}
    :param origen: Nodo de inicio del recorrido.
    :return: Tupla con (distancias minimas, predecesores para reconstruir rutas).
    """
    # Inicializar distancias con infinito y origen con 0
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[origen] = 0
    predecesores = {nodo: None for nodo in grafo}
    
    # Cola de prioridad que almacena tuplas: (distancia_acumulada, nodo)
    pq = [(0, origen)]
    
    while pq:
        dist_actual, u = heapq.heappop(pq)
        
        # Si la distancia encontrada es mayor a la registrada, se ignora (nodo obsoleto en heap)
        if dist_actual > distancias[u]:
            continue
            
        # Explorar vecinos del nodo actual
        for v, peso in grafo[u].items():
            distancia_alternativa = dist_actual + peso
            
            # Condicion de relajacion de aristas
            if distancia_alternativa < distancias[v]:
                distancias[v] = distancia_alternativa
                predecesores[v] = u
                heapq.heappush(pq, (distancia_alternativa, v))
                
    return distancias, predecesores

def reconstruir_camino(predecesores, destino):
    """Reconstruye el camino optimo desde el origen hasta el destino dado."""
    camino = []
    actual = destino
    while actual is not None:
        camino.insert(0, actual)
        actual = predecesores[actual]
    return camino