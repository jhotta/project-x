#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()

# import sys
import logging
import time
# import libardrone.libardrone as ard

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
  logging.basicConfig(filename='flight.log',
                      level=logging.DEBUG)
  # # intilize
  # drone = ard.ARDrone()
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
  i = 0
  while i < 5:
    print "round: %d" % i
    for item in flight_route:
      direction, wait = item
      # print "%s:%f" % (direction, wait)
      if direction == "foward":
        print direction
        logging.debug(item)
      elif direction == "back":
        print direction
        logging.debug(item)
      elif direction == "right":
        print direction
        logging.debug(item)
      elif direction == "left":
        print direction
        logging.debug(item)
      elif direction == "hover":
        print direction
        logging.debug(item)
      else:
        print "error"
      navdata = "%s:%f \n" % (direction, wait)
      f = open('flight_recoder.txt', 'a+')
      f.write(navdata)
      f.close()
      print "wait %f sec." % wait
      time.sleep(wait)
    i += 1


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
  main()