import heapq

class ColaPrioridad:
    def __init__(self):
        self._data = []
        self._index = 0

    def insertar(self, elemento, prioridad):
        heapq.heappush(self._data, (-prioridad, self._index, elemento))
        self._index += 1

    def eliminar(self):
        return heapq.heappop(self._data)[-1]

cola = ColaPrioridad()

cola.insertar("tarea1", 23)
cola.insertar("tarea2", 12)
cola.insertar("tarea3", 40)
cola.insertar("tarea4", 23)

print(cola.eliminar())
print(cola.eliminar())
print(cola.eliminar())
print(cola.eliminar()) 
