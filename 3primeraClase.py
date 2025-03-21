def marcar_presente(estudiante):
    return f"{estudiante} está presente"

def marcar_ausente(estudiante):
    return f"{estudiante} está ausente"

# Lista de estudiantes
estudiantes = ["Esmeralda", "Arashel", "Freddy", "Berenice","Manuel"]

estado_estudiante = "ausente"  #"presente" o "ausente"
marcar = marcar_presente if estado_estudiante == "presente" else marcar_ausente

asistencia = [marcar(estudiante) for estudiante in estudiantes]

for registro in asistencia:
    print(registro)
