#! /usr/bin/python

import sys
file = open('/dev/input/js0','r')
data = []

while 1:
	for charcter in file.read(1):
		# print charcter
		print ord(charcter)
		data += ['%02X' % ord(charcter)]
		print data
		if len(data) == 8:
			for byte in data:
				sys.stdout.write(byte+' ')
			sys.stdout.write('\n')
			sys.stdout.flush()
			data = []	