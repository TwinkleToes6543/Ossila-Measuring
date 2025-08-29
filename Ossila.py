from xtralien import Device
from decimal import Decimal
import numpy as np
import matplotlib.pyplot as plt

class Ossila():
    def measureVoltage(self):
        port = "/dev/ttyACM0"
        voltage = 0.7

        v = Decimal(str(voltage))  # use high precision
        with Device(port) as smu:
            result = smu.smu1.oneshot(v)[0]  # [voltage, current]
            return float(result[0]), float(result[1])
