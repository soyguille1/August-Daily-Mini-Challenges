grafo = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1],
    4: [1]
}

def dfs(grafo, nodo, visitados):
    visitados.add(nodo)
    print(nodo, end=' ')

    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)


visitados = set()
inicio_nodo = 0
print("Recorrido DFS:")
dfs(grafo, inicio_nodo, visitados)
