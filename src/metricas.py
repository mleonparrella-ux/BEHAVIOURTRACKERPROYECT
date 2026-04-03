# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:35:45 2026

@author: usuario
"""

def calcular_tiempo_total(datos):
    """
    Recorre una lista de registros y suma todos los valores de tiempo de uso.

    Parametros:
        datos: list
            Lista de registros 
            
    Return: float
            Tiempo total
    """
    contador = 0

    for tiempo_uso in datos: 
        contador += tiempo_uso 

    return contador 

def calcular_promedio_uso(datos):
    """
    Calcula el propmedio de uso de aplicaciones

    Parameters
    ----------
    datos : list
        Lista de registros.

    Returns
    -------
    promedio: float
    """
    if len(datos) == 0:
        return 0
    
    total = 0
    
    for registro in datos:
        total += registro["tiempos_uso"]
        
    promedio = total / len(datos)
    
    return promedio