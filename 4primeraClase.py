def ordenar_ascendente(lista):
    return sorted(lista)

def ordenar_descendente(lista):
    return sorted(lista, reverse=True)

orden = ordenar_descendente 
print(orden([5, 2, 4, 1, 8, 3, 7, 6]))
orden = ordenar_ascendente 
print(orden([5, 2, 4, 1, 8, 3, 7, 6]))
