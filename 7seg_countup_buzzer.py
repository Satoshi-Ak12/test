import RPi._GPIO as GPIO
import time

# a,b,c,d,e,f,g,dp　の順でピンを割当(BCM番号)
PINS = [17,27,22,5,6,23,24,25]
Buzzer_PIN = 21

ON = GPIO.LOW
OFF = GPIO.HIGH

DIGIT_MAP = {
    '0': [True, True, True, True, True, True, False, False],
    '1': [False, True, True, False, False, False, False, False],
    '2': [True, True, False, True, True, False, True, False],
    '3': [True, True, True, True, False, False, True, False],
    '4': [False, True, True, False, False, True, True, False],
    '5': [True, False, True, True, False, True, True, False],
    '6': [True, False, True, True, True, True, True, False],
    '7': [True, True, True, False, False, False, False, False],
    '8': [True, True, True, True, True, True, True, False],
    '9': [True, True, True, True, False, True, True, False],
    'A': [True, True, True, False, True, True, True, False],
    'b': [False, False, True, True, True, True, True, False],
    'C': [True, False, False, True, True, True, False, False],
    'd': [False, True, True, True, True, False, True, False],
    'E': [True, False, False, True, True, True, True, False],
    'F': [True, False, False, False, True, True, True, False],
    'H': [False, True, True, False, True, True, True, False],
    'L': [False, False, False, True, True, True, False, False],
    'n': [False, False, True, False, True, False, True, False],
    'o': [False, False, True, True, True, False, True, False],
    'P': [True, True, False, False, True, True, True, False],
    'U': [False, True, True, True, True, True, False, False],
    '-': [False, False, False, False, False, False, True, False],
    ' ': [False, False, False, False, False, False, False, False],
}

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in PINS:
        GPIO.setup(pin,GPIO.OUT,initial=OFF)
    GPIO.setup(16,GPIO.IN,pull_up_down=GPIO.PUD_UP)
    GPIO.setup(Buzzer_PIN,GPIO.OUT)

def show_pattern(bits8):
    #True=点灯/False=消灯
    for pin, seg_on in zip(PINS,bits8):
        GPIO.output(pin,ON if seg_on else OFF)


def show_char(ch, dp=False):
    #表示パターンを探す。なければ空白にする
    if ch in DIGIT_MAP:
        base_pattern = DIGIT_MAP[ch]
    else:
        base_pattern = DIGIT_MAP[' ']
    pat = base_pattern.copy()   #元データを壊さないようにコピー
    #小数点の制御
    pat[7] = dp
    show_pattern(pat)

def Buzzer_beat():
    pwm = GPIO.PWM(Buzzer_PIN,3000)
    pwm.start(50)
    return pwm

def main():
    try:
        setup()
        sw = 0
        show_char('0')
        while True:
            if GPIO.input(16) == GPIO.LOW:
                sw += 1
                if sw == 10:
                    sw = 0
                    p = Buzzer_beat()
                    time.sleep(1.5)
                    p.stop()
                time.sleep(0.5)
            show_char(str(sw))

    except KeyboardInterrupt:
        print("終了します")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()