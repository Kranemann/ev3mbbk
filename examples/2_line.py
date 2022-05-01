import importHelper
import ev3

brick = ev3.EV3Brick()


# Controls the motors
Linke_Motor = ev3.Motor(ev3.Port.A)
Rechte_Motor = ev3.Motor(ev3.Port.B)
robot = ev3.DriveBase(Linke_Motor, Rechte_Motor,
                      wheel_diameter=55.5, axle_track=104)


# Einstellungen
robot.settings(200, 100,100,45)


# Nehmen wir an, dass der Sensor an Port S1 angeschlossen ist
line_sensor = ev3.ColorSensor(ev3.Port.S1)


# Threshold berechnen
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2


Geschwindigkeit_pro_sekunde = 100

PROPOTIONALER_ANSTIEG = 1.2

# Start following the line endlessly.
while True:
    # Calculate the deviation from the threshold.
    if(line_sensor.reflection()is None):
        raise Exception("Sensor is not connected") 
    deviation = line_sensor.reflection() - threshold

    # Calculate the turn rate.
    turn_rate = PROPOTIONALER_ANSTIEG * deviation

    # Set the drive base speed and turn rate.
    robot.drive(Geschwindigkeit_pro_sekunde, turn_rate)
