import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(37, GPIO.OUT)
try: 
    while True:
        input_state = GPIO.input(11)
        if input_state == False:
            print('Button Pressed')
            GPIO.output(37, True)
        else:
            GPIO.output(37, False)
except KeyboardInterrupt:
    GPIO.cleanup()
