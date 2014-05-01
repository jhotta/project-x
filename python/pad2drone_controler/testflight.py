#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()

# import sys
import logging
import time
#import libardrone.libardrone as ard

def keepCmmSleep(drone, sec):
  resolution = 30.0
  t = sec * resolution
  n = 0
  while n <= t:
    time.sleep(1.0 / resolution)
    drone.commwdg()
    n += 1
  return

def travel(direction, unit, resolution):
  t = 1.0/resolution
  i = 0
  while i <= unit:
    #drone.apply_command(drone.forward())
    print direction
    time.sleep(t)
    #drone.apply_command(drone.hover())
    i += 1

def main(flight_route, resolution):
  logging.basicConfig(filename='flight.log',
                      level=logging.DEBUG)
  # # intilize
  #drone = ard.ARDrone()
  # drone.reset()
  # print "reset done"
  # drone.set_speed = 0.1
  # print drone.get_navdata()
  # keepCmmSleep(1)

  # # takeoff
  # print "taking off"
  # drone.apply_command(drone.takeoff())
  # print drone.get_navdata()
  # print "havering"
  # keepCmmSleep(1)

  # move to inital position
  # drone.apply_command(drone.forward())
  # print drone.get_navdata()
  # print "havering"
  # keepCmmSleep(1)

  # programed flight

  for item in flight_route:
    direction, unit = item
    # print "%s:%f" % (direction, unit)
    if direction == "foward":
      logging.debug(item)
      travel(direction, unit, resolution)
    elif direction == "back":
      logging.debug(item)
      travel(direction, unit, resolution)
    elif direction == "right":
      logging.debug(item)
      travel(direction, unit, resolution)
    elif direction == "left":
      logging.debug(item)
      travel(direction, unit, resolution)
    elif direction == "hover":
      logging.debug(item)
      travel(direction, unit, resolution)
    else:
      print "error"
    navdata = "%s:%f \n" % (direction, unit)
    f = open('flight_recoder.txt', 'a+')
    f.write(navdata)
    f.close()



  # # landing
  # print "landiing"
  # drone.apply_command(drone.land())
  # print drone.get_navdata()
  # keepCmmSleep(2)
  # print "landed"
  # drone.apply_command(drone.halt())
  # print drone.get_navdata()
  # print "halted"



if __name__ == "__main__":

  flight_route = (
         ("foward", 40),
         ("right", 160),
         ("hover", 50),
         ("foward", 160),
         ("hover", 50),
         ("left", 160),
         ("hover", 50),
         ("right", 150),
         ("hover", 50),
         ("back", 160),
         ("hover", 50),
         ("left", 150),
         ("hover", 50)
         )

  main(flight_route, 10)