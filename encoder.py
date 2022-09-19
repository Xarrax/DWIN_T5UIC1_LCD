# Class to monitor a rotary encoder and update a value.  You can either read the value when you need it, by calling getValue(), or
# you can configure a callback which will be called whenever the value changes.

<<<<<<< HEAD
import OPi.GPIO as GPIO
=======
#import RPi.GPIO as GPIO	#mkocot
from gpiozero import RotaryEncoder	#mkocot
>>>>>>> b5055af842392453051d0e676bf273954ab09e28

class Encoder:

	def __init__(self, leftPin, rightPin, callback=None):
		#self.leftPin = leftPin	#mkocot
		#self.rightPin = rightPin	#mkocot
		# NOTE: left, right is different from GPIO, to keep it "legacy"	#mkocot
		# swap values	#mkocot
		self.rotor = RotaryEncoder(rightPin, leftPin)	#mkocot
		self.rotor.when_rotated_clockwise = self.rotated_right	#mkocot
		self.rotor.when_rotated_counter_clockwise = self.rotated_left	#mkocot
		self.value = 0
		#self.state = '00'	#mkocot
		#self.direction = None	#mkocot
		self.callback = callback
		
		# GPIO.setup(self.leftPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#mkocot
		# GPIO.setup(self.rightPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)	#mkocot
		# GPIO.add_event_detect(self.leftPin, GPIO.BOTH, callback=self.transitionOccurred)  	#mkocot
		# GPIO.add_event_detect(self.rightPin, GPIO.BOTH, callback=self.transitionOccurred)  	#mkocot

	def rotated_left(self):	#mkocot
		self.value = self.value - 1
		if self.callback is not None:
			self.callback(self.value)
	def rotated_right(self):	#mkocot
		self.value = self.value + 1
		if self.callback is not None:
			self.callback(self.value)
			
	# def transitionOccurred(self, channel):
	#     p1 = GPIO.input(self.leftPin)
	#     p2 = GPIO.input(self.rightPin)
	#     newState = "{}{}".format(p1, p2)

	#     if self.state == "00": # Resting position
	#         if newState == "01": # Turned right 1
	#             self.direction = "R"
	#         elif newState == "10": # Turned left 1
	#             self.direction = "L"

	#     elif self.state == "01": # R1 or L3 position
	#         if newState == "11": # Turned right 1
	#             self.direction = "R"
	#         elif newState == "00": # Turned left 1
	#             if self.direction == "L":
	#                 self.value = self.value - 1
	#                 if self.callback is not None:
	#                     self.callback(self.value)

	#     elif self.state == "10": # R3 or L1
	#         if newState == "11": # Turned left 1
	#             self.direction = "L"
	#         elif newState == "00": # Turned right 1
	#             if self.direction == "R":
	#                 self.value = self.value + 1
	#                 if self.callback is not None:
	#                     self.callback(self.value)

	#     else: # self.state == "11"
	#         if newState == "01": # Turned left 1
	#             self.direction = "L"
	#         elif newState == "10": # Turned right 1
	#             self.direction = "R"
	#         elif newState == "00": # Skipped an intermediate 01 or 10 state, but if we know direction then a turn is complete
	#             if self.direction == "L":
	#                 self.value = self.value - 1
	#                 if self.callback is not None:
	#                     self.callback(self.value)
	#             elif self.direction == "R":
	#                 self.value = self.value + 1
	#                 if self.callback is not None:
	#                     self.callback(self.value)
				
	#     self.state = newState

	def getValue(self):
		return self.value
