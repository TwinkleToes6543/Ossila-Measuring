from decimal import Decimal
import time

import xtralien
import numpy as np

com_no = 3  # USB COM port number of the connected Source Measure Unit
channel = 'smu1'  # SMU channel to use
i_range = 1  # Current range to use, see manual for details
dev_area = 0.049 # Area of the device in cm^2

# Parameters are defined using the Decimal class to avoid floating point errors
start_v = Decimal('1.2')  # Sweep start voltage in volts
end_v = Decimal('-0.1')  # Sweep end voltage in volts
inc_v = Decimal('0.02')  # Sweep voltage increment in volts

voltages = []
currents = []

# Connect to the Source Measure Unit using USB
with xtralien.Device(f'COM{com_no}') as SMU:
    # Set the current range for SMU 1
    SMU[channel].set.range(i_range, response=0)
    time.sleep(0.05)
    # Turn on SMU 1
    SMU[channel].set.enabled(True, response=0)
    time.sleep(0.05)

    #Initialise the set voltage
    set_v = start_v
    # Loop through the voltages to measure
    while set_v >= end_v:
        # Set voltage, measure voltage and current
        voltage, current = SMU[channel].oneshot(set_v)[0]

        voltages.append(voltage)
        currents.append(-current * 1000 / dev_area)

        # Print measured voltage and current
        # print(f'V: {voltage} V; I: {current} A')

        # Increment the set voltage
        set_v -= inc_v

    # Reset output voltage and turn off SMU 1
    SMU[channel].set.voltage(0, response=0)
    time.sleep(0.1)
    SMU[channel].set.enabled(False, response=0)


# Convert lists to numpy arrays
V = np.array(voltages)          # Voltage in Volts
I_A = np.array([i / 1000 * dev_area for i in currents])  # Back-convert to A from mA/cm²
I_J = np.array(currents)        # Current density in mA/cm²

# Sort by voltage
idx = np.argsort(V)
V = V[idx]
I_A = I_A[idx]
I_J = I_J[idx]

# Interpolate Jsc at V = 0
Jsc = np.interp(0, V, I_J)  # mA/cm²
print("Jsc (mA/cm²):", Jsc)

# Interpolate Voc at I = 0
Voc = np.interp(0, I_J[::-1], V[::-1])  # V
print("Voc (V):", Voc)

# --- Maximum power point (total power in Watts) ---
P_W = V * I_A                 # Power in Watts
Pmax_index = np.argmax(P_W)
Vmp = V[Pmax_index]
Imp = I_A[Pmax_index]
Pmax = P_W[Pmax_index]
print("Vmp (V):", Vmp)
print("Imp (A):", Imp)
print("Pmax (W):", Pmax)

# Fill Factor (dimensionless)
FF = Pmax / (Voc * (Jsc / 1000 * dev_area)) * 100  # Use same units: Voc in V, Isc in A
print("Fill Factor (%):", FF)

print("PCE:", (FF * Jsc * Voc / 100), "%")
