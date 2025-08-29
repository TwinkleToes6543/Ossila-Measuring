import time
from spectrum_calib import SpecCal
from Ossila import Ossila

specCal = SpecCal()
ossila = Ossila()

while True:
    voltage, current = ossila.measureVoltage()
    wavelength, intensity = specCal.getWavelength()

    print(f"v: {voltage}, c: {current}, w: {wavelength}, i: {intensity}")

    time.sleep(10)