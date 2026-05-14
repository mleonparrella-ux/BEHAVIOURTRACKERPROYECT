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
Sumar pandas al proyecto implicaria rehacer varias partes del codigo, sobre todo las que tienen que ver con leer el archivo, validar los datos y calcular las metricas. El cambio principal estaria en carga_datos.py: la funcion cargar_datos() ya no abriria el archivo a mano ni recorreria las lineas una por una, sino que usaria pd.read_csv() para armar un DataFrame con toda la informacion del dataset. Gracias a esto, parsear_linea() deja de ser necesaria, porque pandas separa los campos y les asigna un tipo de forma automatica. Las validaciones que hoy se hacen fila por fila pasarian a aplicarse sobre columnas enteras: revisar que el archivo tenga los campos esperados se resolveria mirando df.columns, y detectar valores vacios o negativos se haria con filtros sobre el DataFrame.
En validacion_datos.py, la funciones que convierten campos a int o float ya no haran falta, porque al cargar el archivo se le puede indicar a pandas el tipo de cada columna con dtype, e incluso interpretar fecha con parse_dates. Las propias reglas del pryecto (que el dni tenga ocho digitos positivos, que cantidad_uso y tiempo_uso sean mayores a 0, que app y fecha no esten vacios) se traducirian a filtros aplicados al DataFrame, dejando solo las filas que cumplen todas las condiciones. 
En procesamiento_datos.py, buscar los registros de un participante ya no necesitaria recorrer listas con bucles: bastaria con una expresion como df[df["dni"] == dni_buscado] para obtener todas sus filas. Algo parecido pasaria en metricas.py, donde los calculos manuales se reemplazarian por funciones propias de pandas. 
En cuanto a las clases, Registro dejaria de tener sentido, ya que cada fila del DataFrame cumple ese rol. Participante trabajaria sobre un DataFrame filtrado por DNI y sus metodos se apoyarian en pandas. Sistema solo necesitaria guardar el DataFrame general y armar los participantes a pedido. Finalmente, en main.py, los diccionarios y listas intermediarias se reemplazarian por DataFrames.
