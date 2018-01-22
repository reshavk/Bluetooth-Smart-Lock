from BT_proximity import bt_rssi
import time
import sys
import math

BT_ADDR = '0C:B3:19:B0:0C:D6'
NUM_LOOP = 30

def main():
    btrssi = bt_rssi.BluetoothRSSI(addr = BT_ADDR)

    n = 1.5
    c = 10
    A0 = 2
    actual_dist = 37
    sum_error = 0
    count = 0

    print btrssi

    for i in range(1, NUM_LOOP) :
        rssi_bt = float(btrssi.get_rssi())
        if(rssi_bt != 0 and i > 10):
            count = count + 1;
            x = float((rssi_bt-A0)/(-10*n))
            distance = (math.pow(10,x)*100)+c
            error = abs(actual_dist - distance)
            sum_error = sum_error + error
            avg_error = sum_error/count
            print "Average error : " + str(avg_error)
            print "Error : " + str(error)
            print "Approximate distance : " + str(distance)
            print "RSSI : "+str(rssi_bt)
            print "Count: " + str(count)
            print " "
        time.sleep(1)

if __name__ == '__main__' :
    main()