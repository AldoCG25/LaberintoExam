# LaberintoExam
 
<div id="top"></div>
<br />
<div align="center">
  <a href="[github.com/JosueLara22/PicknPlace-for-Open_Manipulator](https://github.com/AldoCG25/LaberintoExam.git)">
    <img src="https://github.com/AldoCG25/LaberintoExam/blob/main/IMG-1384.jpg" alt="Logo" width="200" height="200">
  </a>

<h3 align="center">Laberinto Examen</h3>

  <p align="center">
    Resolución del Laberinto Maze 3 6x6 con TurtleBot3 "Burger"
  </p>
</div>



## Sobre el examen
This is a pick and place implementation for the Open Manipulator X robot using Ubutntu 20.04, ROS Noetic and the keyboard teleoperation tutorial as the foundation.

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">Sobre el examen</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li>
      <a href="#usage-and-implementation-video">Usage and Implementation Video</a>
    </li>   
    <li>
      <a href="#modifications-to-the-original-project">Modifications to the original project</a>
    </li>  
    <li>
      <a href="#contact">Contact</a>
    </li>
  </ol>
</details>

## Getting Started

<p align="right">(<a href="#top">back to top</a>)</p>

### Prerequisites
For the implementation you will need Ubuntu 20.04 on your computer (not recommended on Virtual Box).
### Installation
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
4. Install controllers and pakages
```sh
source ~/.bashrc	 
sudo apt-get install ros-noetic-ros-controllers ros-noetic-gazebo* ros-noetic-moveit* ros-noetic-industrial-core	 
sudo apt install ros-noetic-dynamixel-sdk ros-noetic-dynamixel-workbench*
sudo apt install ros-noetic-robotis-manipulator
```
5. Install Open Manipulator Pakages
```sh
cd ~/catkin_ws/src/
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/open_manipulator.git
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/open_manipulator_msgs.git
git clone -b noetic-devel https://github.com/ROBOTIS-GIT/open_manipulator_simulations.git
git clone https://github.com/ROBOTIS-GIT/open_manipulator_dependencies.git
```
6. Remove original file	and replace it with PicknPlace program
```sh
cd ~/catkin_ws/src/open_manipulator/open_manipulator_teleop/src/
rm open_manipulator_teleop_keyboard.cpp
git clone https://github.com/JosueLara22/PicknPlace-for-Open_Manipulator.git
cd PicknPlace-for-Open_Manipulator/open_manipulator_teleop/src/
mv open_manipulator_teleop_keyboard.cpp ~/catkin_ws/src/open_manipulator/open_manipulator_teleop/src/
cd ~/catkin_ws/src/open_manipulator/open_manipulator_teleop/src/
rm -rf PicknPlace-for-Open_Manipulator	
cd ~/catkin_ws && catkin_make
clear
```
7. Run communication with Robot
```sh
roslaunch open_manipulator_controller open_manipulator_controller.launch usb_port:=/dev/ttyACM0 baud_rate:=1000000
```
When the communication launch command has correctly run, an overview of the parameters and nodes that are recognized by ROS is displayed. The Dynamixel motors are listed with their corresponding ID and model, as well as showing that the communication was successfully initiated.
Below is a screenshot of the communication instruction execution and displayed summary.

   <br />
<div align="center">
  <a href="github.com/JosueLara22/PicknPlace-for-Open_Manipulator">
<img src="Images/comunicacionexitosaconrobot.png" alt="Captura1" width="900" height="600">
  </a>
</div>
<br />

8. Run file Pick and Place (in new Tab)
```sh
roslaunch open_manipulator_teleop open_manipulator_teleop_keyboard.launch
```
When executing the launch program, an overview of parameters and nodes is displayed in a similar way as in the communication instruction.
Subsequently, a short description of what instruction the robot is doing from Pick and Place program, the angles of each joint and the position of the end effector is shown. Being 1-8 displacement moves, g the gripper opening and f the gripper closing.
Below is a screenshot of the execution of the statement with the termination .launch.

  <br />
<div align="center">
  <a href="github.com/JosueLara22/PicknPlace-for-Open_Manipulator">
<img src="Images/programapicknplacecorriendoexitosamente.png" alt="Captura2" width="900" height="600">
  </a>
</div>
<br />

## Usage and Implementation Video

<p align="right">(<a href="#top">back to top</a>)</p>

<h3 align="left">Pick and Place for Open ManipulatorX YOUTUBE Video</h3>

<div align="center">
  
[![Alt text](https://img.youtube.com/vi/eiSbc5Rm95E/0.jpg)](https://www.youtube.com/watch?v=eiSbc5Rm95E)
  
</div>
<br />


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
