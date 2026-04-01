# -*- coding: utf-8 -*-


def validar_registro(registro):
    """
    Qué hace la función:
    Verifica que:
       - id_participante y  antidad_uso: numeros enteros positivos y no nulos
       - tiempo_uso: numero positivo y no nulo
       - app: str
       - ningún campo esté vacío
    

    Parameteros
    ----------
    registro: dicc
    registro de un participante

    Retorna
    -------
   - False: bool
   si hay algún dato inválido
   - True: bool
   si los datos son todos válidos

    """
    # Verificar que no haya campos vacíos
    for valor in registro.values():
        if valor == "" or valor is None:
            return False
        # Verificar valores positivos
        if (registro["id_participante"] <= 0 or
           registro["cantidad_uso"] <= 0 or
           registro["tiempo_uso"] <= 0):
            return False
    return True


       