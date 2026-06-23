from validación import leer_entero

#-- Con respecto al menu----------------------------------------------------------------------------------
def mostrar_menu_principal():
    """
    Muestra el menú principal con las opciones de los sistemas disponibles.
    
    Parámetros: Ninguno.
    Retorna: Ninguno.
    """
    print ("=======Seleccione el número del sistema que desea utilizar======")
    print ("1. Reporte de turno")
    print ("2. Control de inventario")
    print ("================================================================")

def validar_opción_menu (minimo,maximo):
    """
    Solicita al usuario una opcion para el menu y valida que esté dentro del rango permitido.
    
    Parámetros:
    minimo (int): El valor numérico mínimo que representa una opción válida.
    maximo (int): El valor numérico máximo que representa una opción válida.
    
    Retorna:
    int: El número de la opción seleccionada y ya validado
    """
    opcion_menu = leer_entero("Número del sistema -> ",minimo,maximo)
    return opcion_menu

def opcion1():
    """
    Imprime un mensaje indicando que se ha seleccionado el sistema de Reporte de turno.
    
    Parámetros: Ninguno.
    Retorna: Ninguno.
    """
    print("Usted a elegido el sistema: Reporte de turno.")

def opcion2():
    """
    Imprime un mensaje indicando que se ha seleccionado el sistema de Control de inventario.
    
    Parámetros: Ninguno.
    Retorna: Ninguno.
    """
    print("Usted a elegido el sistema: Control de inventario.")

#-- Definiciones del codigo de Doña Carmen---------------------------------------------------------------------------------------------------------------------

def menu_sistema1 ():
    """
    Muestra el menú de opciones para el Reporte de turno
    
    Parámetros: Ninguno.
    Retorna: Ninguno.
    """
    print("======Seleccione la opción que usará en el sistema 'Reporte de turno'======" )
    print("1. Agregar datos de las líneas" )
    print("2. Reporte de las líneas" )
    print("3. Total producido/rechazado por las líneas" )
    print("4. Línea más eficiente" )
    print("5. Salir" )
    print("===========================================================================")

def mensaje_numero_registro(contador):
    """
    Imprime un encabezado indicando el número consecutivo del registro de datos actual.
    
    Parámetros:
    contador (int): El índice actual del ciclo de recolección de datos.
    
    Retorna:
    Ninguno.
    """
    print(f"Registro de datos #{contador + 1}")

def preguntar_cantidad_lineas():
    """
    Solicita al usuario la cantidad de líneas de producción que estuvieron activas durante el turno.
    
    Parámetros: Ninguno.
    
    Retorna:
    int: La cantidad de líneas activas (un valor entre 1 y 3).
    """
    cantidad_lineas = leer_entero("¿Cuántas líneas estuvieron activas en el turno? Ingrese un número entre 1 y 3: ",1,3)
    return cantidad_lineas

def mostrar_menu_lineas():
    """
    Muestra las líneas de producción disponibles (1, 2 o 3) y solicita al usuario que seleccione en cuál esta trabajando.
    
    Parámetros: Ninguno
    
    Retorna:
    int: El número de la línea seleccionada (1, 2 o 3)
    """
    print("Porfavor, seleccione la línea de produccion")
    print("1. Línea 1")
    print("2. Línea 2")
    print("3. Línea 3")

    opcion = leer_entero("Seleccione en cual línea está trabajando: ",1,3)
    return opcion

# recolecta datos de botellas
def recolectar_producidas ():
    """
    Solicita al usuario ingresar la cantidad total de botellas producidas en la línea que esta trabajando 
    
    Parámetros: Ninguno.
    
    Retorna:
    int: La cantidad total de botellas producidas.
    """
    producidas = leer_entero("Cantidad total de botellas producidas: ",1,9999999999999)
    return producidas

