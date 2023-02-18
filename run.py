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
