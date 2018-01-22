import bluetooth
from BT_proximity import bt_rssi
import time
import os
import sys

target_name = str(raw_input("Enter name of bluetooth-device : "))
target_address = None

while True:
    nearby_devices = bluetooth.discover_devices()

    for bdaddr in nearby_devices:
        if target_name == bluetooth.lookup_name(bdaddr):
            target_address = bdaddr
            break

    if target_address is not None:
        print "Device found : " + str(target_address)
        break
    else:
        print "Device not found"


def main():
    btrssi = bt_rssi.BluetoothRSSI(addr = target_address)
    while True:
        if int(btrssi.get_rssi()) == -1:
            os.popen('gnome-screensaver-command --lock')
        time.sleep(1);

if __name__ == '__main__':
    main()