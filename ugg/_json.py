'''Module for parsing json'''
import json
from functools import lru_cache


@lru_cache()
def get_json(label):
    '''Returns json data from assets folder'''
    with open(f'assets/json/{label}.json') as file_pointer:
        return json.load(file_pointer)