def recolectar_rechazadas ():
    """
    Solicita al usuario ingresar la cantidad de botellas que presentaron defectos o fueron rechazadas en esa linea de produccion.
    
    Parámetros: Ninguno.
    
    Retorna:
    int: La cantidad de botellas rechazadas.
    """
    rechazadas = leer_entero("Cantidad de botellas rechazadas (No puede ser mayor a las producidas): ",0,99999999999)
    return rechazadas

# -- Definicione del reporte final de Doña Carmen-------------------------------------------------------------------------------------------------------------
def encabezado_impresion_de_lineas():
    """
    Imprime el título para el reporte final de la planta.
    
    Parámetros: Ninguno.
    
    Retorna: Ninguno.
    """
    print("=== REPORTE DE TURNO - PLANTA COLIBRÍ ===")

def impresion_de_linea(linea,lineas_datos,eficiencia):
     """
    Muestra de forma final y ordenada las botellas producidas, rechazadas y el porcentaje de eficiencia de una línea específica.
    
    Parámetros:
    linea (int): El número que indica la línea de producción.
    lineas_datos (diccionario): El diccionario que almacena los datos acumulados de las producidas y rechazadas
    eficiencia (float): El porcentaje de eficiencia calculado  mediante la formula de eficiencias para la línea.
    
    Retorna: Ninguno.
    """
     print(f"Línea {linea}: {lineas_datos[linea]["producidas"]} producidas | {lineas_datos[linea]["rechazadas"]} rechazadas | Eficiencia: {eficiencia:.2f}%")

def impresion_total_producido_rechazado(total_producido,total_rechazado):
    """
    Muestra la suma del acumulado de botellas producidas y rechazadas en el turno
    
    Parámetros:
    total_producido (int): La suma total de botellas fabricadas por todas las líneas.
    total_rechazado (int): La suma total de botellas defectuosas de todas las líneas.
    
    Retorna: Ninguno.
    """
    print(f"TOTAL PRODUCIDO: {total_producido} botellas")
    print(f"TOTAL RECHAZADO: {total_rechazado} botellas")

def impresion_linea_eficiente(mejor_linea,mejor_eficiencia):
    """
    Muestra cuál fue la linea mas eficiente, asi como tambien el porcentaje correspondiente 
    
    Parámetros:
    mejor_linea (str): El nombre de la línea que obtuvo el porcentaje más alto.
    mejor_eficiencia (float): El porcentaje de eficiencia más alto registrado en el turno.
    
    Retorna: Ninguno.
    """
    print(f"LÍNEA MÁS EFICIENTE: {mejor_linea} ({mejor_eficiencia:.2f}%)")

# -- Definiciones del codigo de Don Esteban -------------------------------------------------------------------------------------------------------------------------------------------

def cantidad_vacias_y_consumo ():
    
    ### pregunta la cantidad de botellas vacías.
    botellas_vacias = leer_entero("Por favor, digite la cantidad de botellas vacías que hay actualmente en bodega:   ",0,9999999999999)
        
    ### pregunta el promedio de consumo diario
    consumo_botellas = leer_entero("Por favor, digite cuántas botellas se consumen en promedio por día:  ",0,999999999999)
    return (botellas_vacias,consumo_botellas)

def alerta_no_botellas(opcion):
    if opcion == 1:
        print ("No hay botellas vacías en el inventario.")
    if opcion == 2:
        print ("No existe consumo de botellas.")
    if opcion == 3:
        print("¡¡ALERTA!! Inventario crítico. Hay menos de 500 botellas en el inventario.")

def alerta_dias_con_botellas(opcion,dia,botellas_vacias,proximos_dias):
    if opcion ==1:
        print(f"Día {dia}: {botellas_vacias} botellas vacías")
    if opcion ==2:
        print(
                f"¡¡ALERTA!! Inventario crítico. " ###se enseña una alerta al usuario cuando falte un día para el desabastecimiento.
                f"Quedan {proximos_dias:.2f} días antes del desabastecimiento.")


