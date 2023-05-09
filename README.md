# LaberintoExam
 
<div id="top"></div>
<br />
<div align="center">
  <a href="[github.com/JosueLara22/PicknPlace-for-Open_Manipulator](https://github.com/AldoCG25/LaberintoExam.git)">
    <img src="https://github.com/AldoCG25/LaberintoExam/blob/main/6a26de0f-de71-4a06-a354-4c7c5ff3df2d.jpg" alt="Logo" width="700" height="400">
  </a>

<h3 align="center">Laberinto Examen</h3>

  <p align="center">
    Resolución del Laberinto Maze 3 6x6 con TurtleBot3 "Burger"
  </p>
</div>



## Sobre el examen
En este proyecto, se utilizará el Turtlebot3 Burger para resolver un laberinto previamente almacenado en el repositorio de donde se obtuvo el mapa. Para lograr este objetivo, se ha desarrollado un código que permite guiar al robot hacia un punto específico en el mapa.

### Requisitos
Para llevar a cabo la práctica de manera efectiva, se recomienda contar con la versión de Ubuntu 20.04 instalada en una máquina virtual o en una partición del disco duro de su dispositivo. Esto permitirá una mayor estabilidad y compatibilidad con las herramientas utilizadas durante la práctica.
### Instalación
1. Install ROS Noetic: User must be admin to proceed
2. Install Github
```sh 
 sudo apt-get install git-all
```
3. Install ROS Noetic tools (Copy all these instructions on terminal)
```sh 
sudo apt update 
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_noetic.sh
chmod 755 ./install_ros_noetic.sh
bash ./install_ros_noetic.sh
```  
4. Instalar controladores y paquetes.
```sh
source ~/.bashrc	 
sudo apt-get install ros-noetic-ros-controllers ros-noetic-gazebo* ros-noetic-moveit* ros-noetic-industrial-core	 
sudo apt install ros-noetic-dynamixel-sdk ros-noetic-dynamixel-workbench*
sudo apt install ros-noetic-robotis-manipulator
```
5. Crearemos un nuevo paquete de ROS en el espacio de trabajo de catkin llamado 'playwood_mazes'. Asegurandonos de incluir las independencias 'gazebo_ros' y 'turtlebot3_gazebo'.
```sh
cd ~/catkin_ws/src
catkin_create_pkg plywood_mazes gazebo_ros turtlebot3_gazebo
```
6. Crearemos un directorio llamado 'worlds' dentro del paquete 'plywood_mazes'.
```sh
cd ~/catkin_ws/src/plywood_mazes
mkdir worlds
```
7. Continuamos con el tercer paso creando un directorio llamado 'launch' dentro del paquete 'plywood_mazes'.
```sh
mkdir launch
```
8. Consiste en la clonación de los paquetes de GitHub, utilizamos el comando 'cd' para cambiar al directorio donde se desea clonar el paquete.
```sh
cd <directorio_deseado>
```
9. Dentro de este mismo haremos la busqueda de la URL del paquete de GitHub (por lo general se encuentra en la pestaña "Code" del repositório), se ejecutará el siguiente comando 'git clone <URL>'
```sh
git clone <URL>
```
 10. Para el quinto paso abriremos una ventana y colocaremos el siguiente comando 'roslaunch plywood_mazes maze_3_6x6.launch', este lanza todos los nodos especificados en el archivo maze_3_6x6.launch y configura el entorno según las instrucciones en ese archivo.
```sh
roslaunch plywood_mazes maze_3_6x6.launch
```
 11. En la sexta etapa es colocar el siguiente comando 'roslaunch plywood_mazes spawn_turtlebot3.launch' en una nueva ventana, este lanza todos los nodos especificados en el archivo spawn_turtlebot3.launch y configura el entorno según las instrucciones en ese archivo.
 ```sh
roslaunch plywood_mazes spawn_turtlebot3.launch
```

## Código Examen.py


## Video de implementación

<p align="right">(<a href="#top">back to top</a>)</p>

<h3 align="left">Solución al laberinto con robot turtlebot3 burger</h3>

<div align="center">
  
