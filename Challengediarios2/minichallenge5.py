import heapq

def heuristica(nodo, objetivo):
    return abs(ord(nodo) - ord(objetivo))

def a_estrella(grafo, inicio, objetivo):
    conjunto_abierto = [(0, inicio)]
    heapq.heapify(conjunto_abierto)

    costos_g = {nodo: float('infinity') for nodo in grafo}
    costos_g[inicio] = 0

    costos_f = {nodo: float('infinity') for nodo in grafo}
    costos_f[inicio] = heuristica(inicio, objetivo)

    camino_desde = {}

    while conjunto_abierto:
        actual = heapq.heappop(conjunto_abierto)[1]

        if actual == objetivo:
            camino = []
            while actual in camino_desde:
                camino.append(actual)
                actual = camino_desde[actual]
            camino.append(inicio)
            return camino[::-1]

        for vecino, peso in grafo[actual].items():
            puntaje_g_tentativo = costos_g[actual] + peso

            if puntaje_g_tentativo < costos_g[vecino]:
                camino_desde[vecino] = actual
                costos_g[vecino] = puntaje_g_tentativo
                costos_f[vecino] = puntaje_g_tentativo + heuristica(vecino, objetivo)
                heapq.heappush(conjunto_abierto, (costos_f[vecino], vecino))

    return None  

grafo = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'E': 1},
    'D': {'B': 5, 'E': 3},
    'E': {'C': 1, 'D': 3}
}

nodo_inicio = 'A'
nodo_objetivo = 'D'
camino_mas_corto = a_estrella(grafo, nodo_inicio, nodo_objetivo)
print(f"El camino mas corto entre {nodo_inicio} y {nodo_objetivo} es: {' -> '.join(camino_mas_corto)}")
