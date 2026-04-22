# -*- coding: utf-8 -*-

from datetime import datetime

def validar_registro(registro):
    """
    Qué hace la función:
    Verifica que:
       - id_participante y  cantidad_uso: numeros enteros positivos y no nulos
       - tiempo_uso: numero positivo y no nulo
       - fecha y app no  vacíos
       - fecha tenga formato válido
    

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
    for valor in registro:
        
        if registro["app"] not in apps_validas:
                raise ValueError (f"App no valida: {registro["app"]}. Opciones: {apps_validas}")
        if registro["app"] == "":
                raise ValueError (" El campo app es vacío")
                
        if registro["cantidad_uso"] <= 0:
            raise ValueError("Cantidad de uso debe ser un entero positivo")
 
        if registro["tiempo_uso"] <= 0:
            raise ValueError("Tiempo de uso debe ser un numero positivo")
    
        if registro["id_participante"] <= 0: 
            raise ValueError(" El Id debe ser un número entero y positvo") 
        
        if datetime.strptime(registro["fecha"], "%Y-%m-%d") == False:
            raise ValueError ("Formato de fecha inválido. Formato esperado: ""AAAA-mm-dd")
        if registro["fecha"] == "":
            raise ValueError("El campo fecha es vacío")
            
    return True



       
