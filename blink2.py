import RPi.GPIO as GPIO
import time

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)

# set up GPIO output channel
GPIO.setup(37, GPIO.OUT)
def count(n):
  for _ in range(n):
    GPIO.output(37,1)
    time.sleep(.5)
    GPIO.output(37,0)
    time.sleep(.5)



