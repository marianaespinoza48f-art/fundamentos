from enviayrecolecta import fecha

def leer_reporte(fecha):
    try:

        with open (f"reporte_{fecha}.txt", "r") as archivo:
            reporte = archivo.read()
            print(reporte)
    except FileNotFoundError:
        print("El archivo no existe, o no ha sido encontrado")


def guardar_reporte(lineas_datos, total_producido, total_rechazado,
                     mejor_linea, mejor_eficiencia,
                     linea1, linea2, linea3, fecha):
    nombre_archivo = f"reporte_{fecha}.txt"


    with open(nombre_archivo, "w") as archivo:


        archivo.write("=== REPORTE DE TURNO - PLANTA COLIBRÍ ===\n\n")

        if lineas_datos[1]["producidas"] > 0:
            archivo.write(
                f"Línea 1: {lineas_datos[1]['producidas']} producidas | "
                f"{lineas_datos[1]['rechazadas']} rechazadas | "
                f"Eficiencia: {linea1:.2f}%\n"
            )

        if lineas_datos[2]["producidas"] > 0:
            archivo.write(
                f"Línea 2: {lineas_datos[2]['producidas']} producidas | "
                f"{lineas_datos[2]['rechazadas']} rechazadas | "
                f"Eficiencia: {linea2:.2f}%\n"
            )

        if lineas_datos[3]["producidas"] > 0:
            archivo.write(
                f"Línea 3: {lineas_datos[3]['producidas']} producidas | "
                f"{lineas_datos[3]['rechazadas']} rechazadas | "
                f"Eficiencia: {linea3:.2f}%\n"
            )

        archivo.write("\n")
        archivo.write(f"TOTAL PRODUCIDO: {total_producido}\n")
        archivo.write(f"TOTAL RECHAZADO: {total_rechazado}\n")
        archivo.write(f"LÍNEA MÁS EFICIENTE: {mejor_linea}\n")
        archivo.write(f"EFICIENCIA: {mejor_eficiencia:.2f}%\n")