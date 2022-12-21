import sys
import os
import signal
from central_server.init import init
import threading
from central_server.menu import menu
from log_config.log import log
from json_utils.functions import open_json, map_json


if __name__ == "__main__":
    log()

    # print('Informe o ip desejado para o Servidor:')
    # ip = input()
    ip = '164.41.98.28'
    # print('Informe a porta desejada para o Servidor:')
    # port = input()
    port = 10848

    server_01 = open_json('json_config/config_sala1.json')

    map_json('json_config/config_sala1.json', 'send')
    map_json('json_config/config_sala2.json', 'send')

    # ip = server_01['ip_servidor_central']
    # port = server_01['porta_servidor_central']

    servidorThread = threading.Thread(target=init,
                                      args=(ip,
                                            port))

    servidorThread.start()

    # Initialize interface
    interface_thread = threading.Thread(target=menu)
    interface_thread.start()
    interface_thread.join()
