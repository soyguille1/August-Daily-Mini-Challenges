def burbujasort(array):
    length = len(array) - 1
    for i in (0, length):
        for j in range(0,length):
            if array[j] > array[j + 1]:
                aux = array [j]
                array[j] = array[j + 1]
                array[j + 1] = aux
    return array
scores = [70,90,0,80,60,85]
print("Antes de ordenar: ")
print(scores)
print("Luego de ordenar: ")
print(burbujasort(scores))