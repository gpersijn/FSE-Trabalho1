from json_utils.functions import save_json, open_json


def config_json(data_config: dict, json_file: str):
    dir = 'src/json/' + json_file + '.json'
    data = open_json(dir)

    data['ip_servidor_central'] = data_config['ip_servidor_central']
    data['porta_servidor_central'] = data_config['porta_servidor_central']

    if (data_config['nome'] == 'Sala 01'):
        data['ip_sala_01'] = data_config['ip_servidor_distribuido']
        data['porta_sala_01'] = data_config['porta_servidor_distribuido']

        count = 0
        while(count < 5):
            data['sala01'][0]['outputs'][count]['gpio'] = data_config['outputs'][count]['gpio']
            count += 1

        count = 0
        while(count < 6):
            data['sala01'][0]['inputs'][count]['gpio'] = data_config['inputs'][count]['gpio']
            count += 1

        data['sala01'][0]['sensor_temperatura_umidade'][0]['gpio'] = data_config['sensor_temperatura'][0]['gpio']
        data['sala01'][0]['sensor_temperatura_umidade'][1]['gpio'] = data_config['sensor_temperatura'][0]['gpio']

    if (data_config['nome'] == 'Sala 02'):
        print('Estou na sala 02')
        data['ip_sala_02'] = data_config['ip_servidor_distribuido']
        data['porta_sala_02'] = data_config['porta_servidor_distribuido']

        count = 0
        while(count < 5):
            data['sala02'][0]['outputs'][count]['gpio'] = data_config['outputs'][count]['gpio']
            count += 1

        count = 0
        while(count < 6):
            data['sala02'][0]['inputs'][count]['gpio'] = data_config['inputs'][count]['gpio']
            count += 1

        data['sala02'][0]['sensor_temperatura_umidade'][0]['gpio'] = data_config['sensor_temperatura'][0]['gpio']
        data['sala02'][0]['sensor_temperatura_umidade'][1]['gpio'] = data_config['sensor_temperatura'][0]['gpio']

    save_json(dir, data)
