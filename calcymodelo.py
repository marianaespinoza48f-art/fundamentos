# -- Calculos y procesos---------------------------------------------------------------------
import enviayrecolecta
###amo a keiry godinez
def dice_opcion_menu(opcion): eso tilin
    """
    Evalúa la opción seleccionada del menú principal y llama a la función correspondiente en el módulo de envíayrecolecta
    
    Parámetros:
    opcion (int): El número de sistema elegido por el usuario (1 para Reporte de turno, 2 para Control de inventario)
    
    Retorna: Ninguno
    """
    if opcion == 1:
        enviayrecolecta.opcion1()
        
    if opcion == 2:
        enviayrecolecta.opcion2()

# -- Sistema de Doña Carmen ---------------------------------------------------------------------------------------------------

def recoleccion_datos_lineas(cantidad_lineas,total_producido,total_rechazado):
    """
    Captura de datos de botellas producidas y rechazadas para cada línea activa y controlando que las piezas rechazadas no superen a las producidas.
    
    Parámetros:
    cantidad_lineas (int): El número de registros de líneas activas que se van a capturar durante el turno.
    total_producido (int): El acumulador de botellas totales producidas en la planta
    total_rechazado (int): El acumulador de botellas totales rechazadas en la planta.
    
    Retorna:
    tupla: La cual contiene:
        - diccionario: Que tiene los totales de botellas producidas y rechazadas por cada línea (1, 2 y 3).
        - int: El total final de botellas producidas de todo el turno
        - int: El total final de botellas rechazadas de todo el turno
        - int: Eficiencias del las líneas.
    """
    
    lineas_datos = {
            1: {"producidas": 0, "rechazadas": 0},
            2: {"producidas": 0, "rechazadas": 0},
            3: {"producidas": 0, "rechazadas": 0}
        }
    
    for contador in range(cantidad_lineas):
        enviayrecolecta.mensaje_numero_registro(contador)

        linea = enviayrecolecta.mostrar_menu_lineas()
        producidas = enviayrecolecta.recolectar_producidas()
        rechazadas = enviayrecolecta.recolectar_rechazadas()

        while rechazadas > producidas:
            rechazadas = enviayrecolecta. recolectar_rechazadas()
            

        # Se realiza la suma sin importar que linea es, mejorando cambios a futuro
        lineas_datos[linea]["producidas"] += producidas
        lineas_datos[linea]["rechazadas"] += rechazadas

        total_producido += producidas
        total_rechazado += rechazadas
    eficiencias= calculo_porcentaje_eficiente(lineas_datos) 
    
    return (lineas_datos,total_producido,total_rechazado,eficiencias)

def calculo_porcentaje_eficiente(lineas_datos):
    """
    Calcula el porcentaje de eficiencia de forma independiente para cada línea de producción 
    que haya registrado botellas fabricadas, aqui se cuida que este numero sea mayor que cero 
    
    Parámetros:
    lineas_datos (dict): La estructura con las botellas producidas y rechazadas de cada línea de producción.
    
    Retorna:
    diccionario: Un diccionario con el porcentaje eficiencia  el cual es un float, calculado por cada número de línea activa
    """
    eficiencias = {}
    if lineas_datos[1]["producidas"] > 0:
        eficiencias[1] = ((lineas_datos[1]["producidas"] - lineas_datos[1]["rechazadas"]) / lineas_datos[1]["producidas"]) * 100


    if lineas_datos[2]["producidas"] > 0:
        eficiencias[2] = ((lineas_datos[2]["producidas"] - lineas_datos[2]["rechazadas"]) / lineas_datos[2]["producidas"]) * 100

    if lineas_datos[3]["producidas"] > 0:
        eficiencias[3] = ((lineas_datos[3]["producidas"] - lineas_datos[3]["rechazadas"]) / lineas_datos[3]["producidas"]) * 100
    return eficiencias

def calculo_linea_eficiente(eficiencias):
    """
    Analiza el valor máximo de rendimiento entre los porcentajes de eficiencia de las tres líneas de la planta
    
    Parámetros:
    eficiencias (dict): Un diccionario que contiene los porcentajes calculados para las líneas de producción activas
    
    Retorna:
    tuple: Una colección organizada con los siguientes datos:
        - float: El porcentaje de eficiencia más alto registrado en el turno.
        - float: El rendimiento final calculado para la línea 1 (0 si no estuvo activa)
        - float: El rendimiento final calculado para la línea 2 (0 si no estuvo activa)
        - float: El rendimiento final calculado para la línea 3 (0 si no estuvo activa)
    """
# -- Para la linea 1 --------------------------------------------------------------------
    if 1 in eficiencias:
     eficiencia_linea_1 = eficiencias[1]
    else:
     eficiencia_linea_1 = 0

