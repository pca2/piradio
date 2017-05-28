# From https://www.youtube.com/watch?v=Bqk6M_XdIC0&t=150s
# lights up when button pressed
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(37, GPIO.OUT)
GPIO.output(37,0)
try: 
    while True:
        GPIO.output(37,GPIO.input(11) )
except KeyboardInterrupt:
    GPIO.cleanup()
