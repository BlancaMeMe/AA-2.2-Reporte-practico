def descuento_alto(pago):
    return pago * 0.20  # 80% de descuento

def descuento_medio(pago):
    return pago * 0.70  # 30% de descuento

def descuento_bajo(pago):
    return pago * 0.75  # 25% de descuento

def aplicar_descuento(promedio, calcular_descuento):
    if promedio >= 90:
        return calcular_descuento(1700)  
    elif promedio >= 75:
        return calcular_descuento(1700)
    else:
        return 1700 

calculo_descuento = descuento_alto  

promedio_calificacion = 90
monto_con_descuento = aplicar_descuento(promedio_calificacion, calculo_descuento)

print(f"Monto a pagar con descuento: ${monto_con_descuento}")
