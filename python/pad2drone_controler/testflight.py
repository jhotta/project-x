#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()

# import sys
import time
import libardrone.libardrone as ard

def mTakeoff(drone):
  print "Takeoff...",
  drone.takeoff()

  print "Ok."

def mHovering(drone):
  print "Hovering..."
  drone.hover()
  print "Ok."

def mLanding(drone):
  print "Landing...",
  drone.land()
  print "Ok."

def full_hatl(drone):
  print "Shutting down...",
  drone.halt()
  print "Ok."

def main():
  drone = ard.ARDrone()
  drone.reset()
  time.sleep(1)
  mTakeoff(drone)
  # mHovering(drone)
  time.sleep(5)
  drone.turn_left()
  time.sleep(5)
  drone.turn_right()
  time.sleep(5)
  # drone.move_forward()
  # time.sleeP(1)
  # drone.move_backward()
  # time.sleeP(1)
  mLanding(drone)
  drone.halt()


if __name__ == "__main__":
  main()