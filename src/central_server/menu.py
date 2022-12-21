import time
import logging
from central_server.status import status_sala_01, status_sala_02
from json_utils.functions import (update_json,
                                  state_change)
from central_server.gpio_utils import set_gpio
from distribuited.temperature import show_temperature
import os


def menu():
    while (True):
        print('\n____________MENU____________\n')
        print('1 - Mostrar estado das sala 01')
        print('2 - Mostrar estado das sala 02')
        print('3 - Ligar Alarme')
        print('4 - Desligar Alarme')
        print('5 - Alterar sala 01')
        print('6 - Alterar sala 02')
        print('7 - Ver temperatura')
        print('__________________________')
        print('Escolha: ')
        response = int(input())
        os.system('clear')

        # OK
        if (response == 1):
            print('Mostrando estado da sala 01...')
            status_sala_01()
            logging.info('Mostrando estados da sala 01...')

        # OK
        if (response == 2):
            print('Mostra estado da sala 02')
            status_sala_02()
            logging.info('Mostrando informações da sala 02')

        elif (response == 3):
            update_json('sala01', 4, 'ON')
            update_json('sala02', 4, 'ON')
            set_gpio('sala01', 4)

            # send_comandos()
            logging.info('Alarme Ligado')

        elif (response == 4):
            update_json('sala01', 4, 'OFF')
            update_json('sala02', 4, 'OFF')
            # send_comandos()
            set_gpio('sala01', 4)
            logging.info('Alarme Desligado')

        elif (response == 5 or response == 6):

            print('___________SALA___________\n')
            print('1 - lampada 01')
            print('2 - lampada 02')
            print('3 - projetor')
            print('4 - ar-condicionado')
            print('5 - todos')
            print('_____________________________')

            print(
                'Escolha qual equipamento deseja ligar/desligar da sala', str(response-4), ':')
            escolha_input = int(input())

            if(response == 5):
                sala = 'sala01'
                logging.info('Equipamento de input na sala 01 foi selecioando')

            elif (response == 6):
                sala = 'sala02'
                logging.info('Equipamento de input na sala 02 foi selecioando')

            state_change(escolha_input, sala)
            # send_comandos()

        elif (response == 7):
            show_temperature(1)

        time.sleep(2)
