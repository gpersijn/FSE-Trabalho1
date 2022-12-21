import json


def parse_json(dir):
    try:
        with open(dir, encoding='utf-8') as file:
            data = json.load(file)
        return data
    except Exception as e:
        print('Erro no parse_json()')
