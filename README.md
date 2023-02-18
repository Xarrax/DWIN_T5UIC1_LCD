# Ender3V2S1_LCD (DWIN_T5UIC1_LCD)

Python class for the Ender 3 V2/S1 LCD runing [Klipper](https://github.com/Klipper3d/klipper) with [Moonraker](https://github.com/arksine/moonraker) for Orange Pi Zero Plus Board using OPi.GPIO

- https://www.klipper3d.org/
- https://octoprint.org/
- https://moonraker.readthedocs.io/

~ Please ensure you got the "DWIN" and not "DACAI" Display Unit in your printer ~

# 1. Setup:

### [Enabling Klipper's API socket](https://www.klipper3d.org/API_Server.html)

Well in this fork of DWIN_T5UIC1_LCD we doesn't need to do much as we will use the Moonraker API unless your "moonraker.sock" has a custom folder path we won't do any big changes.

# 1.1 Library requirements

  Thanks to [wolfstlkr](https://www.reddit.com/r/ender3v2/comments/mdtjvk/octoprint_klipper_v2_lcd/gspae7y)

  ```
  sudo apt-get install python3-pip python3-serial git
  sudo pip3 install requests
  sudo pip3 install OPi.GPIO
  git clone -b opi_zeroplus_lcd https://github.com/Xarrax/Ender3V2S1_LCD.git
  ```

# Note:

* Make sure you enabled UART1 in "armbian-config" if you changed your pinout setup then make sure to also alter to UART2 or 3 and correct the "LCD_COM_Port = '/dev/ttyS1'" variable inside of "run.py"

# 1.1.1 Important

To work with original repo, the RPi.GPIO library was replaced by [OPi.GPIO](https://github.com/rm-hull/OPi.GPIO).

- You should clone OPi.GPIO repo from github and manually install it, or [install via pip](https://opi-gpio.readthedocs.io/en/latest/install.html) as stated in Lib requirements, and then add [zeroplus.py](https://github.com/rm-hull/OPi.GPIO/blob/master/orangepi/zero2.py) module into `install-dir/OPi.GPIO/orangepi`

- Check carefully where the package is installed as then interpreter need to know the directory in its path.

- Also check permissions to call sysfs pin mappings as [non root access](https://opi-gpio.readthedocs.io/en/latest/install.html#non-root-access)

# 1.2 Wire the display

* Display <----> Orange Pi Zero Plus GPIO
* VCC	= PIN 02 | 5V --> RED
* RX	= PIN 08 | PG06 / UART1_TX --> GREEN
* TX	= PIN 10 | PG07 / UART1_RX --> GREEN
* ENT	= PIN 12 | PA07 / PA_EINT7 / SIM_CLK --> GREY
* GND	= PIN 14 | GND --> BLACK
* A	= PIN 16 | PA19 / TWI1_SDA --> YELLOW
* B	= PIN 18 | PA18 / TWI1_SCK --> YELLOW

Here's a diagram based on color selection as stated above:

![Orange-Pi-Zero-Pinout](https://user-images.githubusercontent.com/24323772/219821760-080476f0-08d2-47b2-a7fe-1276afe9f644.png)

### 1.3 Run The Code

Enter the downloaded Ender3V2S1_LCD folder.
Edit the file run.py and edit or copy/paste in the following (pick one)

```
How to obtain the API Key

replace the API_Key = 'your_moonraker_api_key_here' with your Moonraker API Key which you obtain via http://{moonraker-host}/access/api_key
  or
via SSH inside with executing ""~/moonraker/scripts/fetch-apikey.sh"

```

For Ender3 V2/S1
```python
#!/usr/bin/env python3
from dwinlcd import DWIN_LCD

encoder_Pins = (18, 16)
button_Pin = 12
LCD_COM_Port = '/dev/ttyS1'
API_Key = 'your_moonraker_api_key_here'

DWINLCD = DWIN_LCD(
	LCD_COM_Port,
	encoder_Pins,
	button_Pin,
	API_Key
)
```

If your control wheel is reversed use this instead.
```python
#!/usr/bin/env python3
from dwinlcd import DWIN_LCD

encoder_Pins = (16, 18)
button_Pin = 12
LCD_COM_Port = '/dev/ttyS1'
API_Key = 'your_moonraker_api_key_here'

DWINLCD = DWIN_LCD(
	LCD_COM_Port,
	encoder_Pins,
	button_Pin,
	API_Key
)
```
Make sure the LCD is connected to the correct pins before you try executing the script else you will face a bunch of error messages.

```
sudo chmod +x run.py

sudo ./run.py

```

### 1.4 Run at boot:

Note: Delay of 30s after boot to allow webservices to settal. Path of `run.py` is expected to be `/home/pi/DWIN_T5UIC1_LCD/run.py`
Modify service to point where is the run.py path. By default was set to USER env var.

   ```
   sudo chmod +x simpleLCD.service
   sudo mv simpleLCD.service /lib/systemd/system/simpleLCD.service
   sudo chmod 644 /lib/systemd/system/simpleLCD.service
   sudo systemctl daemon-reload
   sudo systemctl enable simpleLCD.service
   sudo reboot
   ```
## 2. Status

### 2.1 Working

 Print Menu:

    * List / Print jobs from OctoPrint / Moonraker
    * Auto swiching from to Print Menu on job start / end.
    * Display Print time, Progress, Temps, and Job name.
    * Pause / Resume / Cancle Job
    * Tune Menu: Print speed & Temps

 Perpare Menu:

    * Move / Jog toolhead
    * Disable stepper
    * Auto Home
    * Z offset (PROBE_CALIBRATE)
    * Preheat
    * cooldown

 Info Menu:

    * Shows printer info.

### 2.2 Not working
    * Save / Loding Preheat setting, hardcode on start can be changed in menu but will not retane on restart.
    * The Control: Motion Menu
