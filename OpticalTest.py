import pyvisa
import time

rm = pyvisa.ResourceManager()
print(rm.list_resources())
pm = rm.open_resource(rm.list_resources()[0])
print(pm.query("*IDN?"))

power = float(pm.query("MEAS:POW?"))
print(f"Power: {power} W")

# Continuous measurements
for i in range(10):
    power = float(pm.query("MEAS:POW?"))
    print(f"Measurement {i}: {power} W")
    time.sleep(1)