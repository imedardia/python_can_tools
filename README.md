Python CAN tools:
Those CAN tools are developed based on Linux SocketCAN and Python python-can package.

First step: Install pyhton-can package:
sudo pip install python-can

In order to be able to test using for Example a virtual CAN interface:
1- sudo modprobe vcan
2- sudo ip link add vcan0 type vcan
3- sudo ip link set vcan0 up

- can_dump.py: dump all CAN frames transiting on given interface

$ python can_dump.py vcan0
Timestamp: 1512572656.323818    ID: 00000000    010    DLC: 3    1d c3 1b
Timestamp: 1512572657.324961    ID: 00000001    010    DLC: 3    5d cd 37
Timestamp: 1512572660.055001        ID: 0000    000    DLC: 3    cc 3d 9d

- can_gen.py: Generate CAN Data based on random Arbitration ID and random
Data Buffer

$ python can_send.py -I vcan0 -L 3 -N 10 -E 1
