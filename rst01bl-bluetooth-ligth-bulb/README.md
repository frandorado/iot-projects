# RST01BL E27 7W RGB Bluetooth Ligth Bulb

Script in python for the control with bluetooth of RST01BL bulb and integration with home assistant and Raspberry Pi.

## Table of contents
1. [Description](#section1)
2. [How to use](#section2)
3. [Home assistant integration](#section3)
4. [References](#section4)

## <a name="section1"></a> 1. Description

This project provides to be a guide for the control of the bluetooth bulb and its integration with Home Assistant (https://home-assistant.io/). We need follow the next steps before use the bluetooth bulb.

* Identify the bulb address (XX:XX:XX:XX:XX:XX). You can use NRF Connect o similar.
* Install the pexpect library, 'sudo pip install pexpect'.
* Install gatttool

## <a name="section2"></a> 2. How to use

### 2.1. Turn On

From python script:

```
> sudo python start-light.py XX:XX:XX:XX:XX:XX
```

From console:

```
> gatttool -I
> connect XX:XX:XX:XX:XX:XX
> char-write-cmd 0x0043 CC2333
> quit
```

### 2.2. Turn Off

```
> sudo python stop-light.py XX:XX:XX:XX:XX:XX
```

From console:

```
> gatttool -I
> connect XX:XX:XX:XX:XX:XX
> char-write-cmd 0x0043 CC2433
> quit
```

### 2.3. RGB Color

We'll use 14 hex digits to change the color following the next pattern:

```
56 XX XX XX 00 YY AA
```

* The `XX XX XX` indicates the values of R(Red) G(Green) B(Blue) in HEX. So if we want a red color we should indicate the value `FF0000`

* The `YY` indicates if we want color (F0) or white ligth (0F). If we choose the white ligth value (F0) the `XX XX XX` value will be ignored. 

### 2.4. Examples

* Turn on
```
char_write_cmd 0x0043 CC2333
```

* Turn off
```
char_write_cmd 0x0043 CC2433
```

* White light
```
char_write_cmd 0x0043 56FFFFFF000FAA
```

* Blue light
```
char_write_cmd 0x0043 560000FF00F0AA
```

## <a name="section3"></a> 3. Home assistant integration

```
switch:
  - platform: command_line
    switches:
	   bluetooth_bulb:
	     oncmd: "sudo python ~/.homeassistant/start-light.py XX:XX:XX:XX:XX:XX"
	     offcmd: "sudo python ~/.homeassistant/stop-light.py XX:XX:XX:XX:XX:XX"   
```

## <a name="section4"></a> 4. References
[1] Link to buy <http://www.dx.com/p/rst01bl-e27-7w-wireless-bluetooth-4-0-music-smart-28-led-light-bulb-rgb-400lm-3000k-ac-85-265v-391147>







