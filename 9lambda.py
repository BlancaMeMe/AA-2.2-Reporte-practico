proyectos = [("IA", 1), ("Redes", 3), ("Web", 2)]
proyectos_ordenados = sorted(proyectos, key=lambda x: x[1])
print(proyectos_ordenados)  # [('Web', 1), ('IA', 2), ('Redes', 3)]
