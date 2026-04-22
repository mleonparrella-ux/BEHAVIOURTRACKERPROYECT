def filtrar_por_participante(datos, id_buscar):
    """
    Filtra los datos de un participante específico.

    Parámetros:
    datos (list): Lista de registros (diccionarios).
    id_buscar (int): id del participante a filtrar

    Retorna:
   -  registro (dicc) del participante con el mismo id
  
    """

    for participante in datos:
        if participante["id_participante"] == id_buscar:
            return [participante]
        else:
            print("ID no encontrado. Intente nuevamente")
                   
       
