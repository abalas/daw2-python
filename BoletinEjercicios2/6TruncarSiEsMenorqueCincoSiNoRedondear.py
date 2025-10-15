from os import truncate


def cumpleRango(n):
    return 0 <= n <= 10

datosIncorrectos = True

while datosIncorrectos:
    notaTrabajoEnClase = float(input("Introduzca la nota de trabajo en clase: "))
    notaEjerciciosPracticos = float(input("Introduzca la nota de los ejercicios prácticos: "))
    notaExamen = float(input("Introduzca la nota del examen: "))

    if cumpleRango(notaTrabajoEnClase) and cumpleRango(notaEjerciciosPracticos) and cumpleRango(notaExamen):
        media = notaTrabajoEnClase * 0.05 + notaEjerciciosPracticos * 0.15 + notaExamen * 0.80
        if media<5:
            truncate(media)
        else :
            print("La nota final es:", media)
            datosIncorrectos = False  # ✅ Salimos del bucle
    else:
        print("Alguna nota es incorrecta. Introduce valores entre 0 y 10.")