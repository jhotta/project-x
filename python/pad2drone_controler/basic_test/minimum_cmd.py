#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import libardrone.libardrone as ard

drone = ard.ARDrone()

# emergency mode
drone.reset()

print "Taking off"
drone.takeoff()

print "Hovering"
for i in range(1000):
    drone.hover()
    time.sleep(0.001)

print "Landing"
drone.land()
time.sleep(1.0)

print "halting"
drone.halt()
