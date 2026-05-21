# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:35:45 2026

@author: usuario
"""

def calcular_tiempo_total(datos):
    """
    Calcula tiempo total de uso

    Parametros:
        datos: pandas.DataFrame
            DataFrame con  registros 
            
    Return: float
            Suma total de la columna "tiempo_uso"
    """
    tiempo_total = datos["tiempo_uso"].sum()

    return tiempo_total

def calcular_promedio_uso(datos):
    """
    Calcula el propmedio de uso de aplicaciones

    Parameters
    ----------
    datos : pandas.DataFrame
        DataFrame con  registros.

    Returns
    -------
    promedio: float
    """
    if len(datos) == 0:
        return 0

    promedio = datos["tiempo_uso"].mean()

    return promedio

def calcular_uso_por_app(datos):
    """
    Calcula el tiempo total de uso por aplicación.

    Parámetros:
    datos (pandas.DataFRame): DataFrame  registros.

    Retorna:
    uso_apps: pandas.Series
    """

    uso_por_app = datos.groupby("app")["tiempo_uso"].sum()

    return uso_por_app
