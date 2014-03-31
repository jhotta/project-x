#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()

import sys
#import time
import pygame
from pygame.locals import *
#import pygame.surfarray
#import pygame.transform
import libardrone.libardrone as ard


def init_gamepad():
  pygame.joystick.init()
  try:
    pad = pygame.joystick.Joystick(0) # create a joystick instance
    pad.init() # init instance
    return pad
  except pygame.error:
    print "Unexpected error:", sys.exc_info()[0]


def init_ardrone():
  try:
    drone = ard.ARDrone()
    drone.reset()
    return drone
  except:
    print "Unexpected error:", sys.exc_info()[0]


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
  full_hatl(drone)


def full_hatl(drone):
  print "Shutting down...",
  drone.halt()
  print "Ok."


def get_gamepad_action(pad, drone):

  Width, Hight = 320, 240
  axis_value = {'0':0.0, '1':0.0, '2':0.0, '3':0.0}
  bt_status = [0,0,0,0,0,0,1,1,0,0,0,0,0]

  pygame.init()
  pygame.display.set_mode((Width, Hight))
  clock = pygame.time.Clock()
  running = True

  while running:
    for e in pygame.event.get():
      if e.type == QUIT: # 終了が押された？
        return
      if (e.type == KEYDOWN and
        e.key  == K_ESCAPE): # ESCが押された？
        return
      if e.type == pygame.JOYAXISMOTION: # 7
        axis_value[str(e.axis)] = e.value
        print axis_value
      elif e.type == pygame.JOYHATMOTION: # 9
        print e.value
        print 'hat motion'
      elif e.type == pygame.JOYBUTTONDOWN: # 10
        print "%s button pushed" % str(e.button)
        bt_status[e.button] = 1
        if bt_status[4] == 1 and bt_status[5] == 1:
          print "takeoff"
          #mTakeoff(drone)
        elif bt_status[6] == 1 and bt_status[7] == 1:
          print "Landing"
          #mLanding(drone)
        elif bt_status[0] == 1:
          print "away(left turn)"
        elif bt_status[1] == 1:
          print "going down"
        elif bt_status[2] == 1:
          print "comeby(right turn)"
        elif bt_status[3] == 1:
          print "going up"
        print bt_status
      elif e.type == pygame.JOYBUTTONUP: # 11
        print "%s button released"% str(e.button)
        bt_status[e.button] = 0
        print bt_status
    # print bt_status


def main():
  pad = init_gamepad()
  drone = init_ardrone()
  get_gamepad_action(pad, drone)
  # mTakeoff(drone)
  # mHovering(drone)
  # # time.sleep(1)
  # mLanding(drone)


if __name__ == "__main__":
  main()