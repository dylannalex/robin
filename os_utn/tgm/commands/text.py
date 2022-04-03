"""
This file contains the text the bot will use for buttons
and dialogs.
"""

from os_utn.tgm.message import emojis
from os_utn.tgm.message import markdown_validation


#
# Other
#

VALID_UNITS = f"""
Las unidades válidas son\\:
{emojis.PUSHPIN} GB
{emojis.PUSHPIN} MB
{emojis.PUSHPIN} KB
{emojis.PUSHPIN} B
{emojis.PUSHPIN} b
"""

#
# Commands dialog text
#
START_GUIDE = f"""
Hola\\, soy el bot de Sistemas Operativos {emojis.COMPUTER}
Seleccione una de las siguientes opciones para comenzar\\!

{emojis.NUMBER_1} Planificación de procesos
{emojis.NUMBER_2} Paginación \\(traducción de direcciones\\)
"""

SELECT_PROCESSES_SCHEDULING_ALGORITHM = f"""
Seleccione uno de los siguientes algoritmos{emojis.DOWN_POINTING_INDEX}
"""

LOAD_PROCESSES = f"""
A continuación manda un mensaje con los procesos, sus tiempo\
 de llegada y sus tiempos de ejecución\\ {emojis.HAPPY_FACE}

Ingrese los procesos de la siguiente forma\\:

```
nombre_proceso - tiempo_de_llegada - tiempos_de_ejecución , ... 
```
"""

RR_TIME_SLICE_AND_MODIFICATION = f"""
Los algoritmos Round Robin tienen un _time slice_ \\(o _quantum_\\) y\
 pueden ser _con modificación_ o _sin modificación_\\.

A su vez, el algoritmo puede cambiar su estado _con ó sin modificación_\
 en un momento determinado {emojis.EXPLODING_HEAD}

Ingrese estas características de la siguiente forma\\:

```
time_slice - 0 ó 1 - cambio_de_modificación
```

{emojis.PUSHPIN} El **0** significa _sin modificación_ y el 1 significa\
 _con modificación_\\.

{emojis.PUSHPIN} _cambio\\_de\\_modificación_ es el instante de tiempo\
 donde el algoritmo pasa de ser _sin modificación_ a _con modificación_\
 o viceversa\\. 
"""

PAGING_SELECT_TASK = f"""
¿En que puedo ayudarte? {emojis.HAPPY_FACE}

{emojis.NUMBER_1} Traducir dirección virtual a física
{emojis.NUMBER_2} Obtener cantidad de bits de una dirección física
{emojis.NUMBER_3} Obtener cantidad de bits de una dirección virtual
"""

TRANSLATE_LOGICAL_TO_REAL = f"""
Lo primero que debemos hacer para traducir una dirección virtual a una\
 física es conseguir el número página de la dirección virtual\\. {emojis.COWBOW_HAT_FACE}

Para ello necesitamos la _dirección virtual_ y el _tamaño de página_\\.

Ingrese estos datos de la siguiente forma\\:

```
dirección_virtual (en binario) - tamaño_de_página (con unidad)
```
{VALID_UNITS}
"""

GET_REAL_ADDRESS = (
    lambda page_number: f"""
El número de página es {page_number}\\. Ahora buscá en la tablita cual es\
 el número de marco de página que le corresponde a {page_number}\\.

Tené en cuenta que el número de página que calculé está en decimal {emojis.HAPPY_FACE}

Ingrese estos datos de la siguiente forma\\:

```
número_de_pagina (en decimal)
```
"""
)

REAL_ADDRESS_LENGTH = f"""
Ingesa el número de marco de páginas y su tamaño de la siguiente manera:

```
número_de_marcos_de_página - tamaño_de_marco_de_página (en bytes)
```
"""

LOGICAL_ADDRESS_LENGTH = f"""
Ingesa el número de páginas y su tamaño de la siguiente manera:

```
número_de_páginas - tamaño_de_página (en bytes)
```
"""

#
# Buttons text
#

NEED_AN_EXAMPLE_BUTTON = f"Necesito un ejemplo {emojis.CONFUSED_FACE}"
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
SUPPORT_ME_BUTTON = f"Repositorio en GitHub {emojis.GRINNING_CAT_WITH_SMILING_EYES}"


