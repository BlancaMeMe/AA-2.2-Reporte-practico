def calcular_uso_ancho_banda(datos_transferidos, tiempo_segundos):
    return datos_transferidos / tiempo_segundos  # Mbps

datos = 500  # Megabits transferidos
tiempo = 20  # Segundos
print(f"Uso de ancho de banda: {calcular_uso_ancho_banda(datos, tiempo)} Mbps")
