# ugg-parser

## Usage

To parse Kennen's data for aram

```
from pprint import pprint

from ugg import get_champions_mapping
from ugg import get_patch
from ugg import get_ugg_overview
from ugg import get_ugg_patch
from ugg import humanize_ugg_overview

patch = get_patch(index=1)
mapping = get_champions_mapping(patch)
overview = get_ugg_overview({
    'patch': get_ugg_patch(patch),
    'champion_id': mapping['Kennen'],
    'queue': 'normal_aram',
    'region': 'world',
    'rank': 'overall',
    'role': 'none',
})
overview = humanize_ugg_overview(overview)
pprint(overview)
```

Output

```
{'abilities': {'ability_max_order': ['Q', 'W', 'E'],
               'ability_order': ['Q',
                                 'W',
                                 'E',
                                 'Q',
                                 'Q',
                                 'R',
                                 'Q',
                                 'W',
                                 'Q',
                                 'W',
                                 'R',
                                 'W',
                                 'W',
                                 'E',
                                 'E',
                                 'R',
                                 'E',
                                 'E'],
               'matches': 34502,
               'wins': 16987},
 'core_items': {'core_items': [3152, 3020, 3157],
                'matches': 13213,
                'wins': 6431},
 'item_4_options': [{'item': 3089, 'matches': 12719, 'wins': 6602},
                    {'item': 3151, 'matches': 15034, 'wins': 7440}],
 'item_5_options': [{'item': 3089, 'matches': 5945, 'wins': 2966},
                    {'item': 3116, 'matches': 2313, 'wins': 1200},
                    {'item': 3102, 'matches': 1932, 'wins': 993}],
 'item_6_options': [{'item': 3102, 'matches': 555, 'wins': 310},
                    {'item': 3165, 'matches': 558, 'wins': 297},
                    {'item': 3151, 'matches': 615, 'wins': 313}],
 'low_sample_size_warning': False,
 'matches': 85403,
 'runes': {'matches': 8786,
           'primary_style': 8100,
           'runes': [8112, 8014, 8135, 8138, 8139, 9111],
           'secondary_style': 8000,
           'wins': 4366},
 'shards': {'matches': 27742,
            'shards': ['5008', '5008', '5002'],
            'wins': 13437},
 'starting_items': {'matches': 21941,
                    'starting_items': [1001, 2003, 3145],
                    'wins': 10941},
 'summoner_spells': {'matches': 68192,
                     'summoner_spells': [4, 32],
                     'wins': 32984},
 'wins': 40773}
```
