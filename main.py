#Aquí estara el main
import enviayrecolecta 
import calcymodelo




#controla que funciones va a llamar según el sistema elegido
def sistema(opcion):
    """
    Controla el flujo del programa dirigiendo al usuario hacia el sistema seleccionado desde el menú principal
    
    Parámetros:
    opcion (int): El número del sistema elegido 
    
    Retorna: Ninguno
    """
    if opcion == 1:
        llamar_sistema1()

    if opcion ==2:
        llamar_sistema2()
        
def llamar_sistema1():
    """
    Gestiona la interacción del sistema de "Reporte de turno", coordinando la captura de datos, cálculos de rendimiento y visualización de reportes 
    hasta que el usuario decida salirse.
    
    Parámetros: Ninguno.
    
    Retorna: Ninguno
    """
    enviayrecolecta.menu_sistema1()
    opcion=enviayrecolecta.validar_opción_menu(1,5)
    while opcion != 5:
        if opcion ==1:
            cantidad = enviayrecolecta. preguntar_cantidad_lineas ()
            (lineas_datos,total_producido, total_rechazado,eficiencias) = calcymodelo. recoleccion_datos_lineas (cantidad,0,0)
            
            (mejor_eficiencia,linea1,linea2,linea3) = calcymodelo. calculo_linea_eficiente(eficiencias)
            mejor_linea = calcymodelo. linea_mas_eficiente(mejor_eficiencia,linea1,linea2,linea3)
            enviayrecolecta.menu_sistema1()
            opcion=enviayrecolecta.validar_opción_menu(1,5)
        
        if opcion == 2:
            calcymodelo.reporte_de_linea (lineas_datos,linea1,linea2,linea3)
            enviayrecolecta.menu_sistema1()
            opcion=enviayrecolecta.validar_opción_menu(1,5)

        if opcion == 3:
            enviayrecolecta. impresion_total_producido_rechazado(total_producido,total_rechazado)
            enviayrecolecta.menu_sistema1()
            opcion=enviayrecolecta.validar_opción_menu(1,5)

        if opcion == 4:
            enviayrecolecta. impresion_linea_eficiente (mejor_linea,mejor_eficiencia)
            enviayrecolecta.menu_sistema1()
            opcion=enviayrecolecta.validar_opción_menu(1,5)

def llamar_sistema2():
    (vacias,consumo)=enviayrecolecta.cantidad_vacias_y_consumo()
    calcymodelo.comprobacion_botellas_no0(vacias,consumo)
    calcymodelo.cantidad_dias_con_botellas(vacias,consumo)

#Main principal 
def main ():
    """
    Entrada principal del programa. Interfaz de usuario y arrancar la ejecución del mismo
    
    Parámetros: Ninguno
    
    Retorna: Ninguno.
    """
    enviayrecolecta. mostrar_menu_principal()
    opcion= enviayrecolecta. validar_opción_menu(1,2)
    calcymodelo. dice_opcion_menu(opcion)
    sistema(opcion)


    

main()