from decimal import Decimal
import time
import xtralien

class Ossila():
    def measureVoltage(self):
        port = "/dev/ttyACM0" # USB COM port number of the connected Source Measure Unit
        channel = 'smu2'  # SMU channel to use
        i_range = 1  # Current range to use, see manual for details

        # Parameters are defined using the Decimal class to avoid floating point errors
        start_v = Decimal('8.3')  # Sweep start voltage in volts
        end_v = Decimal('-0.1')  # Sweep end voltage in volts
        inc_v = Decimal('0.04')  # Sweep voltage increment in volts
        power = []

        # Connect to the Source Measure Unit using USB
        with xtralien.Device(port) as SMU:
            # Set the current range for SMU 1
            SMU[channel].set.range(i_range, response=0)
            time.sleep(0.05)
            # Turn on SMU 1
            SMU[channel].set.enabled(True, response=0)
            time.sleep(0.05)

            #Initialise the set voltage
            set_v = start_v
            # Loop through the voltages to measure
            while set_v > end_v:
                # Set voltage, measure voltage and current
                # voltage, current = SMU[channel].oneshot(set_v)
                result = SMU[channel].oneshot(set_v)
                try:
                    voltage, current = result[0]
                except:
                    break

                # Get power
                power.append((current * voltage) / 10.23)

                # Increment the set voltage
                set_v += inc_v

            # Get max power
            mPower = max(power)

            # Reset output voltage and turn off SMU 1
            SMU[channel].set.voltage(0, response=0)
            time.sleep(0.1)
            SMU[channel].set.enabled(False, response=0)

            return mPower
