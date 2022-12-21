import RPi.GPIO as GPIO
import logging
from central_server.gpio_utils import set_gpio
from json_utils.parse_json import parse_json
import json


def update_json(sala: str, nivel: int, chave: str):
    data = parse_json('json_config/config_states.json')
    data[sala][0]['outputs'][nivel]['status'] = chave
    save_json('json_config/config_states.json', data)


def get_status(sala: str, nivel: int):
    data = parse_json('json_config/config_states.json')
    return data[sala][0]['outputs'][nivel]['status']


def state_change(escolha_input: int, sala: str):
    if (escolha_input == 1):
        if (get_status(sala, 0) == "ON"):
            update_json(sala, 0, 'OFF')
            logging.info('Lamapada 01 Desligada')
        else:
            update_json(sala, 0, 'ON')
            logging.info('Lamapada 01 Ligada')

    if (escolha_input == 2):
        if (get_status(sala, 1) == 'ON'):
            update_json(sala, 1, 'OFF')
            logging.info('Lamapada 02 Desligada')
        else:
            update_json(sala, 1, 'ON')
            logging.info('Lamapada 02 Ligada')

    if (escolha_input == 3):
        if (get_status(sala, 2) == 'ON'):
            update_json(sala, 2, 'OFF')
            logging.info('Projetor Desligado')
        else:
            update_json(sala, 2, 'ON')
            logging.info('Projetor Ligada')

    if (escolha_input == 4):
        if (get_status(sala, 3) == 'ON'):
            update_json(sala, 3, 'OFF')
            logging.info('Ar-condicionado Desligado')
        else:
            update_json(sala, 3, 'ON')
            logging.info('Ar-condicionado Ligado')
    set_gpio(sala, (escolha_input-1))


def open_json(dir: str):
    with open(dir) as json_file:
        data = json.load(json_file)
    return data


def save_json(dir: str, dictionary: dict):
    try:
        json_object = json.dumps(dictionary, indent=4)
        with open(dir, "w") as outfile:
            outfile.write(json_object)
    except Exception as e:
        print('Erro no save_json')
