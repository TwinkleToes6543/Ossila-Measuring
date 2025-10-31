import time
import datetime
from spectrum_calib import SpecCal
from Ossila import Ossila

specCal = SpecCal()
ossila = Ossila()

while True:
    # Measure JV and irradiance
    devResults = ossila.measureVoltage()
    sunPower_uWcm2 = specCal.getWavelength()  # returns µW/cm²
    currentTime = datetime.datetime.now()

    # Convert µW/cm² → W/cm², apply calibration factor
    sunPower_mWcm2 = (sunPower_uWcm2 / 1_000)

    # Calculate efficiency (%)
    eff = (devResults["mPower"] / sunPower_mWcm2) * 1000
    eff = abs(eff)

    ff = (eff) / (devResults["voc"] * devResults["jsc"])

    print("voc:", devResults["voc"], "jsc:", devResults["jsc"], "ff:", ff, "eff:", eff)

    if(ff > 1):
        ff = 0.0
        eff = 0.0

    # Write data to file
    with open("data/data9.txt", "a") as f:
        f.write(
            f"\nEfficiency: {eff:.2f}% | "
            f"Jsc: {devResults["jsc"]:.3f} mA/cm² | "
            f"Voc: {devResults["voc"]:.3f} V | "
            f"Fill Factor: {ff:.3f} | "
            f"Date: {currentTime}"
        )

    time.sleep(10)
