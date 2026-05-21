# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:36:24 2026

@author: mom
"""

#código principal
from src.carga_datos import cargar_datos
from src.metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app
from src.procesamiento_datos import filtrar_por_participante


def main():
    
    datos = cargar_datos()
    
    while True:
        try:
            id_buscar = int(input("Ingrese el dni del participante que desea filtrar: "))
        except ValueError:
            return ("No se pudo convertir el tipo de dato Id")
        else:
            break
    datos_filtrados = filtrar_por_participante(datos, id_buscar)
    if datos_filtrados.empty:
            print("No se encontraron datos para ese participante.")
           
 # calculo las métricas para los registros filtrados
    promedio_uso = calcular_promedio_uso(datos_filtrados)
    uso_por_app = calcular_uso_por_app(datos_filtrados)
    tiempo_total = calcular_tiempo_total(datos_filtrados)
        
  
    print(f" El promedio de uso es de: {promedio_uso}, El tiempo total es de: {tiempo_total}, El uso por app es: {uso_por_app}(todos los tiempos están evaluados en minutos)")


if __name__ == "__main__":
    main()
  


  