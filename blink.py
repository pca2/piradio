import RPi.GPIO as GPIO
import time
 
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
 
# set up GPIO output channel
GPIO.setup(37, GPIO.OUT)
 
while 1:
  # set RPi board pin 37 high
  GPIO.output(37, True)
  time.sleep(.5)
  GPIO.output(37, False)
  time.sleep(.5)