#
# Examples
#

LOAD_PROCESSES_EXAMPLE = f"""
Para el ejemplo de la foto de arriba {emojis.UP_POINTING_INDEX}\
 el mensaje para cargar correctamente los procesos es\\:

{emojis.PERSON} ``` A - 0 - 10, B - 1 - 2, C - 2 - 3```

Envíame tus procesos para continuar {emojis.HAPPY_FACE}
"""

RR_TIME_SLICE_AND_MODIFICATION_EXAMPLE = [
    f"""
Interpretar estos datos puede resultar muy confuso {emojis.WORRIED_FACE}

A continuación te voy a mandar algunos ejercicios y el mensaje para cargar\
 correctamente el time slice\\, si es "con modificación" o "sin modificación"\
 y sus cambios\\ {emojis.DOWN_POINTING_INDEX}
""",
    f"""
Empecemos por uno sencillo {emojis.COWBOW_HAT_FACE}

{emojis.BOOKS} Ejercicio\\:

Complete con los valores de acuerdo con la actuación del planificador según el\
 algoritmo Round Robin con q \\= 2 ms


{emojis.BOOKS} Como cargar los datos\\:

"q \\= 2 ms" significa que el _quantum_ \\(o _time slice_\\) es igual a 2\\.

El ejercicio no nos da ningún dato acerca de si el algoritmo es _con modificación_\
 o _sin modificación_ {emojis.SHRUG}\\.
En este caso se asume que es _sin modificación_, pero te recomiendo consultar a tu\
 profesor\\/a para asegurarte\\.

Tampoco menciona nada acerca del cambio de modificación\\.

En este caso el mensaje para cargar los datos correctamente es\\:

{emojis.PERSON} ``` 2 - 0 - 0```
""",
    f"""
Ahora veamos un ejemplo mas complicado {emojis.COWBOW_HAT_FACE}{emojis.WATER_PISTOL}

{emojis.BOOKS} Ejercicio\\:

Se tiene un planificador con time slice \\= 1\\. Tenga en cuenta que, a partir del\
 instante 5, si hay 2 sucesos simultáneos, un proceso que ingresa y un proceso que\
 pasa del estado de ejecución al listo, considere que el que primero pasa a la cola\
 de listos es proceso que ingresa al sistema\.


{emojis.BOOKS} Como cargar los datos\\:

Parece una ensalada de frutas, pero vamos por partes {emojis.SMILING_FACE_WITH_TEAR}\\.

Lo primero que vemos es que el time slice es igual a 1\\. Un dato menos\\!

Recordemos que cuando un algoritmo es _con modificación_, si hay dos procesos\
 simultaneos donde uno de ellos ingresa y otro pasa del estado de ejecución al\
 listo, el que pasa a la cola de listos primero es el proceso que ingresa\\.\
 Cuando un algoritmo es _sin modificación_ el que pasa primero es el proceso\
 que pasa del estado de ejecución al listo\\.

Sabiendo esto, el texto nos dice que a partir del instante 5 el algoritmo pasa\
 a ser _con modificación_\\. Esto significa que originalmente el algoritmo es\
 _sin modificación_ y cambia a _con modificación_ en el instante 5\\.

En este caso el mensaje para cargar los datos correctamente es\\:

{emojis.PERSON} ``` 1 - 0 - 5```

Donde el 0 significa que el algoritmo es _sin modificación_ y el 5 significa que\
 pasa a ser _con modificación_ en el instante de tiempo 5\\ {emojis.HAPPY_FACE} 
""",
    f"""
Ahora te toca a vos {emojis.SMILING_FACE_WITH_TEAR}\\. Mandame los datos de tu\
 ejercicio \\(como te mostré arriba {emojis.UP_POINTING_INDEX}\\) para continuar\\!
""",
]

