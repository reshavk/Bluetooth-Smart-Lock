# Bluetooth-Smart-Lock
Trying to implement the window's "Bluetooth Smart Lock" feature for ubuntu.


## TO TEST ON YOUR SYSTEM
    Clone/Download the repository
   
    Execute find_my_phone.py using Python 2.
        python2 find_my_phone.py
    
    Provide your bluetooth device name
    
    Wait for few minutes since bluetooth discovery takes time
    
    Once device found message is displayed, move away from your system and it should get locked on its own.
    
## NOTE
This project utilizes RSSI value (received signal strength indicator) to estimate distance between the system and device.
This method is not one of the best ways to get idea about the distance, as it is affected by noise to a large extent.
This project is still in its development phase and hence may not perform as accurate as it's windows couterpart. 
