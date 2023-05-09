# LaberintoExam
Pasos seguidos y video de resolución de examen para salir del laberinto Maze3 6x6 con Turtlebot 3
NOTA: para llevar a cabo una buena realización de la practica se recomienda tener la versión de Ubuntu 20.04, ya sea en una Virtual Machine o haciendo una partición en el disco duro del dispositivo.
Paso uno, crearemos un nuevo paquete de ROS en el espacio de trabajo de catkin llamado 'playwood_mazes'. Asegurandonos de incluir las independencias 'gazebo_ros' y 'turtlebot3_gazebo'.
En el segundo paso crearemos un directorio llamado 'worlds' dentro del paquete 'plywood_mazes'.
Continuamos con el tercer paso creando un directorio llamado 'launch' dentro del paquete 'plywood_mazes'.
El cuarto paso consiste en la clonación de los paquetes de GitHub, utilizamos el comando 'cd' para cambiar al directorio donde se desea clonar el paquete.
Dentro de este mismo haremos la busqueda de la URL del paquete de GitHub (por lo general se encuentra en la pestaña "Code" del repositório), se ejecutará el siguiente comando 'git clone <URL>'
Para el quinto paso abriremos una ventana y colocaremos el siguiente comando 'roslaunch plywood_mazes maze_3_6x6.launch', este lanza todos los nodos especificados en el archivo maze_3_6x6.launch y configura el entorno según las instrucciones en ese archivo. 
En la sexta etapa es colocar el siguiente comando 'roslaunch plywood_mazes spawn_turtlebot3.launch' en una nueva ventana, este lanza todos los nodos especificados en el archivo spawn_turtlebot3.launch y configura el entorno según las instrucciones en ese archivo.
  
A continuación se explicará con mayor detalle el archivo examen2.py :
  
