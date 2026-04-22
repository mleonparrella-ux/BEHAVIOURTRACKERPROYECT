# -*- coding: utf-8 -*-


def validar_registro(registro):
    """
    Qué hace la función:
    Verifica que:
       - id_participante y  cantidad_uso: numeros enteros positivos y no nulos
       - tiempo_uso: numero positivo y no nulo
       - app: str
       - los datos (strings) no esten vacíos
    

    Parameteros
    ----------
    registro: dicc
    registro de un participante

    Retorna
    -------
   - ValueError si es un dato inválido
   - True: si los datos son todos válidos

    """
    # Verificar que no haya campos vacíos
    apps_validas = ["Twitter", "Instagram", "Facebook", "Tiktok", "Whatsapp"] 
    for valor in registro.values():
        if app not in apps:
            raise ValueError (f"App no valida: {app}. Opciones: {apps_validas}")

        if cantidad_uso <= 0:
            raise ValueError("Cantidad de uso debe ser un entero positivo")

        if tiempo_uso <= 0:
            raise ValueError("Tiempo de uso debe ser un numero positivo")
    
        if valor == "": #para los strings (fecha y app)
            raise ValueError(" El campo fecha o app es vacío") #me lo dijo chat, aclarar en readme
            
        # Verificar valores positivos
            # y verificar dni de 8 dígitos
        if (registro["id_participante"]) <= 0 or (len(str(registro["id_participante"])) != 8):
            raise ValueError("El dni debe ser un número positivo de ocho dígitos")
            
        if registro["cantidad_uso"] <= 0:
            raise ValueError("La cantidad de uso debe ser un número positivo")
            
        if registro["tiempo_uso"] <= 0:
            raise ValueError("El tiempo de uso debe ser un número positivo")
            
            
    return True


       
