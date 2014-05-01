#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()

# import sys
import time
import libardrone.libardrone as ard

def keepCmmSleep(drone, sec):
  resolution = 30.0
  t = sec * resolution
  n = 0
  while n <= t:
    time.sleep(1.0 / resolution)
    drone.commwdg()
    n += 1
  return


def main():
  # intilize
  drone = ard.ARDrone()
  drone.reset()
  print "reset done"
  drone.set_speed = 0.1
  print drone.get_navdata()
  keepCmmSleep(1)

  # takeoff
  print "taking off"
  drone.apply_command(takeoff)
  print drone.get_navdata()
  print "havering"
  keepCmmSleep(8)

  # # hight speed left turn
  # #drone.speed = 0.5
  # drone.turn_left()
  # print "trun left"
  # keepCmmSleep(2)

  # # haver
  # drone.haver()
  # keepCmmSleep(2)

  # drone.move_right()
  # keepCmmSleep(1)

  # # haver
  # drone.haver()
  # keepCmmSleep(2)

  # # low speed right turn
  # drone.set_speed = 0.2
  # drone.turn_right()
  # keepCmmSleep(1)




  # landing
  print "landiing"
  drone.apply_command(land)
  print drone.get_navdata()
  keepCmmSleep(2)
  print "landed"
  drone.apply_command(halt)
  print drone.get_navdata()
  print "halted"


if __name__ == "__main__":
  main()