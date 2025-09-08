import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)  # 周波数50Hz
p.start(0)

def set_angle(angle):
    duty = 3 + (angle / 19)  # 角度→デューティ比変換
    p.ChangeDutyCycle(duty)
    time.sleep(0.5)
    p.ChangeDutyCycle(0)  # サーボが震えないように0に戻す

try:
    while True:
        set_angle(0)
        set_angle(90)
        set_angle(180)
        set_angle(90)
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()
