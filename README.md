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
## Código Examen.py


## Video de implementación

<p align="right">(<a href="#top">back to top</a>)</p>

<h3 align="left">Solución al laberinto con robot turtlebot3 burger</h3>

<div align="center">
  
[![Alt text](https://github.com/AldoCG25/LaberintoExam/blob/main/image.png)](https://youtu.be/EeLlrUJnqTU)
  
</div>
<br />


  

