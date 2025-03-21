
def imprimir_mensaje(mensaje):
    print(mensaje)

def ejecutar_callback(callback, mensaje):
    callback(mensaje)  

ejecutar_callback(imprimir_mensaje, "Bienvenido al Instituto Tecnologico Superior de Felipe Carrillo Puerto")
