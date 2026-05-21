
import pandas as pd
from src.validacion_datos import validar_registro

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
    
    campos = [campo.strip() for campo in campos] #saco espacios de cada campo
    
    if len(campos) != 5:
        raise ValueError("Error, no hay cinco elementos en la línea de archivo") #verificio que haya cinco campos
    try:
        id_participante = int(campos[0])
    except ValueError as e:
        raise ValueError ("Error en el tipo de dato(no se pudo convertir): " , {e})
   
    fecha = campos[1]
    try:
        app = str(campos[2])
    except ValueError as e:
        raise ValueError ("Error en el tipo de dato(no se pudo convertir): " , {e})

    try:
        cantidad_uso = int(campos[3])
    except ValueError as e:
            raise ValueError ("Error en el tipo de dato(no se pudo convertir): " , {e})
    try:
        tiempo_uso = float(campos[4])
    except ValueError as e:
          raise ValueError ("Error en el tipo de dato(no se pudo convertir): " , {e})
      
    lista_valores_parseados = [id_participante, fecha, app, cantidad_uso,tiempo_uso]
    return lista_valores_parseados 
           
    

def cargar_datos(ruta = "datos/BehaviorTracker_mock_data.csv"):
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
    - datos_validos: list.pandas.DataFrame
        DataFrame con los datos válidos del archivo.
        Cada fila representa un registro de uso de app.
        
    - ValueError si hay datos registrados inválidos
    Una lista de diccionarios. Cada diccionario 
    representa un registro de uso de app.
    """
    datos_validos = []  

   
    try: 
        with open(ruta, "r") as archivo:
            lineas = archivo.readlines()
    except Exception as e : #
         return (f"Error. No se pudo abrir el archivo , {e}")   #verifico que pueda abrirse el archivo
    
    for linea in lineas:
      if linea.strip() != "":
          lista_datos = parsear_linea(linea)

          registro = {
              "id_participante": lista_datos[0],
              "fecha": lista_datos[1],
              "app": lista_datos[2],
              "cantidad_uso": lista_datos[3],
              "tiempo_uso": lista_datos[4]
          }
 
          try:
              registro_valido = validar_registro(registro)
          except ValueError as e:
              raise ValueError(f"Tipo de error encontrado: {e}")
          else:
              datos_validos.append(registro_valido)

    datos_validos = pd.DataFrame(datos_validos)

    return datos_validos





