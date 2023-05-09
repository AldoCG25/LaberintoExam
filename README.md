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
En este proyecto, se utilizará el Turtlebot3 Burger para resolver un laberinto del repositorio https://github.com/rfzeg/plywood_mazes.git. Para lograr este objetivo, se ha desarrolló un código que permite guiar al robot hacia un punto específico en el mapa, en este caso, para resolver el laberinto y que el robot termine en la esquina superior derecha del mapa Maze 3.

### Requisitos
Para llevar a cabo el proyecto de manera efectiva, se recomienda contar con la versión de Ubuntu 20.04 instalada en una máquina virtual o en una partición del disco duro de su dispositivo. Esto permitirá una mayor estabilidad y compatibilidad con las herramientas utilizadas durante el proyecto.
### Instalación
1. Instalar ROS Noetic en modo administrador
2. Instalar Github
```sh 
 sudo apt-get install git-all
```
3. Instalar ROS Noetic (Copiar los comandos en Terminal)
```sh 
sudo apt update 
wget https://raw.githubusercontent.com/ROBOTIS-GIT/robotis_tools/master/install_ros_noetic.sh
chmod 755 ./install_ros_noetic.sh
bash ./install_ros_noetic.sh
```  
4. Instalar controladores y paquetes del turtlebot3 como se describe en el siguiente repositorio:
https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/

5. Clonar los paquetes de GitHub en donde se encuntran los laberintos, el comando 'cd' para se utiliza para cambiar al directorio donde se desea clonar el paquete.
```sh
cd <catkin_ws>
cd <src>
```
6. Dentro de la dirección src se clona el Github con el URL del paquete (por lo general se encuentra en la pestaña "Code" del repositorio), para ello, se ejecuta el comando 'git clone <URL>'
```sh
git clone https://github.com/rfzeg/plywood_mazes.git
```
 7. Se abre una ventana en terminal y se ejecuta el siguiente comando 'roslaunch plywood_mazes maze_3_6x6.launch', este lanza todos los nodos especificados en el archivo maze_3_6x6.launch y configura el entorno según las instrucciones en ese archivo.
```sh
roslaunch plywood_mazes maze_3_6x6.launch
```
 8. En otra ventana de terminal, se ejecuta el siguiente comando 'roslaunch plywood_mazes spawn_turtlebot3.launch', este lanza todos los nodos especificados en el archivo spawn_turtlebot3.launch y spawnea al robot el el laberinto de Gazebo.
 ```sh
roslaunch plywood_mazes spawn_turtlebot3.launch
```
 9. Por último, en una nueva ventan de teminal ejecutar archivo .py creado para la solución del laberinto.
 ```sh
rosrun plywood_mazes examen2.py
 ```




## Video de implementación

<p align="right">(<a href="#top">back to top</a>)</p>

<h3 align="left">Solución al laberinto con robot turtlebot3 burger</h3>

<div align="center">
  
[![Alt text](https://github.com/AldoCG25/LaberintoExam/blob/main/image.png)](https://youtu.be/EeLlrUJnqTU)
  
</div>
<br />
 
## Código Examen.py
Explicacion del código 
<a href="https://github.com/AldoCG25/LaberintoExam/blob/main/examen2.py">
examen2.py
  </a>
:
 
Este código es un programa el cual el objetivo principal es que el robot “turtlebot3” tenga la capacidad de evadir objetos, esto lo realiza gracias a los tópicos que engloban los sensores laser y publica mensajes de movimiento en el topico “/cmd_vel”. Las primeras 4 líneas de este código, se encargan de importar los módulos necesarios de ROS para poder trabajar con el sensor lase asi como los mensajes de movimiento. 
 
-import rospy: Esta línea importa el módulo rospy, que es la biblioteca principal utilizada para interactuar con ROS a través de Python. Proporciona funciones y herramientas para crear, inicializar y ejecutar nodos ROS, publicar y suscribirse a mensajes, las cuales son las principales que se utilizan en la programación de robots.
 
-from sensor_msgs.msg import LaserScan: Esta línea importa el mensaje LaserScan del paquete sensor_msgs. En este caso, LaserScan es un mensaje que contiene datos de un escáner láser, que se utlizó para la detección y mapeo de objetos en el mundo escogido.
 
-from geometry_msgs.msg import Twist: Esta línea importa el mensaje Twist del paquete geometry_msgs. Twist es un mensaje que describe la velocidad y la dirección de un movimiento en un espacio tridimensional. Este mensaje se utilizó para controlar el movimiento de del robot, proporcionando una forma de enviar comandos de movimiento desde un nodo ROS a los motores del robot.
 
A continuación, se define una función de devolución de llamada “callback”, esta se ejecuta cada vez que se reciba un mensaje del láser. Dentro de la función “callback” se imprimen las distancias de los tres ángulos a utilizar (0, 90 y 270), en las líneas 10-15 se establecen los diferentes umbrales para detectar la distancia de los objetos, cada uno de ellos se utilizó en secciones posteriores, esto para calcular y conocer la distancia en diferentes direcciones.
 
Para configurar los ángulos de los cuales queremos obtener las distancias, en las líneas 19-21 se crearon tres variables (umbral) las cuales permiten compar distancias actuales del sensor, a la derecha, al frente y a la izquierda respectivamente. Una vez establecidas todas las variables y herramientas a utilizar para la navegación del robot en el mundo en Gazebo, se declaró una serie de condiciones “if-else” las cuales determinan el comportamiento del robot dentro del mapa, en función de los umbrales y las distancias de los obstáculos. 
 
En este caso, la implementación del programa para la evasión de obstáculos es relativamente simple, ya que, el robot avanza siempre y cuando no detecte algún objeto en el frente dentro del umbral establecido, el siguiente grupo de condiciones se encargan de girar hacia la derecha o hacia la izquierda dependiendo en que ángulo detecte obstáculos, es decir, si detecta obstáculos del lado derecho gira hacia la izquierda y viceversa. Finalmente, tenemos una condición doble, la cual se encarga de parar el robot una vez que se encuentre en el punto requerido.
 
Una vez terminadas las condiciones se publican los mensajes de movimiento los cuales son calculados por el tópico “/cmd_vel”, después tenemos la línea “move = Twist()” la cual crea un objeto de esta clase, que se utiliza para enviar comandos de movimiento al robot, la línea siguiente inicializa un nodo de ROS llamado "obstacle_avoidance_node" este comando es para indicar que el código que sigue está asociado con este nodo.
 
Finalmente tenemos la variable “pub” la cual crea un objeto de publicación el cual envía comandos de movimiento al robot a través del tópico "/cmd_vel". El objeto "pub" publica mensajes del tipo Twist () en este y el argumento queue_size=10 indica que el tamaño máximo de la cola de mensajes es de 10. La variable “sub” crea un objeto de suscripción el cual recibe datos de los sensores láser del robot a través del topico "/scan". El objeto "sub" está configurado para llamar a la función callback cada vez que llega un nuevo mensaje. Tenemos la última línea de código “rospy.spin()” la cual inicia el bucle de eventos de ROS, este procesa los mensajes entrantes, llama a las funciones de suscripción y maneja las publicaciones salientes, esta línea nos indica que el programa se ejecutará continuamente hasta que se detenga manualmente o se produzca una excepción.




  

