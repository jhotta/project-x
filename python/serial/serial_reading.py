#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import pdb; pdb.set_trace()

import serial
import struct
#import binascii

com = serial.Serial(port='/dev/cu.usbserial-A600aiiy',
                    baudrate=9600,
                    bytesize=serial.EIGHTBITS,
                    stopbits=serial.STOPBITS_ONE,
                    parity=serial.PARITY_NONE,
                    timeout=None,)


def get_paylaod():
    data = [0, 0]
    payload = []
    loop = True

    while True:
        # read serial sginals
        if data[0] != "~":
            data[0] = com.read()
        else:
            data[1] = com.read()
            # print '-----'
            if data[1] in ['1', '2', '3', '4']:
                payload.append(data[1])
                # print "---------------"
                while loop:
                    payload.append(com.read())
                    if payload[-1] == '~':
                        loop = False
                # print payload[:-1]
                return payload[:-1]
            else:
                data[0] = data[1]


def get_sonic_val(upper, lower):
    return (upper << 8) + lower


def get_check_sum(upper, lower, pos):
    return (upper + lower + pos) & 255


def get_correct_val(value):
    return value ^ 32


def main():
    while True:
        bucket = []
        check = []
        payload = get_paylaod()
        payload.reverse()
        print payload
        for item in payload:
            # print struct.unpack('B', item)[0]
            try:
                if item == "}":
                        bucket.append(get_correct_val(bucket.pop()))
                else:
                    temp = struct.unpack('B', item)[0]
                    bucket.append(temp)
                    check.append(temp)
                # print bucket
                # print check
            except:
                print "error: building payload! skipping this data!"

        try:
            if bucket[0] == get_check_sum(check[1], check[2], check[3]):
                print "-------"
                print "checksum value: %s" % bucket[0]
                print "sonic value: %d" % \
                    get_sonic_val(bucket[1], bucket[2])
                print "-------\n"
            else:
                print "data error: chechsum dose not match!"
                print bucket
                print "\n\n"
        except:
            print "pass"
            pass

if __name__ == '__main__':
    main()
