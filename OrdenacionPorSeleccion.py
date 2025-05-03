def encuentraMenor(array):
    menor = array[0]
    indice_menor = 0
    for i in range(1, len(array)):
        if array[i] < menor:
            menor = array[i]
            indice_menor = i
    return indice_menor
    
def OrdenacionPorSeleccion(array):
    nuevoArr = []
    for i in range(len(array)):
        menor = encuentraMenor(array)
        nuevoArr.append(array.pop(menor))
    return nuevoArr

print("ESTO ES ORDENACION POR SELECCION")
print("*"*20)
print(OrdenacionPorSeleccion([5, 3, 6, 2, 10,42,34,12,4,2,67]))