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


  

