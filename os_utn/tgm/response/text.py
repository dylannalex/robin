"""
This file contains the text the bot will use for buttons
and dialogs.
"""

from os_utn.tgm.message import emojis
from os_utn.tgm.message import markdown_validation


############################
#   Miscellaneous          #
############################

VALID_UNITS = f"""
Las unidades válidas son\\:
{emojis.PUSHPIN} GB
{emojis.PUSHPIN} MB
{emojis.PUSHPIN} KB
{emojis.PUSHPIN} B
{emojis.PUSHPIN} b
"""

############################
#   Commands dialog text   #
############################

START_GUIDE = f"""
Hola, soy el bot de Sistemas Operativos {emojis.CAT_WITH_WRY_SMILE}

{emojis.COMPUTER} Seleccione una de las siguientes opciones\
 para comenzar\\:

{emojis.NUMBER_1} Planificación de procesos
{emojis.NUMBER_2} Paginación
"""

SELECT_PROCESSES_SCHEDULING_ALGORITHM = f"""
Seleccione uno de los siguientes algoritmos{emojis.DOWN_POINTING_INDEX}
"""

LOAD_PROCESSES = f"""
Ingrese los procesos, sus tiempos de llegada y sus tiempos de ejecución\
 {emojis.GRINNING_CAT_WITH_SMILING_EYES}

```
nombreProceso - tiempoLlegada - tiemposDeEjecución , ... 
```
"""

RR_TIME_SLICE_AND_MODIFICATION = f"""
Ingrese el time slice \\(también llamado quantum\\),\
 si el algoritmo es con o sin modificación \\(0 significa sin modificación\
 y 1 con modificación\\) y el instante de tiempo donde se da el cambio de\
 modificación {emojis.GRINNING_CAT_WITH_SMILING_EYES}

```
timeSlice - 0/1 - cambioModificación
```
"""

PAGING_SELECT_TASK = f"""
¿En que puedo ayudarte? {emojis.GRINNING_CAT_WITH_SMILING_EYES}

{emojis.NUMBER_1} Traducir dirección virtual a física
{emojis.NUMBER_2} Obtener cantidad de bits de una dirección física
{emojis.NUMBER_3} Obtener cantidad de bits de una dirección virtual
"""

TRANSLATE_LOGICAL_TO_REAL = f"""
Ingrese la dirección virtual y el tamaño de\
 página {emojis.GRINNING_CAT_WITH_SMILING_EYES}

```
direcciónVirtual (en binario) - tamañoPágina (con unidad)
```
{VALID_UNITS}
"""

GET_REAL_ADDRESS = (
    lambda page_number: f"""
 El número de página es {page_number}\\. Ingrese el número de marco\
 de página \\(en decimal\\) {emojis.GRINNING_CAT_WITH_SMILING_EYES}

```
marcoPagina (en decimal)
```
"""
)

REAL_ADDRESS_LENGTH = f"""
Ingese el número de marcos de página y su tamaño {emojis.GRINNING_CAT_WITH_SMILING_EYES}

```
cantidadMarcosPágina - tamañoMarcoPágina (en bytes)
```
"""

LOGICAL_ADDRESS_LENGTH = f"""
Ingese el número de páginas y su tamaño {emojis.GRINNING_CAT_WITH_SMILING_EYES}

```
cantidadPáginas - tamañoPágina (en bytes)
```
"""

############################
#       Buttons            #
############################

# Tasks:
PROCESSES_SCHEDULING_GUIDE_BUTTON = emojis.NUMBER_1
PAGING_BUTTON = emojis.NUMBER_2
# Processes:
ROUND_ROBBIN_BUTTON = "Round Robin"
SJF_BUTTON = "SJF"
FCFS_BUTTON = "FCFS"
SRTN_BUTTON = "SRTN"
# Paging:
TRANSLATE_LOGICAL_TO_REAL_BUTTON = emojis.NUMBER_1
REAL_ADDRESS_LENGTH_BUTTON = emojis.NUMBER_2
LOGICAL_ADDRESS_LENGTH_BUTTON = emojis.NUMBER_3
# Result:
SUPPORT_ME_BUTTON = f"{emojis.LINK} GitHub"
REPORT_A_BUG_BUTTON = f"{emojis.BUG} Reportar un Bug"
BACK_TO_SELECT_TASK_BUTTON = f"{emojis.COMPUTER} Volver al Inicio"
# Examples:
NEED_AN_EXAMPLE_BUTTON = f"Necesito un ejemplo {emojis.CONFUSED_FACE}"
RR_WITHOUT_MODIFICATION_CHANGE_EXAMPLE_BUTTON = (
    f"{emojis.NUMBER_1} Ejemplo sin cambio de modificacion"
)
RR_WITH_MODIFICATION_CHANGE_EXAMPLE_BUTTON = (
    f"{emojis.NUMBER_2} Ejemplo con cambio de modificacion"
)

