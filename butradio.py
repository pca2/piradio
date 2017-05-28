import RPi.GPIO as GPIO
import time
import subprocess
GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(17)
    if input_state == False:
      player = subprocess.Popen(["mpg123","-m" ,"http://wbur-sc.streamguys.com/wbur.mp3"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

