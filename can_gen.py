import time
import sys
import argparse
import random

import can
can.rc['interface'] = 'socketcan_ctypes'


def can_producer(can_channel, can_dlc, can_ext, count):
	bus = can.interface.Bus(channel=can_channel)
	can_id = list(range(count))
	can_data = list(bytearray([random.randrange(0, 255)
					   for a in range(can_dlc)])
			for b in range(count))
	for i in range(count):
		m = can.Message(
			arbitration_id=can_id[i],
			extended_id=can_ext,
			dlc=can_dlc,
			data=can_data[i]
		)
		#print(m)
		bus.send(m)
		time.sleep(1)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Process Prog arguments  ')
	parser.add_argument('-I', type=str , action="store", required=True, dest='channel' , default="vcan0", help='CAN Interface')
	parser.add_argument('-L', type=int , action="store", required=True, dest='dlc'     , default=8      , help='CAN Data Length')
	parser.add_argument('-E', type=bool, action="store", required=False, dest='ext'    , nargs="?", default=False  , help='Extended ID    ')
	parser.add_argument('-N', type=int,  action="store", required=True, dest='count'   , default=0      , help='Num of Messages To send')
	results = parser.parse_args()
	can_producer(results.channel, results.dlc, results.ext, results.count)

