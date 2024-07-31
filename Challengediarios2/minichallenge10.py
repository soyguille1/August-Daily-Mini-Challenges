from collections import OrderedDict

def eliminar_duplicados_orden(lista):
    return list(OrderedDict.fromkeys(lista))

mi_lista_ordenada = [2, 4, 4, 4, 4, 4, 9, 9]
lista_sin_duplicados_orden = eliminar_duplicados_orden(mi_lista_ordenada)
print(lista_sin_duplicados_orden)
