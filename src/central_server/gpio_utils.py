import time
import RPi.GPIO as GPIO
from json_utils.parse_json import parse_json


def set_gpio(sala: str, nivel: int):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    data_states = parse_json('json_config/config_states.json')
    status = data_states[sala][0]['outputs'][nivel]['status']

    if(sala == 'sala01'):
        data_gpio = parse_json('json_config/config_sala1.json')
    else:
        data_gpio = parse_json('json_config/config_sala02.json')

    pino = data_gpio['outputs'][nivel]['gpio']
    GPIO.setup(pino, GPIO.OUT)

    if(status == 'OFF'):
        GPIO.output(pino, GPIO.LOW)
        print("Pino foi alterado para DESLIGADO")
    else:
        GPIO.output(pino, GPIO.HIGH)
        print("Pino foi alterado para LIGADO")
