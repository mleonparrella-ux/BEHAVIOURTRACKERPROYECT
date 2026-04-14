

def parsear_linea(linea):
    """
    Qué hace la función:
    1. Recibe una línea de datos
    2. separa sus campos por dato
    3. valida los datos
    4. convierte cada valor al tipo de dato que corresponde 
    5. guarda los valores en una lista

    Parámetros
    ---
    - linea: str
    Una línea del archivo con el formato:
    id_participante,fecha,app,cantidad_uso,tiempo_uso

    Retorna
    ---
    - lista_vslores_parseados: list.
    - 

    ---
    ValueError: si la linea de archivo no se puede convertir en el dato 
    """
    linea = linea.strip()
    partes = linea.split(",")
    
    for elementos in partes:
        elementos.strip()  #saco espacios del elemento
    
    if len(partes) != 5:
        return("Error, no hay cinco elementos en la línea de archivo")
    try:
        id_participante = int(partes[0])
    except ValueError as e:
        return ("Error en el tipo de dato(no se pudo convertir): " , {e})
   
    fecha = partes[1]
    try:
        app = str(partes[2])
    except ValueError as e:
        return ("Error en el tipo de dato(no se pudo convertir): " , {e})

    try:
        cantidad_uso = int(partes[3])
    except ValueError as e:
            return ("Error en el tipo de dato(no se pudo convertir): " , {e})
    try:
        tiempo_uso = float(partes[4])
    except ValueError as e:
          return ("Error en el tipo de dato(no se pudo convertir): " , {e})
      
    lista_valores_parseados = [id_participante, fecha, app, cantidad_uso,tiempo_uso]
    return lista_valores_parseados 
           
    

def cargar_datos(ruta):
    """
    Qué hace la función:
    1. Lee el archivo de datos, crea una lista "datos" en la que acumula un registro (diccionario)
    por  participante (contiene informacion sobre uso de apps). 
    Parámetros
    ---
    - ruta: str.
    Ruta del archivo a leer.

    Retorna
    ---
    - datos: list. 
    Una lista de diccionarios. Cada diccionario 
    representa un registro de uso de app.
    """
    with open("datos/BehaviorTracker_mock_data",  "r") as archivo:
        lineas = archivo.readlines()
    datos = []
    inicio = 0

    # Verifico si la primera línea es encabezado
    primera = lineas[0].strip().split(",")
    if not primera[0].isdigit():
      inicio = 1  # si hay encabezado lo saltea
    
    for linea in lineas[inicio:]:
            if linea.strip() != "": #verifico q no sea una linea vacia
                lista_datos = parsear_linea(linea)
                id_participante = lista_datos[0]
                encontrado = False
                for dicc_participante in datos:
                    if id_participante == dicc_participante["Id_participante"]:
                        dicc_participante["fecha"].append(lista_datos[1])
                        dicc_participante["app"].append(lista_datos[2])
                        dicc_participante["tiempo_uso"].append(lista_datos[3])
                        dicc_participante["cantidad_uso"].append(lista_datos[4])
                        encontrado = True 
                        break #corta la busqueda 
                    if not encontrado: #mas especifico q poner un else
                        nuevo_dicc_participante = {}
                        nuevo_dicc_participante["id_participante"] = lista_datos[0]
                        nuevo_dicc_participante["fecha"] = lista_datos[1]
                        nuevo_dicc_participante["app"] = lista_datos[2]
                        nuevo_dicc_participante["tiempo_uso"] = lista_datos[3]
                        nuevo_dicc_participante["cantidad_uso"] = lista_datos[4]
                        datos.append(nuevo_dicc_participante)
      
    return datos