'''Main module'''
from pprint import pprint

from ugg import get_champions_mapping
from ugg import get_patch
from ugg import get_ugg_overview
from ugg import get_ugg_patch
from ugg import humanize_ugg_overview


def main():
    '''Main function'''
    patch = get_patch(index=1)
    if patch is None:
        print('Could not parse patch data from ddragon.')
        return
    mapping = get_champions_mapping(patch)
    if mapping is None:
        print('Could not parse champions data from ddragon.')
    overview = get_ugg_overview({
        'patch': get_ugg_patch(patch),
        'champion_id': mapping['Kennen'],
        'queue': 'normal_aram',
        'region': 'world',
        'rank': 'overall',
        'role': 'none',
    })
    if overview is None:
        print('Could not parse overview data from ugg.')
        return
    overview = humanize_ugg_overview(overview)
    pprint(overview)


if __name__ == '__main__':
    main()
