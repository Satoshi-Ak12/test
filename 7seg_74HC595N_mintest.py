import RPi.GPIO as GPIO
import time

SEG_PIN = 21  # aセグメントを直結

GPIO.setmode(GPIO.BCM)
GPIO.setup(SEG_PIN, GPIO.OUT, initial=GPIO.LOW)

try:
    while True:
        # 点灯
        GPIO.output(SEG_PIN, GPIO.LOW)
        print("ON")
        time.sleep(2)

        # 消灯
        GPIO.output(SEG_PIN, GPIO.HIGH)
        print("OFF")
        time.sleep(2)

finally:
    GPIO.cleanup()
