# RIDEN RD6006 Python module

This module allows to control a RD6006 via the USB interface using Python.

As with previous models, the RD6006 uses the Modbus protocol over serial, the
registers however are different than the DPS models. The registers are described
in the [registers.md](registers.md) file.

## Features

It allows to control the following options :
 * Output voltage and current
 * Protection voltage and current
 * Backlight
 * Enable status

## Installation
```
$ python setup.py install --user
```

## Usage

```
In [1]: from rd6006 import RD6006
In [2]: r = RD6006('/dev/ttyUSB3')                                                                         
In [3]: r.status()                                                                                                
== Device
Model   : 60062
SN      : 3917
Firmware: 1.26
Input   : 12.28V
Temp    : 26°C
== Output
Voltage : 0.0V
Current : 0.0A
Power   : 0.0W
== Settings
Voltage : 3.33V
Current : 0.2A
== Protection
Voltage : 3.4V
Current : 0.2A

In [8]: r.voltage=1.8                                                                                             
In [10]: r.enable=True                                                                                            
In [11]: r.status()                                                                                               
== Device
Model   : 60062
SN      : 3917
Firmware: 1.26
Input   : 12.28V
Temp    : 26°C
== Output
Voltage : 1.79V
Current : 0.0A
Power   : 0.0W
== Settings
Voltage : 1.8V
Current : 0.2A
== Protection
Voltage : 3.4V
Current : 0.2A
```


## New Methods

Two new methods have been added to the `RD6006` class to set a specific power output:

### set_power

The `set_power` method sets a specific power output by adjusting the current. It takes one argument, `power`, which is the desired power output in watts. It calculates the current needed to get the desired power with the current voltage, and sets the output current to this value.

### set_power_continuous

The `set_power_continuous` method sets a specific power output by adjusting the current, and keeps adjusting it continuously. It takes two arguments, `power` (the desired power output in watts) and `delay` (the delay in seconds between adjustments, default is 1). It continuously calls the `set_power` method with the specified power and delay.

## New Script Behavior

When the script is run directly, it now asks the user to enter the mode (constant current, constant wattage, or constant voltage). Based on the chosen mode, it then asks the user to enter the desired value and sets the corresponding output parameter on the RD6006 device.
