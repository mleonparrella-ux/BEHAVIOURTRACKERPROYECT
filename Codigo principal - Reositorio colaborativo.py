# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 15:36:24 2026

@author: mom
"""

#código principal
datos = cargar_datos(datos/datos_proyecto.csv)
datos_validos = []
for registro in datos:
	if validar_registro(registro):
		datos_validos.append(registro)
id_ingresado = int(input("Ingrese su dni: "))
datos_por_participante = filtrar_participante(datos_validos, id_ingresado)
promedio_uso= calcular_promedio_uso(datos_por_participante)
uso_por_por_app_app = calcular_uso_por_app(datos_por_participante)
uso_total = calcular_uso_total(datos_por_participante)

print(f" El promedio de uso es de: {promedio_uso}, El uso total es de: {uso_total}, El uso por app es: {uso_por_app}(todos los tiempos están evaluados en minutos)")
