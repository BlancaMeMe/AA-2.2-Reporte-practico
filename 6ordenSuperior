def area_circulo(radio):
    return 3.14 * radio ** 2

def area_cuadrado(lado):
    return lado ** 2

def calcular_area(figura):
    if figura[1] == "circulo":
        return area_circulo(figura[0])
    elif figura[1] == "cuadrado":
        return area_cuadrado(figura[0])

figuras = [(5, 'circulo'), (4, 'cuadrado')]

areas = list(map(calcular_area, figuras))

print(areas)
