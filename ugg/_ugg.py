'''Module to parse data from ugg'''
import json

import requests

from ._json import get_json

UGG_OVERVIEW = 'https://stats2.u.gg/lol/1.1/overview/{patch}/{queue}/{champion_id}/1.4.0.json'
UGG_RANKINGS = 'https://stats2.u.gg/lol/1.1/rankings/{patch}/{queue}/{champion_id}/1.4.0.json'


def get_ugg_patch(patch):
    '''
    Returns patch name in ugg format
    use index 0 for latest patch and index 1 for second latest patch
    '''
    return '_'.join(patch.split('.')[:2])


def get_ugg_overview(config):
    '''
    param config is a dict with following keys:
        patch, champion_id, queue, region, rank, role

    attribute queue:
        "ranked_solo_5x5"
        "normal_aram"
    '''
    try:
        url = UGG_OVERVIEW.format(patch=config['patch'],
                                  queue=config['queue'],
                                  champion_id=config['champion_id'])
        response = requests.get(url)
        region = get_json('regions')[config['region']]
        rank = get_json('ranks')[config['rank']]
        role = get_json('roles')[config['role']]
        if response.ok:
            return response.json()[region][rank][role]
        return None
    except (requests.exceptions.RequestException, json.decoder.JSONDecodeError):
        return None
