#!/usr/bin/bash python3
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.tools import wait

try:
    from pybricks._common import Motor
except ImportError:
    pass
