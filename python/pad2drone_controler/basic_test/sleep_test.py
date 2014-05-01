#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()

# import sys
import time
#import libardrone.libardrone as ard

def sleep(sec):
  resolution = 100.0
  t = sec * resolution
  n = 0
  while n <= t:
    time.sleep(1.0 / resolution)
    print n
    n += 1
  print "waited %f secs" % sec
  return


def main():
  sleep(8)
  print "done"

if __name__ == "__main__":
  main()