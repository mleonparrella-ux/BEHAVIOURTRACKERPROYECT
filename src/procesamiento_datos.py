def filtrar_por_participante(datos, id_participante):
    """
    Filtra los datos de un participante específico.

    Parámetros:
    datos (list): Lista de registros (diccionarios).
    id_participante (int): ID del participante a buscar.

    Retorna:
    Diccionario con listas agrupadas del participante (dict).
    
    Formato de salida:
    {
        "id_participante": int,
        "fecha": [],
        "app": [],
        "cantidad_uso": [],
        "tiempo_uso": []
    }
    """

    resultado = {
        "id_participante": id_participante,
        "fecha": [],
        "app": [],
        "cantidad_uso": [],
        "tiempo_uso": []
    }

    for registro in datos:
        if registro["id_participante"] == id_participante:
            resultado["fecha"].append(registro["fecha"])
            resultado["app"].append(registro["app"])
            resultado["cantidad_uso"].append(registro["cantidad_uso"])
            resultado["tiempo_uso"].append(registro["tiempo_uso"])

    return resultado
