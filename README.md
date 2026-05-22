# proyecto-cola

Integrantes del grupo: Mia Blaquier, Agustina Igarreta, Manuel Leon Parrella, Ramon Otero Monsegur.

1. ¿Qué hace nuestro programa?
Nuestro programa busca medir a lo largo del tiempo, la frecuencia y cantidad de tiempo que una persona utiliza una determinada app en su celular. Hace uso de contadores para representar el comportamiento, y luego utiliza métricas básicas para poder calcular la actividad.

2. ¿Qué datos recibe?, ¿Cuántas columnas hay?, ¿Qué tipo de dato es cada una?
Recibe datos de un archivo sobre el uso del celular de las personas. Cada dato corresponde a una columna especifica:
dni de la persona  → int
fecha → str
app → str
cantidad de uso → int
tiempo de uso → float

3. ¿Qué resultados produce?
El resultado de este programa es realizar un seguimiento meticuloso de una persona en relación al uso de las apps del celular. Además analiza patrones del comportamiento de la persona a lo largo de un periodo de tiempo. Esto puede ayudar a reducir/aumentar hábitos negativos/positivos. El programa busca devolver informacion como promedio del tiempo de uso del celular, promedio de uso por app, entre otras metricas en relacion a la tematica que pueden ayudar a concientizar y disminuir respecto al uso del celular.

Errores y Validaciones
Incluimos validaciones para los siguientes datos (en ambos casos salta ValueError):

- Que el dni sea un número entero positivo de ocho dígitos
- Que “cantidad_uso” y “tiempo_uso” contengan un número no nulo y  positivo
- Que “app” y “fecha” sean campos no vacíos que puedan convertirse en strings

Incluimos try/except para atajar los siguientes errores:

- En la función parsear_linea: que haya necesariamente cinco campos en una línea de archivo. Además, que todos los datos se puedan convertir en su tipo de dato correspondiente, de lo contrario salta ValueError y muestra la respectiva línea.
- En la función cargar_datos modificamos el código para que sea más específica y detallada la acción de revisar los dnis ya ingresados y volver a cargar un diccionario o crear uno adicional en caso de que el mismo participante no haya sido ingresado todavía.

OBJETOS:
Para modelar este sistema utilizando objetos, pensamos en utilizar 3 clases, con el fin de optimizar el código.
	Primero, una clase Registro, que representaría una fila del archivo presentado, contendría todos los datos de los usuarios, y tendría como método la validación.
	Segundo, pensamos en una clase Participante, que agrupe esos registros a partir del id de los mismos participantes. Para los métods, tendríamos en cuenta el calculo del promedio, el tiempo total, y el uso por app, que son propias de cada participante.
	Por último, pensamos en una clase Sistema, que englobe a todos los usuarios y que permita la carga de datos, y hacer consultas, como poder buscar un participante.
	Estos tres objetos están relacionados: un Sistema contiene muchos Participantes, y estos contienen muchos Registros.
	
**Utilizacion de Pandas**
	La incorporacion de pandas implico reescribir las partes del codigo relacionadas con la lectura del archivo, la validacion de datos, el procesamiento y el calculo de metricas.
	En carga_datos.py, la funcion cargar_datos() reemplazo la lectura manual linea por linea por pd.read_csv(), eliminando la necesidad de parsear_linea(). El DataFrame resultante se envia directamente a validar_datos().
	En validacion_datos.py, todas las validaciones se aplican sobre columnas enteras del DataFrame: se verifica que las columnas esperadas esten presentes, que no haya valores nulos, que los tipos de datos sean correctos, que los valores numericos sean positivos, que las apps pertenezcan a la lista valida y que las fechas tengan el formato de dd-mm-aaaa y no sean futuras. 

En procesamiento_datos.py, la busqueda de un participante se simplifico a datos[datos["id_participante] == id_buscar]. En metricas.py, los calculos manuales fueron reemplazados por: .sum(), .mean() y .groupby().
En cuanto a las clases, Registro dejo de tener sentido ya que cada fila del DataFrame cumple este rol. Participante y Sistema ahora trabajan directamente sobre DataFrames, y los diccionarios y listas de main.py fueron reemplazados por DataFrames. 
