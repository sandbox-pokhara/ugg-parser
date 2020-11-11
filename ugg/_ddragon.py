'''Module to parse data from ddragon'''
import json

import requests

VERSIONS = 'http://ddragon.leagueoflegends.com/api/versions.json'
CHAMPIONS_URL = 'http://ddragon.leagueoflegends.com/cdn/{patch}/data/en_US/champion.json'


def get_patch(index=0):
    '''Parses patch from ddragon'''
    try:
        response = requests.get(VERSIONS)
        if response.ok:
            return response.json()[index]
        return None
    except (requests.exceptions.RequestException, json.decoder.JSONDecodeError, IndexError):
        return None


def get_champions(patch):
    '''Parses champions from ddragon'''
    try:
        url = CHAMPIONS_URL.format(patch=patch)
        return requests.get(url).json()
    except (requests.exceptions.RequestException, json.decoder.JSONDecodeError):
        return None


def get_champions_mapping(patch):
    '''Parses champions from ddragon'''
    champions = get_champions(patch)
    if champions is None:
        return None
    return {k: int(v['key']) for k, v in champions['data'].items()}
