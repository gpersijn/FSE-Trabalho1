from json_utils.functions import open_json, map_json
from log_config.log import log
import threading
from central_server.init import initSocket

if __name__ == "__main__":
    print('1 - Sala 01\n2 - Sala 02\n')
    print('Escolha a sala:')
    sala = input()
    if (sala == 1):
        sala_01 = open_json('json_config/config_sala_1.json')
        print('Sala 01')
        map_json('json_config/config_sala_1.json', 'config_states')
        ip = sala_01['ip_servidor_distribuido']
        port = sala_01['porta_servidor_distribuido']
        d = 'sala01'
    if (sala == 2):
        sala_02 = open_json('json_config/config_sala_2.json')
        print('Sala 02')
        map_json('json_config/config_sala_2.json', 'config_states')
        ip = sala_02['ip_servidor_distribuido']
        port = sala_02['porta_servidor_distribuido']
        d = 'sala02'

    serv_thread = threading.Thread(target=initSocket,
                                   args=(ip,
                                         int(port)))
    serv_thread.start()
