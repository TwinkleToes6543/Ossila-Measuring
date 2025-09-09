import time
from spectrum_calib import SpecCal
from Ossila import Ossila

specCal = SpecCal()
ossila = Ossila()

while True:
    devPower = ossila.measureVoltage()
    sunPower = specCal.getWavelength()

    with open("data.txt", "a") as f:
        f.write(str(float(devPower / sunPower * 100)))


    time.sleep(10)
