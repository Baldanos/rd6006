import minimalmodbus
minimalmodbus.TIMEOUT = 0.5

class RD6006:

    def __init__(self, port, address=1, baudrate=115200):
        self.port = port
        self.address = address
        self.instrument = minimalmodbus.Instrument(port=port, slaveaddress=address)
        self.instrument.serial.baudrate=baudrate
        regs = self._read_registers(2, 2)
        self.sn = regs[0]
        self.fw = regs[1]/100

    def __repr__(self):
        return f"RD6006 SN:{self.sn} FW:{self.fw}"

    def _read_register(self, register):
        try:
            return self.instrument.read_register(register)
        except minimalmodbus.NoResponseError:
            return self._read_register(register)

    def _read_registers(self, start, length):
        try:
            return self.instrument.read_registers(start, length)
        except minimalmodbus.NoResponseError:
            return self._read_registers(start, length)
        except minimalmodbus.InvalidResponseError:
            return self._read_registers(start, length)

    def _write_register(self, register, value):
        try:
            return self.instrument.write_register(register, value)
        except minimalmodbus.NoResponseError:
            return self._write_register(register, value)

    def status(self):
        regs = self._read_registers(0, 100)
        print("== Device")
        print(f"Model   : {regs[0]}")
        print(f"SN      : {regs[2]}")
        print(f"Firmware: {regs[3]/100}")
        print(f"Input   : {regs[14]/100}V")
        print(f"Temp    : {regs[5]}°C")
        print("== Output")
        print(f"Voltage : {regs[10]/100}V")
        print(f"Current : {regs[11]/1000}A")
        print(f"Power   : {regs[13]/100}W")
        print("== Settings")
        print(f"Voltage : {regs[8]/100}V")
        print(f"Current : {regs[9]/1000}A")
        print("== Protection")
        print(f"Voltage : {regs[82]/100}V")
        print(f"Current : {regs[83]/1000}A")

    @property
    def input_voltage(self):
        return self._read_register(14)/100

    @property
    def voltage(self):
        return self._read_register(8)/100
    @voltage.setter
    def voltage(self, value):
        self._write_register(8, int(value*100))

    @property
    def current(self):
        return self._read_register(9)/1000
    @current.setter
    def current(self, value):
        self._write_register(9, int(value*1000))

    @property
    def voltage_protection(self):
        return self._read_register(82)/100
    @voltage_protection.setter
    def voltage_protection(self, value):
        self._write_register(82, int(value*100))

    @property
    def current_protection(self):
        return self._read_register(83)/1000
    @current_protection.setter
    def current_protection(self, value):
        self._write_register(83, int(value*1000))

    @property
    def enable(self):
        return self._read_register(18)
    @enable.setter
    def enable(self, value):
        self._write_register(18, int(value))

    @property
    def backlight(self):
        return self._read_register(72)
    @backlight.setter
    def backlight(self, value):
        self._write_register(72, value)
