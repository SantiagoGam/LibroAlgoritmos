def BusquedaBinaria(lista, elemento):
    menor = 0
    mayor = len(lista)-1

    while menor <= mayor:
        medio = (menor+mayor)//2
        estimado = lista[medio]
        if estimado == elemento:
            return medio
        if estimado > elemento:
            mayor = medio-1

        else:
            menor=medio+1
    
    return None
lista=[1, 3, 5, 7, 9, 11, 23, 45]

print(BusquedaBinaria(lista, 3))
