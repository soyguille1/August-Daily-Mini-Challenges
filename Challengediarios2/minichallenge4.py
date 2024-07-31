from collections import deque
grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}
def bfs(grafo, inicio_nodo):
    visitados = set()
    cola = deque([inicio_nodo])

    while cola:
        nodo = cola.popleft()
        if nodo not in visitados:
            print(nodo, end=' ')
            visitados.add(nodo)
            for vecino in grafo[nodo]:
                if vecino not in visitados:
                    cola.append(vecino)

inicio_nodo = 0
print("Recorrido BFS:")
bfs(grafo, inicio_nodo)
