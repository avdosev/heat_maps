import json


def read_geojson(filename):
    with open(filename, 'r') as file:
        data = file.read()
        return json.loads(data)
