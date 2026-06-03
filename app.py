# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 11:17:22 2026

@author: usuario
"""

from src.carga_datos import cargar_datos
from src.metricas import (
    calcular_tiempo_total,
    calcular_promedio_uso,
    calcular_uso_por_app
)
from src.procesamiento_datos import filtrar_por_participante


def main():

    datos = cargar_datos()

    while True:
        try:
            id_buscar = int(
                input(
                    "Ingrese el DNI/ID del participante que desea consultar: "
                )
            )
            break

        except ValueError:
            print("Debe ingresar un número entero.")

    datos_filtrados = filtrar_por_participante(
        datos,
        id_buscar
    )

    if datos_filtrados.empty:
        print("No se encontraron datos para ese participante.")
        return

    promedio = calcular_promedio_uso(datos_filtrados)
    total = calcular_tiempo_total(datos_filtrados)
    uso_app = calcular_uso_por_app(datos_filtrados)

    print("\nRESULTADOS")
    print("-" * 40)
    print(f"Tiempo total: {total:.2f} minutos")
    print(f"Promedio de uso: {promedio:.2f} minutos")

    print("\nUso por aplicación:")
    print(uso_app)


if __name__ == "__main__":
    main()