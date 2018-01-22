from BT_proximity import bt_rssi
import time
import os
import sys

BT_ADDR = '0C:B3:19:B0:0C:D6'

def main():
    btrssi = bt_rssi.BluetoothRSSI(addr = BT_ADDR)
    i = 0;
    while True:
        if  int(btrssi.get_rssi()) == -1:
            os.popen('gnome-screensaver-command --lock')
        time.sleep(1);

if __name__ == '__main__':
    main()