############################
#       Examples           #
############################

LOAD_PROCESSES_EXAMPLE = f"""
Para el ejemplo de la imagen de arriba {emojis.UP_POINTING_INDEX}\
 el mensaje para cargar correctamente los procesos es\\:

{emojis.PERSON} ``` A - 0 - 10, B - 1 - 2, C - 2 - 3```

Ingrese sus procesos para continuar {emojis.GRINNING_CAT_WITH_SMILING_EYES}
"""

ROUND_ROBIN_WITHOUT_MODIFICATION_CHANGE_EXAMPLE = f"""
Ejemplo de algoritmo Round Robin sin modificación {emojis.CAT_WITH_WRY_SMILE}

{emojis.BOOKS} Ejercicio\\:

Complete con los valores de acuerdo con la actuación del planificador según el\
 algoritmo Round Robin con q \\= 2 ms


{emojis.BOOKS} Como cargar los datos\\:

El ejercicio nos menciona que "q \\= 2 ms", es decir, que el *quantum* es igual\
 a 2\\. Como el enunciado no especifica nada más, asumiremos que el algoritmo es\
 *sin modificación*, y que no hay cambios de modificación\\. 


{emojis.PUSHPIN} El mensaje para cargar los datos correctamente es\\:

{emojis.PERSON} ``` 2 - 0 - 0```

Ingrese los datos de su ejercicio {emojis.GRINNING_CAT_WITH_SMILING_EYES}
"""
ROUND_ROBIN_WITH_MODIFICATION_CHANGE_EXAMPLE = f"""
Ejemplo de algoritmo Round Robin con cambio de modificación {emojis.CAT_WITH_WRY_SMILE}

{emojis.BOOKS} Ejercicio\\:

Se tiene un planificador con time slice \\= 1\\. Tenga en cuenta que, a partir del\
 instante 5, si hay 2 sucesos simultáneos, un proceso que ingresa y un proceso que\
 pasa del estado de ejecución al listo, considere que el que primero pasa a la cola\
 de listos es proceso que ingresa al sistema\.


{emojis.BOOKS} Como cargar los datos\\:

Lo primero que vemos es que el time slice es igual a 1\\.

Recordemos que cuando un algoritmo es *con modificación*, si hay dos procesos\
 simultaneos donde uno de ellos ingresa y otro pasa del estado de ejecución al\
 listo, el que pasa a la cola de listos primero es el proceso que ingresa\\.\
 Cuando un algoritmo es *sin modificación* el que pasa primero es el proceso\
 que pasa del estado de ejecución al listo\\.

El texto nos dice que a partir del instante 5 el algoritmo pasa a ser\
 *con modificación*\\. Esto significa que, desde el instante 0, el algoritmo\
 es *sin modificación*, y cambia a *con modificación* en el instante 5\\.

{emojis.PUSHPIN} El mensaje para cargar los datos correctamente es\\:

{emojis.PERSON} ``` 1 - 0 - 5```

Ingrese los datos de su ejercicio {emojis.GRINNING_CAT_WITH_SMILING_EYES}
"""

TRANSLATE_LOGICAL_TO_REAL_EXAMPLE = f"""
Tomemos el siguiente ejercicio como ejemplo {emojis.CAT_WITH_WRY_SMILE}

{emojis.BOOKS} Ejercicio\\:

Considerando páginas de 1KB de tamaño, si la dirección virtual es 1101010111000110,\
 ¿Cuál es la dirección física en memoria real?

{emojis.BOOKS} Como cargar los datos\\:

{emojis.PERSON} ``` 11101010111000110 - 1KB```

Notemos que la dirección virtual está en binario\\. En caso que nos den una dirección\
 virtual en otra unidad, debemos convertirla a binario\\!

Manda un mensaje con tu dirección virtual y el tamaño de página para continuar\
 {emojis.GRINNING_CAT_WITH_SMILING_EYES}
"""

