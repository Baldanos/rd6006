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
