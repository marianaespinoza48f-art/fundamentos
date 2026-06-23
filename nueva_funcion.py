#nueva_funcion.py 
def evaluar_meta_calidad(eficiencia_linea):
    """
    Evalúa la eficiencia de la línea en cuestion y retorna un mensaje si no alcanza la meta con un estándar mínimo 
    establecido en la planta del 95.0% para cualquier linea de produccion. Si la eficiencia es menor se retorna un mensaje de alerta para el reporte.
    
    Parametros:
    eficiencia_linea (float): El porcentaje de eficiencia calculado para la línea de producción.
        
    Returna:
    string: Un mensaje de alerta si la línea no cumple la meta de la planta. 
    O por otro lado, una cadena vacía "" si la línea opera de manera óptima (>= 95.0%).
    """
    meta_minima = 95.0
    
    # Si baja del 95%, está mal y se genera el mensaje de alerta 
    if eficiencia_linea < meta_minima:
        return "¡ALERTA!. Eficiencia menor al 95%"
    
    # De otro modo, si es igual o mayor a 95%, está bien y no devuelve texto
    return ""