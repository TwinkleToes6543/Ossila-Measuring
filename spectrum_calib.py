# spectrum_calib.py
from libspec import ASQESpectrometer
import numpy as np
import matplotlib.pyplot as plt

spec = ASQESpectrometer()
spec.configure_acquisition()

class SpecCal():
    def getWavelength(self):
        try:
            wavelength, intensity = spec.normalize_spectrum()
            return wavelength, intensity
        except KeyboardInterrupt:
            pass