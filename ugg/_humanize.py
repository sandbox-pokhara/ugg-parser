'''Module to parse data from ugg'''


def humanize_ugg_overview(overview):
    '''Humanizes ugg raw data'''
    data = overview[0]
    item_4_options = [{'item': o[0], 'wins': o[1], 'matches': o[2]} for o in data[5][0]]
    item_5_options = [{'item': o[0], 'wins': o[1], 'matches': o[2]} for o in data[5][1]]
    item_6_options = [{'item': o[0], 'wins': o[1], 'matches': o[2]} for o in data[5][2]]
    return {
        'runes': {
            'matches': data[0][0],
            'wins': data[0][1],
            'primary_style': data[0][2],
            'secondary_style': data[0][3],
            'runes': data[0][4],
        },
        'summoner_spells': {
            'matches': data[1][0],
            'wins': data[1][1],
            'summoner_spells': data[1][2],
        },
        'starting_items': {
            'matches': data[2][0],
            'wins': data[2][1],
            'starting_items': data[2][2],
        },
        'core_items': {
            'matches': data[3][0],
            'wins': data[3][1],
            'items': data[3][2],
        },
        'abilities': {
            'matches': data[4][0],
            'wins': data[4][1],
            'ability_order': data[4][2],
            'ability_max_order': list(data[4][3]),
        },
        'item_4_options': item_4_options,
        'item_5_options': item_5_options,
        'item_6_options': item_6_options,
        'wins': data[6][0],
        'matches': data[6][1],
        'low_sample_size_warning': data[7],
        'shards': {'matches': data[8][0], 'wins': data[8][1], 'shards': data[8][2]},
    }
