"""
This file contains the text the bot will use for buttons
and dialogs.
"""

from os_utn.tgm.message import emojis
from os_utn.tgm.message import markdown_validation


#
# Commands dialog text
#
START_GUIDE = f"""
Hola\\, soy el bot de Sistemas Operativos {emojis.COMPUTER}
Seleccione una de las siguientes opciones para comenzar\\!

{emojis.NUMBER_1} Planificación de procesos
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

#
# Buttons text
#

NEED_AN_EXAMPLE_BUTTON = f"Necesito un ejemplo {emojis.CONFUSED_FACE}"
PROCESSES_SCHEDULING_GUIDE_BUTTON = emojis.NUMBER_1
ROUND_ROBBIN_BUTTON = "Round Robin"
SJF_BUTTON = "SJF"
FCFS_BUTTON = "FCFS"
SRTN_BUTTON = "SRTN"


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
