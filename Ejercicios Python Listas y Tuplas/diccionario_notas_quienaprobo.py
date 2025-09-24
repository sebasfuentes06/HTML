estudiantes={"ana":85, "luis":58, "pedro":70, "sofia":45, "maria":90}
aprobados={nombre:notas for nombre, notas in estudiantes.items() if notas >=60}
print("estudiante aprobados", aprobados)