
from validacion_datos import validar_registro
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
    - lista_valores_parseados: list.

    ---
    ValueError: si la linea de archivo no se puede convertir en el dato 
    """
    linea = linea.strip() #le saco posibles espacios en principio y fin de linea
    campos = linea.split(",") #separo lineas por campo y los acumulo en una lista
    
    for campo in campos:
        campo.strip()  #saco espacios de cada campo
    
    if len(campos) != 5:
        return("Error, no hay cinco elementos en la línea de archivo") #verificio que haya cinco campos
    try:
        id_participante = int(campos[0])
    except ValueError as e:
        return ("Error en el tipo de dato(no se pudo convertir): " , {e})
   
    fecha = campos[1]
    try:
        app = str(campos[2])
    except ValueError as e:
        return ("Error en el tipo de dato(no se pudo convertir): " , {e})

    try:
        cantidad_uso = int(campos[3])
    except ValueError as e:
            return ("Error en el tipo de dato(no se pudo convertir): " , {e})
    try:
        tiempo_uso = float(campos[4])
    except ValueError as e:
          return ("Error en el tipo de dato(no se pudo convertir): " , {e})
      
    lista_valores_parseados = [id_participante, fecha, app, cantidad_uso,tiempo_uso]
    return lista_valores_parseados 
           
    

def cargar_datos(ruta = "datos/BehaviorTracker_mock_data"):
    """
    Qué hace la función:
    1. Abre y lee un archivo.
    2. separa el archivo en líneas
    4. Parsea las lineas
    5. busca el id del participante en una lista. Si lo encuentra: agrega valores a diccionario
    existente, sino agrega valores a  uno nuevo
    
    Parámetros:
    ---
    - ruta: str. archivo

    Retorna
    ---
    - datos_validos: list. 
    - ValueError si hay datos registrados inválidos
    Una lista de diccionarios. Cada diccionario 
    representa un registro de uso de app.
    """
   

    datos = []
    try: 
        with open(ruta,  "r") as archivo:
            pass
    except Exception as e : #
         return (f"Error. No se pudo abrir el archivo , {e}")   #verifico que pueda abrirse el archivo
    lineas = archivo.readlines()
    for linea in lineas:
        if linea.strip() != "": #verifico q no sea una linea vacia
            lista_datos = parsear_linea(linea)
            id_participante = lista_datos[0]
            encontrado = False
            for dicc_participante in datos:
                if id_participante == dicc_participante["Id_participante"]:
                    dicc_participante["fecha"].append(lista_datos[1])
                    dicc_participante["app"].append(lista_datos[2])
                    dicc_participante["tiempo_uso"].append(lista_datos[4])
                    dicc_participante["cantidad_uso"].append(lista_datos[3])
                    encontrado = True 
                    break #corta la busqueda 
                if not encontrado: #mas especifico q poner un else
                    nuevo_dicc_participante = {}
                    nuevo_dicc_participante["id_participante"] = lista_datos[0]
                    nuevo_dicc_participante["fecha"] = lista_datos[1]
                    nuevo_dicc_participante["app"] = lista_datos[2]
                    nuevo_dicc_participante["tiempo_uso"] = lista_datos[4]
                    nuevo_dicc_participante["cantidad_uso"] = lista_datos[3]
                    datos.append(nuevo_dicc_participante)
                
    datos_validos = []
    for registro in datos:
        try:
            registro_valido = validar_registro(registro)
        except ValueError as e:
              raise (f" Tipo de error encontrado: {e}. Ubicación: {validar_registro}")
        else:
               datos_validos.append(registro_valido) 
               
    return datos_validos
