from json_utils.parse_json import parse_json


def status_sala_01():
    data = parse_json('json_config/config_states.json')

    print('\n************ Informações da sala 01 ************ \n')
    i = 0
    while(i < 4):
        print(data['sala01'][0]['outputs'][i]['type'] +
              ': ' + data['sala01'][0]['outputs'][i]['status'])
        i += 1
    i = 0
    while(i < 5):
        print(data['sala01'][0]['inputs'][i]['type'] + ': ' +
              str(data['sala01'][0]['inputs'][i]['status']))
        i += 1

    i = 0
    while(i < 2):
        print(data['sala01'][0]['sensor_temperatura_umidade'][i]['type'] + ': ' +
              str(data['sala01'][0]['sensor_temperatura_umidade'][i]['status']))
        i += 1
    print('\n*************************************************\n')


def status_sala_02():
    data = parse_json('json_config/config_states.json')
    print('\n************ Informações da sala 02 ************ \n')
    i = 0
    while(i < 4):
        print(data['sala02'][0]['outputs'][i]['type'] +
              ': ' + data['sala02'][0]['outputs'][i]['status'])
        i += 1
    i = 0
    while(i < 5):
        print(data['sala02'][0]['inputs'][i]['type'] + ': ' +
              str(data['sala02'][0]['inputs'][i]['status']))
        i += 1
    i = 0
    while(i < 2):
        print(data['sala02'][0]['sensor_temperatura_umidade'][i]['type'] + ': ' +
              str(data['sala02'][0]['sensor_temperatura_umidade'][i]['status']))
        i += 1
    print('\n************************************************* \n')
