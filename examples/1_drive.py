import importHelper
import ev3

# Initialisiere den EV3 Brick.
ev3Brick = ev3.EV3Brick()
# Motoren initialisieren.
left_motor = ev3.Motor(ev3.Port.B)
right_motor = ev3.Motor(ev3.Port.C)

# DriveBase initialisieren.
robot = ev3.DriveBase(left_motor, right_motor,
                  wheel_diameter=55.5, axle_track=104)

# Einen Meter vorwärts gehen.
robot.straight(1000)
ev3Brick.speaker.beep()

# Einen Meter rückwärts gehen.
robot.straight(-1000)
ev3Brick.speaker.beep()

# 360 Grad im Uhrzeigersinn drehen.
robot.turn(360)
ev3Brick.speaker.beep()
