# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:36:24 2026

@author: mom
"""

#código principal
from carga_datos import cargar_datos
from metricas import calcular_tiempo_total, calcular_promedio_uso, calcular_uso_por_app
from procesamiento_datos import filtrar_por_participante
from validacion_datos import validar_registro

datos = cargar_datos("datos/datos_proyecto.csv")
datos_validos = []
for registro in datos:
	if validar_registro(registro):
		datos_validos.append(registro)
id_ingresado = int(input("Ingrese su dni: "))
datos_por_participante = filtrar_por_participante(datos_validos, id_ingresado)
promedio_uso= calcular_promedio_uso(datos_por_participante)
uso_por_app = calcular_uso_por_app(datos_por_participante)
tiempo_total = calcular_tiempo_total(datos_por_participante)

print(f" El promedio de uso es de: {promedio_uso}, El tiempo total es de: {tiempo_total}, El uso por app es: {uso_por_app}(todos los tiempos están evaluados en minutos)")