TRANSLATE_LOGICAL_TO_REAL_EXAMPLE = f"""
Tomemos el siguiente ejercicio como ejemplo {emojis.COWBOW_HAT_FACE}{emojis.DOWN_POINTING_INDEX}

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

{emojis.BOOKS} Como cargar los datos\\:

Si cargamos la dirección virtual y el tamaño de página, conseguiremos un número de página\
 igual a 83\\. ¿Y ahora qué?\\.\\.\\.

Veamos la tabla\\! {emojis.COWBOW_HAT_FACE}{emojis.DOWN_POINTING_INDEX}
""",
    f"""
Primero tenemos que ubicar el tamaño de página en la tabla\\. Para ello nos dirigimos a la\
 columna \\"N° de Página\\"\\. Cuando observamos esta columna, nos damos cuenta que el número\
 de página 83 no está\\. ¿Y ahora que hacemos? {emojis.WEARY_FACE}\\.

Si observamos bien, veremos que el ultimo número de página es el 1A\\. Esto significa que los\
 números de página estan en el sistema hexadecimal\\. Como mencione anteriormente, mi creador\
 solo me enseñó a trabajar con el sistema decimal {emojis.SAD_FACE_WITH_TEAR}\\. Tenemos que\
 convertir el 83 a hexadecimal\\. Esto lo pueden hacer a mano o con un\
 [conversor de unidades](https://www.rapidtables.com/convert/number/decimal-to-hex.html)

Al convertir el 83 a hexadecimal, descubrimos que le número de página es 53\\. A continuación\
 nos fijamos cual es número de marco de página que le corresponde, el 13B9\\. Este es el dato\
 que necesitamos cargar, pero de nuevo, esta en hexadecimal {emojis.DIZZY_FACE}\\.
Al convertirlo a decimal obtenemos el número 5049, que es el número que tenemos que ingresar\\!

{emojis.PERSON} ```5049```
""",
    f"""
Ahora te toca a vos {emojis.SMILING_FACE_WITH_TEAR}\\. Mandame los datos de tu\
 ejercicio \\(como te mostré arriba {emojis.UP_POINTING_INDEX}\\) para continuar\\!
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
 Como no nos dice nada acerca del tamaño de los marcos de página, deducimos que tienen el mismo\
 tamaño que las páginas\\.
 
¡Carguemos los datos {emojis.HAPPY_FACE}\\!

{emojis.PERSON} ``` 2048 - 1024```

Ahora te toca a vos {emojis.SMILING_FACE_WITH_TEAR}\\. Mandame los datos de tu\
 ejercicio \\(como te mostré arriba {emojis.UP_POINTING_INDEX}\\) para continuar\\!
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
 
¡Carguemos los datos {emojis.HAPPY_FACE}\\!

{emojis.PERSON} ``` 4028 - 1024```

Ahora te toca a vos {emojis.SMILING_FACE_WITH_TEAR}\\. Mandame los datos de tu\
 ejercicio \\(como te mostré arriba {emojis.UP_POINTING_INDEX}\\) para continuar\\!
"""

#
# Results
#
SUPPORT_ME_MESSAGE = f"""
Si logré ayudarte mi creador agradecería mucho si le das una estrellita {emojis.STAR}\
 y un follow en GitHub {emojis.SMILING_FACE_WITH_OPEN_HANDS}

Para volver al menú principal utiliza el comando /start
"""

PROCESSES_SCHEDULING_RESULT = (
    lambda scheduling_algo, execution_string: f"""
Este es el diagrama de Gantt para un planificador según el algoritmo\
 **{scheduling_algo.upper()}**\\.
 
La cadena de ejecución es\\: {execution_string} {emojis.SMILING_FACE_WITH_GLASSES}
"""
)

TRANSLATE_LOGICAL_TO_REAL_RESULT = (
    lambda real_address: f"""
La dirección física es {real_address} {emojis.SMILING_FACE_WITH_GLASSES}
"""
)

REAL_ADDRESS_LENGTH_RESULT = (
    lambda real_address_length: f"""
La dirección física tiene {real_address_length} bits {emojis.SMILING_FACE_WITH_GLASSES}
"""
)

LOGICAL_ADDRESS_LENGTH_RESULT = (
    lambda logical_address_length: f"""
La dirección virtual tiene {logical_address_length} bits {emojis.SMILING_FACE_WITH_GLASSES}
"""
)
