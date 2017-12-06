import time
import sys
import can
can.rc['interface'] = 'socketcan_ctypes'
fmt_id = '{:08X}'
fmt_data = '{:02X}'

def can_help():
	print "can_send.py can_inf"
	print "example: can_send.py vcan0"

def can_dump(can_channel):
	bus = can.interface.Bus(channel=can_channel)
	while True:
		for msg in bus:
			print(msg)

if __name__ == '__main__':
	if(len(sys.argv) < 2):
		can_help()
		exit(1)
	can_dump(sys.argv[1])
