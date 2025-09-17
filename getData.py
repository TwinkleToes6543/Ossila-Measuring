import time
from spectrum_calib import SpecCal
from Ossila import Ossila
import datetime

specCal = SpecCal()
ossila = Ossila()

while True:
    devPower = ossila.measureVoltage()
    sunPower = specCal.getWavelength()

    currentTime = datetime.datetime.now()

    with open("data.txt", "a") as f:
        eff = float(devPower / sunPower * 100)
        if eff < 0: eff *= -1

        f.write("\n" + str(eff) + "; Date: " + str(currentTime))


    time.sleep(10)
