

def parsear_linea(linea):
    """
    Qué hace la función:
    1. Recibe una línea del archivo de datos
    2. separa sus campos,
    3. convierte cada valor al tipo de dato que corresponde 
    4. crea un diccionario

    Parámetros
    ---
    - linea: str
    Una línea del archivo con el formato:
    id_participante,fecha,app,cantidad_uso,tiempo_uso

    Retorna
    ---
    - registro: dicc
    Un diccionario con la estructura:
        {
            "id_participante": int,
            "fecha": str,
            "app": str,
            "cantidad_uso": int,
            "tiempo_uso": float
        }
    Raises
    ---
    None: si la linea de archivo es vacia o no se puede convertir
    el dato 
    """
    linea = linea.strip()
    partes = linea.split(",")
    try:
        registro = {
            "id_participante": int(partes[0]),
            "fecha": partes[1],
            "app": partes[2],
            "cantidad_uso": int(partes[3]),
            "tiempo_uso": float(partes[4])
        }
        return registro

    except ValueError:
        return None
    


def cargar_datos(ruta):
    """
    Qué hace la función:
    1. Lee el archivo de datos
    2. transforma cada línea (no vacía) en un registro
    3. almacena todos los registros en una lista

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
    datos = []

    with open(ruta, "r") as archivo:
        lineas = archivo.readlines()

        inicio = 0

        # Verifico si la primera línea es encabezado
        primera = lineas[0].strip().split(",")

        if not primera[0].isdigit():
            inicio = 1  # si hay encabezado lo saltea

        for linea in lineas[inicio:]:
            if linea.strip() != "": #verifico q no sea una linea no vacia
                registro = parsear_linea(linea)
                if registro is not None:
                    datos.append(registro)
              

    return datos