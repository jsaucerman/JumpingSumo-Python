JumpingSumo Control Library for Python

This is a fork of the repository:
https://github.com/haraisao/JumpingSumo-Python

So far, I have focused on porting the code to python3


1. About this project:
JumpingSumo is a small mobile robot produced by Parrot(http://www.parrot.com).
The SDK of this robot is already released on Github.com(https://github.com/Parrot-Developers).

This is a Python port of the Parrot SDK.

2. Quick start

   1. Power on your JumpingSumo and connect to the Wifi connection of the robot.
   2. start Python
   3. load library 
     - >> import sumo

   4. create controller; cnt
     - >> cnt = sumo.SumoController('MyCtrl')

   5. connect to the robot
     - >> cnt.connect()

   6. call 'move' function to confirm connection...
     - >> cnt.move(10)

   7. stop moving
     - >> cnt.move(0)

   8. please try to activate 'move', 'action', 'jump', 'posture' functions...
     - cnt.move(speed, turn_spped) ; speed = [-100:100],turn_speed = [-100:100]
     - cnt.action(param)           ; param = [0:9]
     - cnt.jump(param)             ; param = [0:1]
     - cnt.posture(param)          ; param = [0:2]
  
Acknowledgements
This repository was originally cloned from https://github.com/haraisao/JumpingSumo-Python
