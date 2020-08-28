import requests
import json


def _fill_template(card):
    card_template = {}
    values = [
        'name', 'mana_cost', 'cmc', 'type_line', 'oracle_text', 'power', 'toughness',
        'colors', 'color_identity', 'keywords', 'rarity', 'flavor_text'
    ]

    for value in values:
        try:
            card_template[value] = card[value]
        except KeyError:
            card_template[value] = None

    return card_template


def scryfall_search(search_term):
    resp = requests.get('https://api.scryfall.com/cards/search', params={'q': search_term})
    if resp.status_code == 200:
        res = resp.json()
        res_data = {'cards': []}
        for card in res['data']:
            res_data['cards'].append(_fill_template(card))
        return res_data
    else:
        print(f'Something went wrong when trying to communicate with the API: {resp.status_code}')
        print(resp.url)


def save_results(data, filename):
    # We only need:
    # name, mana_cost, cmc, type_line, oracle_text, power, toughness,
    # colors, color_identity, keywords, rarity, flavor_text
    with open(f'dataset/{filename}.json', 'w') as json_file:
        json.dump(data, json_file)


def cardsearch():
    # The search terminology is the same as on Scryfall! See: https://scryfall.com/docs/syntax
    print('Input your search.')
    search_term = input()
    # res is in json format (it's a Python dict - see {'cards': []} for list content see _fill_template(card))
    res = scryfall_search(search_term)
    save_results(res, 'search_test')


if __name__ == '__main__':
    cardsearch()