[![Alt text](https://github.com/AldoCG25/LaberintoExam/blob/main/image.png)](https://youtu.be/EeLlrUJnqTU)
  
</div>
<br />

<a href="https://github.com/AldoCG25/LaberintoExam/blob/main/examen2.py">

Este código es un programa el cual el objetivo principal es que el robot “turtlebot3” tenga la capacidad de evadir objetos, esto lo realiza gracias a los tópicos que engloban los sensores laser y publica mensajes de movimiento en el topico “/cmd_vel”. Las primeras 4 líneas de este código, se encargan de importar los módulos necesarios de ROS para poder trabajar con el sensor lase asi como los mensajes de movimiento. 
 
import rospy: Esta línea importa el módulo rospy, que es la biblioteca principal utilizada para interactuar con ROS a través de Python. Proporciona funciones y herramientas para crear, inicializar y ejecutar nodos ROS, publicar y suscribirse a mensajes, y muchas otras cosas que se utilizan en la programación de robots.
 
from sensor_msgs.msg import LaserScan: Esta línea importa el mensaje LaserScan del paquete sensor_msgs. Los mensajes son la forma en que los diferentes componentes de un sistema ROS se comunican entre sí. En este caso, LaserScan es un mensaje que contiene datos de un escáner láser, que se utiliza comúnmente para la detección y mapeo de objetos en entornos robóticos.
 
from geometry_msgs.msg import Twist: Esta línea importa el mensaje Twist del paquete geometry_msgs. Twist es un mensaje que describe la velocidad y la dirección de un movimiento en un espacio tridimensional. Este mensaje se utiliza comúnmente para controlar el movimiento de un robot móvil, proporcionando una forma de enviar comandos de movimiento desde un nodo ROS a los actuadores del robot.
 
A continuación, se define una función de devolución de llamada “callback”, esta se ejecuta cada vez que se reciba un mensaje del láser. Dentro de la función “callback” se imprimen las distancias de los tres ángulos a utilizar (0, 90 y 270), en las líneas 10-15 se establecen los diferentes umbrales para detectar la distancia de los objetos, cada uno de ellos se utilizó en secciones posteriores, esto para calcular y conocer la distancia en diferentes direcciones.
 
Para configurar los ángulos de los cuales queremos obtener las distancias, en las líneas 19-21 se crearon tres variables las cuales se encargan de las distancias actuales del sensor, a la derecha, al frente y a la izquierda respectivamente. Una vez establecidas todas las variables y herramientas a utilizar para la navegación del robot en el mundo en Gazebo, se declaró una serie de condiciones “if-else” las cuales determinan el comportamiento del robot dentro del mapa, en función de los umbrales y las distancias de los obstáculos. 
 
En este caso, la implementación del programa para la evasión de obstáculos es relativamente simple, ya que, el robot avanza siempre y cuando no detecte algún objeto en el frente dentro del umbral establecido, el siguiente grupo de condiciones se encargan de girar hacia la derecha o hacia la izquierda dependiendo en que ángulo detecte obstáculos, es decir, si detecta obstáculos del lado derecho gira hacia la izquierda y viceversa. Finalmente, tenemos una condición doble, la cual se encarga de parar el robot una vez que se encuentre en el punto requerido.
 
Una vez terminadas las condiciones se publican los mensajes de movimiento los cuales son calculados por el tópico “/cmd_vel”, después tenemos la línea “move = Twist()” la cual crea un objeto de esta clase, que se utiliza para enviar comandos de movimiento al robot, la línea siguiente inicializa un nodo de ROS llamado "obstacle_avoidance_node" este comando es para indicar que el código que sigue está asociado con este nodo.
 
Finalmente tenemos la variable “pub” la cual crea un objeto de publicación el cual envía comandos de movimiento al robot a través del tópico "/cmd_vel". El objeto "pub" publica mensajes del tipo Twist () en este y el argumento queue_size=10 indica que el tamaño máximo de la cola de mensajes es de 10. La variable “sub” crea un objeto de suscripción el cual recibe datos de los sensores láser del robot a través del topico "/scan". El objeto "sub" está configurado para llamar a la función callback cada vez que llega un nuevo mensaje. Tenemos la última línea de código “rospy.spin()” la cual inicia el bucle de eventos de ROS, este procesa los mensajes entrantes, llama a las funciones de suscripción y maneja las publicaciones salientes, esta línea nos indica que el programa se ejecutará continuamente hasta que se detenga manualmente o se produzca una excepción.




  

