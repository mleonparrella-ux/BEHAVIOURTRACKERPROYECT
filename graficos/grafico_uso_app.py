# -*- coding: utf-8 -*-
"""
Created on Thu May 21 15:19:49 2026

@author: igarr
"""
import matplotib.pyplot as plt
def graficar_tiempo_por_app(uso_por_app, ruta_salida= "graficos/uso_por_app.png"):
    """
    Genera y guarda un gráfico de barras con el tiempo de uso por aplicación.

    Parámetros
    ----------
    uso_por_app : pandas.Series
        Serie de Pandas donde el índice son los nombres de las aplicaciones
        y los valores representan el tiempo total de uso de cada una.

    ruta_salida : str
        Ruta donde se guardará el gráfico generado en formato PNG.

    Retorna
    -------
    None
        La función no retorna ningún valor. Guarda una imagen PNG.
    """
    if uso_por_app.empty:
        print("No hay datos suficientes para generar el gráfico por app.")
        return

    plt.figure()
    uso_por_app.plot(kind="bar")
    plt.title("Tiempo total de uso por app")
    plt.xlabel("Aplicación")
    plt.ylabel("Tiempo de uso en minutos")
    plt.savefig(ruta_salida)
    plt.close()