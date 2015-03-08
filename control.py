import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.OUT)
GPIO.output(37,0)
GPIO.output(37,1)
time.sleep(3)
GPIO.cleanup()
