# runSumo.py

# load library
import sumo

# create controller; cnt
cnt = sumo.SumoController('MyCtrl')

# connect to the robot
cnt.connect()

# 6. call 'move' function to confirm connection...
cnt.move(10)

#   7. stop moving
cnt.move(0)

#   8. please try to activate 'move', 'action', 'jump', 'posture' functions...
#     - cnt.move(speed, turn_spped) ; speed = [-100:100],turn_speed = [-100:100]
#     - cnt.action(param)           ; param = [0:9]
#     - cnt.jump(param)             ; param = [0:1]
#     - cnt.posture(param)          ; param = [0:2]
#  