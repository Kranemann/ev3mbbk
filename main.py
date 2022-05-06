#!/usr/bin/env pybricks-micropython
import os
os.write(1, b'\x1b[2J\x1b[H')
import ev3
