
import minimalmodbus
import time

minimalmodbus.TIMEOUT = 0.5

class RD6006(minimalmodbus.Instrument):
    def __init__(self, port, address=1, baudrate=115200):
        super().__init__(port, address)
        self.serial.baudrate = baudrate
        self.serial.timeout = 0.5
        self.serial.stopbits = 1
        self.mode = minimalmodbus.MODE_RTU
        self.clear_buffers_before_each_transaction = True
        self.serialnumber = self.read_string(0, 16)
        self.firmware = self.read_string(16, 3)
        self.type = self.read_register(19, 0, 3, False)
        if self.type == 6012 or self.type == 6018 or self.type == 6024:
            print(f"Model RD60{self.type} detected.")
            self.maxVoltage = self.type
            self.maxCurrent = 12 if self.type == 6012 else 18 if self.type == 6018 else 24

    # Existing methods would go here...

    def set_power(self, power):
        """Sets a specific power output by adjusting the current."""
        voltage = self.measvoltage
        if voltage == 0:
            print("Voltage is zero, cannot set power.")
            return
        current = power / voltage
        self.current = current

    def set_power_continuous(self, power, delay=1):
        """Sets a specific power output by adjusting the current, and keeps adjusting it continuously."""
        while True:
            self.set_power(power)
            time.sleep(delay)

if __name__ == "__main__":
    import serial.tools.list_ports

    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if "USB-SERIAL CH340" in p.description:
            rd = RD6006(p.device)
            print(rd.status())

            mode = input("Enter mode (constant current, constant wattage, constant voltage): ")
            if mode == "constant wattage":
                power = float(input("Enter desired power (W): "))
                rd.set_power_continuous(power)
            elif mode == "constant current":
                current = float(input("Enter desired current (A): "))
                rd.current = current
            elif mode == "constant voltage":
                voltage = float(input("Enter desired voltage (V): "))
                rd.voltage = voltage
            else:
                print("Unknown mode.")
