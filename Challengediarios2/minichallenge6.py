class NodoBST:
    def __init__(self, clave):
        self.clave = clave
        self.izquierda = None
        self.derecha = None

def insertar(raiz, clave):
    if raiz is None:
        return NodoBST(clave)
    if clave < raiz.clave:
        raiz.izquierda = insertar(raiz.izquierda, clave)
    else:
        raiz.derecha = insertar(raiz.derecha, clave)
    return raiz

def recorrido_en_orden(raiz):
    if raiz:
        recorrido_en_orden(raiz.izquierda)
        print(raiz.clave, end=" ")
        recorrido_en_orden(raiz.derecha)

claves = [15, 10, 20, 8, 12]
raiz_bst = None
for clave in claves:
    raiz_bst = insertar(raiz_bst, clave)

recorrido_en_orden(raiz_bst)
