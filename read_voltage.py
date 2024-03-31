from ina219 import INA219, DeviceRangeError

SHUNT_OHMS = 0.1  # Adjust this value based on your specific module's shunt resistor value

def read_ina219():
    # Specify bus number 7 here since your device is on bus 7
    # I connect the I2C pins of INA219 to pin 3 and 5 of jetson orin nano
    ina = INA219(SHUNT_OHMS, busnum=7)
    ina.configure()

    print("Reading from INA219...")
    try:
        print("Bus Voltage: {:.3f} V".format(ina.voltage()))
        print("Bus Current: {:.3f} mA".format(ina.current()))
        print("Power: {:.3f} mW".format(ina.power()))
        print("Shunt Voltage: {:.3f} mV".format(ina.shunt_voltage()))
    except DeviceRangeError as e:
        # Current out of device range with specified shunt resistor
        print(e)

if __name__ == "__main__":
    read_ina219()
