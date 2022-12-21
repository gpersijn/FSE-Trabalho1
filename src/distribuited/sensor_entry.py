import RPi.GPIO as GPIO
import time
import datetime
import os

GPIO.setmode(GPIO.BCM)
SOUND_PIN = 21
GPIO.setup(SOUND_PIN, GPIO.IN)

count = 0


def DETECTED(SOUND_PIN):
    global count
    count += 1

    return count


try:
    GPIO.add_event_detect(SOUND_PIN, GPIO.RISING, callback=DETECTED)
except KeyboardInterrupt:
    print(" Quit")
    GPIO.cleanup()