# -- Para la Línea 2 ---------------------------------------------------------------------
    if 2 in eficiencias:
        eficiencia_linea_2 = eficiencias[2]
    else:
        eficiencia_linea_2 = 0

# -- Para la Línea 3 --------------------------------------------------------------------
    if 3 in eficiencias:
      eficiencia_linea_3 = eficiencias[3]
    else:
     eficiencia_linea_3 = 0

    mejor_eficiencia = max(eficiencia_linea_1, eficiencia_linea_2, eficiencia_linea_3)
    return (mejor_eficiencia,eficiencia_linea_1,eficiencia_linea_2,eficiencia_linea_3)

def linea_mas_eficiente(mejor_eficiencia,eficiencia_linea_1,eficiencia_linea_2,eficiencia_linea_3):
    """
    Asigna el nombre correspondiente a la línea de producción que obtuvo el mayor porcentaje de rendimiento en la planta durante el turno
    
    Parámetros:
    mejor_eficiencia (float): El porcentaje de eficiencia máximo obtenido en el turno
    eficiencia_linea_1 (float): El porcentaje individual de rendimiento de la línea 1
    eficiencia_linea_2 (float): El porcentaje individual de rendimiento de la línea 2
    eficiencia_linea_3 (float): El porcentaje individual de rendimiento de la línea 3
    
    Retorna:
    str: El nombre de la linea mas eficiente 
    """
    mejor_linea = ""
    if mejor_eficiencia == eficiencia_linea_1 and eficiencia_linea_1 > 0:
        mejor_linea = "Línea 1"
    elif mejor_eficiencia == eficiencia_linea_2 and eficiencia_linea_2 > 0:
        mejor_linea = "Línea 2"
    elif mejor_eficiencia == eficiencia_linea_3 and eficiencia_linea_3 > 0:
        mejor_linea = "Línea 3"
    else:
        mejor_linea = "Ninguna línea estuvo activa"
    return mejor_linea

def reporte_de_linea(lineas_datos,eficiencia_linea_1, eficiencia_linea_2, eficiencia_linea_3):
    """
    Ordena la print del reporte detallado que se mostrara, el cual solo para aquellas líneas que registraron botellas producidas
    
    Parámetros:
    lineas_datos (diccionario): El diccionario con la información acumulada de botellas producidas y rechazadas.
    eficiencia_linea_1 (float): El porcentaje de eficiencia final de la línea 1
    eficiencia_linea_2 (float): El porcentaje de eficiencia final de la línea 2
    eficiencia_linea_3 (float): El porcentaje de eficiencia final de la línea 3.
    
    Retorna: Ninguno
    """
    if lineas_datos[1]["producidas"] > 0:
        numero_linea = 1
        enviayrecolecta. impresion_de_linea(numero_linea,lineas_datos,eficiencia_linea_1)
        

    if lineas_datos[2]["producidas"] > 0:
        numero_linea = 2
        enviayrecolecta. impresion_de_linea(numero_linea,lineas_datos,eficiencia_linea_2)
        
        
    if lineas_datos[3]["producidas"] > 0:
        numero_linea = 3
        enviayrecolecta. impresion_de_linea(numero_linea,lineas_datos,eficiencia_linea_3)

# -- Sistema Don Esteban ---------------------------------------------------------------------------------------------------------------------------

def comprobacion_botellas_no0 (botellas_vacias, consumo_botellas):
    # En caso de que no hayan botellas o consumo.
    if  botellas_vacias == 0:
        enviayrecolecta.alerta_no_botellas(1)

    if  consumo_botellas == 0:
        enviayrecolecta.alerta_no_botellas(2)

    if botellas_vacias < 500 and (botellas_vacias == 0 or consumo_botellas == 0):
        enviayrecolecta.alerta_no_botellas(3)



def cantidad_dias_con_botellas(botellas_vacias, consumo_botellas):
    dia: int=1
    MINIMO= 500
    alerta_mostrada: bool= False

       ###se empieza el ciclo con la condición de que la cantidad de botellas vacías sea mayor a cero.
    while botellas_vacias > 0 and consumo_botellas > 0:
        botellas_vacias -= consumo_botellas ###se le resta a la cantidad de botellas vacías el consumo diario (promedio de consumo).
        enviayrecolecta.alerta_dias_con_botellas (1,dia,botellas_vacias,0)
        

        if botellas_vacias <= MINIMO and botellas_vacias > 0 and not alerta_mostrada: ###evaluar si la cantidad de botellas vacías es menor o igual al mínimo establecido (500) y a la vez mayor a cero.
            proximos_dias = botellas_vacias / consumo_botellas ###las condiciones del if son para evitar la dividión entre cero.
            enviayrecolecta.alerta_dias_con_botellas (2,dia,botellas_vacias,proximos_dias)

            
            alerta_mostrada = True

        dia += 1
