def leer_entero (mensaje, minimo, maximo):
    """
    Solicita al usuario un número entero y valida que se encuentre dentro del rango permitido, repitiendo la solicitud en caso de error ya que esta protegido con ValueError
    
    Parámetros:
    mensaje (str): El texto que se le muestra al usuario para solicitar el dato.
    minimo (int): El valor entero mínimo aceptable
    maximo (int): El valor entero máximo aceptable
    
    Retorna:
    int: El número entero ingresado por el usuario que cumple con el rango establecido.
    """
    while True: 
        try:
            entero=int (input (mensaje))
            if (entero>=minimo and maximo>=entero):
                return entero
            else: 
                print("Está fuera del rango")
        except ValueError:
            print("Error: Valor incorrecto, digite un numero entero")




    

def leer_decimal(mensaje, minimo, maximo):
    """
    Solicita al usuario un número decimal y valida que se encuentre dentro del rango permitido, y ademas teniendo en cuenta las excepciones de entrada incorrecta
    
    Parámetros:
    mensaje (str): El texto que se le muestra al usuario para solicitar el dato.
    minimo (float): El valor decimal mínimo aceptable.
    maximo (float): El valor decimal máximo aceptable
    
    Retorna:
    float: El número decimal ingresado por el usuario que cumple con el rango establecido.
    """
    while True: 
        try:
            decimal=float (input (mensaje))
            if (decimal>=minimo and maximo>=decimal):
                return decimal
            else: 
                print("Está fuera del rango")
        except ValueError:
            print("Error: Valor incorrecto, digite un numero real")
    

def leer_texto(mensaje, largo_min, largo_max):
    """
    Solicita al usuario una cadena de texto y valida que el largo de los caracteres se encuentre dentro de los límites mínimo y máximo establecidos.
    
    Parámetros:
    mensaje (str): El texto que se le muestra al usuario para solicitar el dato.
    largo_min (int): La cantidad mínima de caracteres que debe tener el texto
    largo_max (int): La cantidad máxima de caracteres permitida para el texto
    
    Retorna:
    str: La cadena de texto ingresada por el usuario que cumple con la longitud validada
    """
    
    while True: 
        try:
            texto=(input (mensaje))
            longitud=len(texto)
            if (longitud>=largo_min and largo_max>=longitud):
                return texto
            else: 
                print("Está fuera de la longitud")
        except ValueError:
            print("Error: Valor incorrecto, digite un texto con longitud adecuada")
    
