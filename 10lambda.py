estudiantes = [("Esmeralda", 85), ("Arashel", 45), ("Manuel", 78), ("Berenice", 89), ("Freddy", 78)]
aprobados = list(filter(lambda x: x[1] >= 60, estudiantes))
print(aprobados)  # [('Juan', 85), ('Luis', 78)]
