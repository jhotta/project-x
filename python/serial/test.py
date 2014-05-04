#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import struct

com = serial.Serial(port='/dev/cu.usbserial-A600aiiy',
                    baudrate=9600,
                    bytesize=serial.EIGHTBITS,
                    stopbits=serial.STOPBITS_ONE,
                    parity=serial.PARITY_NONE,
                    timeout=None,)
com.close()

print "start serial readline"
while True:
    com.open()
    #print '-----'
    data = ''
    for i in range(24):
        r = com.read()
        data += r
    print struct.unpack('cbHHHcbHHHcbHHH', data)
    print struct.unpack('24c', data)
    com.close()
