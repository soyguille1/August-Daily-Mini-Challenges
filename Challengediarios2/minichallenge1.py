def binary(list,low,high,x):
    print(low, high)
    if high >= low:
        mid = (high + low)//2
        if list[mid] == x:
            return mid
        elif list[mid] > x:
            return binary(list, low, mid -1, x)
        else: return binary(list, mid +1, high,x)
    else:
        return -1     
list=[1,2,3,4,5,6,7,8,9,10]
x= int(input(f"ingrese el valor que desea buscar en la lista"))
result = binary(list, 0, len(list) - 1, x)

if result != -1:
    print(f"Elemento encontrado en el indice {result}")
else:
    print("Elemento no encontrado en la lista")