GET_REAL_ADDRESS_EXAMPLE = (
    f"""
Veamos un ejemplo {emojis.GRINNING_CAT_WITH_SMILING_EYES}

{emojis.BOOKS} Ejercicio\\:

Considerando páginas de 2 KB de tamaño, si la dirección virtual es 0011110111000110,\
 ¿Cuál es la dirección en memoria real \\(RAM\\)?
""",
    f"""
{emojis.BOOKS} Como cargar los datos\\:

El número de página que le corresponde a la dirección virtual 0011110111000110 es el 83\
 \\(valor en decimal\\)\\. En este caso, los números de página en la tabla estan en\
 sistema hexadecimal, por lo que debemos convertir el 83 a hexadecimal\\. Esto podemos\
 hacerlo con un\
 [conversor de unidades](https://www.rapidtables.com/convert/number/decimal-to-hex.html)\
 {emojis.CAT_WITH_WRY_SMILE}

El número de pagina, en hexadecimal, es 53\\. Le corresponde el marco de página 13B9, que\
 en decimal es el marco de página 5049\\.

{emojis.PERSON} ```5049```

Ingrese el marco de página de su ejercicio {emojis.GRINNING_CAT_WITH_SMILING_EYES}
""",
)

REAL_ADDRESS_LENGTH_EXAMPLE = f"""
Veamos un ejemplo {emojis.GRINNING_CAT_WITH_SMILING_EYES}

{emojis.BOOKS} Ejercicio\\:

En un sistema operativo el espacio de direccionamiento lógico es de 4028 páginas de 1024 bytes\
 cada una\\. Este espacio de direccionamiento se mapea en una memoria física que tiene 2048 marcos\
 de página\\.

¿Cuántos bits tiene la dirección física?

{emojis.BOOKS} Como cargar los datos\\:

El ejercicio nos dice que hay 4028 páginas de 1024 bytes de tamaño, y 2048 marcos de página\\.\
 Como no nos dice nada acerca del tamaño de los marcos de página, asumiremos que tienen el mismo\
 tamaño que las páginas\\.

{emojis.PERSON} ``` 2048 - 1024```

Ingrese el número de marcos de página y el tamaño de cada marco de página \\(en bytes\\)\
 de su ejercicio {emojis.GRINNING_CAT_WITH_SMILING_EYES}
"""

LOGICAL_ADDRESS_LENGTH_EXAMPLE = f"""
Veamos un ejemplo {emojis.GRINNING_CAT_WITH_SMILING_EYES}

{emojis.BOOKS} Ejercicio\\:

En un sistema operativo el espacio de direccionamiento lógico es de 4028 páginas de 1024 bytes\
 cada una\\. Este espacio de direccionamiento se mapea en una memoria física que tiene 2048 marcos\
 de página\\.

¿Cuántos bits tiene la dirección virtual?

{emojis.BOOKS} Como cargar los datos\\:

El ejercicio nos dice que hay 4028 páginas de 1024 bytes de tamaño\\.
 
{emojis.PERSON} ``` 4028 - 1024```

Ingrese el número de página y el tamaño de cada página \\(en bytes\\)\
 de su ejercicio {emojis.GRINNING_CAT_WITH_SMILING_EYES}
"""

#
# Results
#
SUPPORT_ME_MESSAGE = f"""
Si fui de ayuda agradecería mucho una estrellita y un follow en GitHub\
 {emojis.SMILING_FACE_WITH_OPEN_HANDS}
Tambien puedes ayudarme reportando errores y compartiendo el bot con\
 tus compañeros {emojis.HAPPY_FACE} 
"""

PROCESSES_SCHEDULING_RESULT = (
    lambda scheduling_algo, execution_string: f"""
Este es el diagrama de Gantt para un planificador según el algoritmo\
 **{scheduling_algo}**\\.
 
La cadena de ejecución es\\: {execution_string} {emojis.GRINNING_CAT_WITH_SMILING_EYES}
"""
)

TRANSLATE_LOGICAL_TO_REAL_RESULT = (
    lambda real_address: f"""
La dirección física es {real_address} {emojis.GRINNING_CAT_WITH_SMILING_EYES}
"""
)

REAL_ADDRESS_LENGTH_RESULT = (
    lambda real_address_length: f"""
La dirección física tiene {real_address_length} bits {emojis.GRINNING_CAT_WITH_SMILING_EYES}
"""
)

LOGICAL_ADDRESS_LENGTH_RESULT = (
    lambda logical_address_length: f"""
La dirección virtual tiene {logical_address_length} bits {emojis.GRINNING_CAT_WITH_SMILING_EYES}
"""
)
