import sys
import os
import signal
from central_server.socket_utils import initSocket
import threading
from central_server.menu import menu
from log_config.log import log


if __name__ == "__main__":

    # print('Informe o ip desejado para o Servidor:')
    # ip = input()
    ip = "164.41.98.28"
    # print('Informe a porta desejada para o Servidor:')
    # port = input()
    port = "10843"

    servidorThread = threading.Thread(
        target=initSocket, args=(ip, int(port)))
    servidorThread.start()
    interfaceThread = threading.Thread(target=menu)
    interfaceThread.start()
    interfaceThread.join()
