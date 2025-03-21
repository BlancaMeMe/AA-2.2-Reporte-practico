def es_par(numero):
    return numero % 2 == 0

def filtrar_datos(lista_datos, callback):
    resultado = []
    for dato in lista_datos:
        if callback(dato):  
            resultado.append(dato)
    return resultado

numeros = [2,3,5,6,9,10,12,15,18,20,21]

numeros_validos = filtrar_datos(numeros, es_par)

print(numeros_validos)
