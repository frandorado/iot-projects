# RST01BL E27 7W RGB Bluetooth Ligth Bulb
# Author: Francisco Dorado

import math
import sys
import time

import pexpect

# Get bulb address from command parameters.
if len(sys.argv) != 2:
    print 'Error you must specify bulb address as parameter'
    print 'Example: sudo python stop-light.py XX:XX:XX:XX:XX:XX'
    sys.exit(1)
bulb = sys.argv[1]

# Run gatttool interactively.
gatt = pexpect.spawn('gatttool -I')

# Connect to the device.
gatt.sendline('connect {0}'.format(bulb))
gatt.expect('Connection successful')

# Send "Stop"
gatt.sendline('char-write-cmd 0x0043 CC2433')

# Quit gattool
gatt.sendline('quit')


