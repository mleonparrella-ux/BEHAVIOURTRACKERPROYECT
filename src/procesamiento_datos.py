def filtrar_por_participante(datos):
    """
    Filtra los datos de un participante específico.

    Parámetros:
    datos (list): Lista de registros (diccionarios).

    Retorna:
   - si usuario ingresa un id: registro (dicc) del participantecon ese id 
   - si usuario ingresa "todos": datos.  registro de todos los participantes (list). es una lista de diccionarios.
    """

    while True:
        opcion = input("Ingrese ID del participante o 'todos' para analizar los datos de todos los participantes: ")

        if opcion == "todos":
            return datos
        elif opcion.isdigit():
            id_buscar = int(opcion)
        for participante in datos:
                if participante["id_participante"] == id_buscar:
                    return [participante]
                else:
                    print("ID no encontrado. Intente nuevamente")
                    continue
        else:
                print("Dato ingresado no válido")
                continue
