#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()

import pygame
import sys

def init_gamepad():
  pygame.joystick.init()
  try:
    pad = pygame.joystick.Joystick(0) # create a joystick instance
    pad.init() # init instance
    return pad
  except pygame.error:
    print "Unexpected error:", sys.exc_info()[0]

def get_gamepad_action(pad):
  axis_value = {'0':0.0, '1':0.0, '2':0.0, '3':0.0}
  pygame.init()
  while 1:
    for e in pygame.event.get():
      if e.type == pygame.JOYAXISMOTION: # 7
        axis_value[str(e.axis)] = e.value
        print axis_value
      elif e.type == pygame.JOYHATMOTION: # 9
        print e.value
        #print 'hat motion'
      elif e.type == pygame.JOYBUTTONDOWN: # 10
        print "%s button pushed" % str(e.button)
      elif e.type == pygame.JOYBUTTONUP: # 11
        print "%s button released"% str(e.button)


if __name__ == "__main__":
  pad = init_gamepad()
  get_gamepad_action(pad)
