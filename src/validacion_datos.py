# -*- coding: utf-8 -*-

import pandas as pd
def validar_datos(datos):
    """
    Valida un DataFrame con datos de uso de aplicaciones.

    Qué hace la función:
    1. Verifica que estén las columnas esperadas.
    2. Verifica que no haya valores vacíos o nulos.
    3. Verifica que los tipos de datos sean correctos.
    4. Verifica que los valores numéricos sean positivos.
    5. Verifica que las apps pertenezcan a las opciones válidas.

    Parámetros
    ----------
    datos : pandas.DataFrame
        DataFrame con los datos cargados desde el archivo CSV.

    Retorna
    -------
    pandas.DataFrame
        El mismo DataFrame si supera todas las validaciones.

    Errores
    -------
    ValueError
        Si faltan columnas, hay datos vacíos, tipos incorrectos
        o valores inválidos.
    """
    columnas= [
        "id_participante",
        "fecha",
        "app",
        "cantidad_uso",
        "tiempo_uso"
    ]

    if list(datos.columns) != columnas:
        raise ValueError(f"El archivo debe tener estas columnas: {columnas}")

    if datos.isna().any().any():
        raise ValueError("El archivo contiene campos vacíos o valores nulos.")

           #validar tiempo uso
    if datos["tiempo_uso"].dtype not in ["float64", "int64"]:
        raise ValueError("El tiempo_uso debe ser un número.")

    if (datos["tiempo_uso"] <= 0).any():
        raise ValueError("El tiempo_uso debe ser positivo.")
   
          #validar id
    if (datos["id_participante"] <= 0).any():
        raise ValueError("El id_participante debe ser positivo.")
        
    if datos["id_participante"].dtype != "int64":
        raise ValueError("El id_participante debe ser un número entero.")
        
         #validar cantidad uso
    if (datos["cantidad_uso"] <= 0).any():
        raise ValueError("La cantidad_uso debe ser positiva.")
    if datos["cantidad_uso"].dtype != "int64":
         raise ValueError("La cantidad_uso debe ser un número entero.")
    
 
        #validar app 
    if datos["app"].dtype != "object":
         raise ValueError("La app debe estar escrita como texto.")
         
    if (datos["app"].str.strip() == "").any():
        raise ValueError("Hay campos vacíos en la columna app.")

    apps_validas = ["twitter", "instagram", "facebook", "tiktok", "whatsapp"]

    if not datos["app"].isin(apps_validas).all():
        raise ValueError(f"Hay apps no válidas. Las opciones son: {apps_validas}")
    
        #validar fechas
        
    if datos["fecha"].dtype != "object":
        raise ValueError("La fecha debe estar escrita como texto.")
        
    fechas_convertidas = pd.to_datetime(datos["fecha"], format="%d-%m-%Y")

    if fechas_convertidas.isna().any():
        raise ValueError("Hay fechas inválidas o con formato distinto a dd-mm-AAAA.")

    if (fechas_convertidas > pd.Timestamp.today()).any():
        raise ValueError("Hay fechas futuras en el archivo.")
       
    if (datos["fecha"].str.strip() == "").any():
        raise ValueError("Hay campos vacíos en la columna fecha.")

    return datos

