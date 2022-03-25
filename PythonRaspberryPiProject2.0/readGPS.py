import gpsd
from time import sleep

gpsd.connect()

while True:
    packet = gpsd.get_current()
    try:
        print(packet.position())
        print("Position successfully determined")
    except:
        print("Position could not be determined")
    sleep(5)