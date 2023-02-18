#!/usr/bin/env python3
from dwinlcd import DWIN_LCD

encoder_Pins = (18, 16)
button_Pin = 12
LCD_COM_Port = '/dev/ttyS5'
API_Key = '3c90b2bfe3fc4e4888c585554a9d6b9f'

DWINLCD = DWIN_LCD(
	LCD_COM_Port,
	encoder_Pins,
	button_Pin,
	API_Key
)
