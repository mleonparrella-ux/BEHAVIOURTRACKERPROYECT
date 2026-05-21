import os
import pandas as pd
from src.validacion_datos import validar_datos

def cargar_datos(ruta="datos/BehaviorTracker_mock_data.csv"):
    """
    Carga el archivo CSV usando Pandas.

    Qué hace la función:
    1. Verifica que el archivo exista en la ruta indicada.
    2. Lee el archivo CSV con pandas.
    3. Envía el DataFrame a validar.
    4. Retorna el DataFrame validado.

    Parámetros
    ----------
    ruta : str
        Ruta del archivo CSV que contiene los datos.

    Retorna
    -------
    pandas.DataFrame
        DataFrame con los datos cargados y validados.

    Errores
    -------
    FileNotFoundError
        Si el archivo no existe.
    ValueError
        Si el archivo tiene datos inválidos.
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(f"No se encontró el archivo en la ruta: {ruta}")

    datos = pd.read_csv(ruta)

    datos = validar_datos(datos)

    return datos







