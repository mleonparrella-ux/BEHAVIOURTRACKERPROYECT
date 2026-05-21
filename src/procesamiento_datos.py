def filtrar_por_participante(datos, id_buscar):
    """
    Filtra los datos de un participante específico usando Pandas.

    Parámetros:
    datos (pandas.Dataframe): DataFrame con todos los registros cargados.
    id_buscar (int): id del participante a filtrar

    Retorna:
   -  datos_filtrados (pandas.DataFRame): DataFrame con los datos correspondientes al id buscado 
  
    """
   
    datos_filtrados = datos[datos["id_participante"] == id_buscar]

    return datos_filtrados
    
                   
       
