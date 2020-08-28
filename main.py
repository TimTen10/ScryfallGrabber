import requests


def scryfall_search(search_term):
    resp = requests.get('https://api.scryfall.com/cards/search', params={'q': search_term})
    if resp.status_code == 200:
        res = resp.json()
        return res
    else:
        print(f'Something went wrong when trying to communicate with the API: {resp.status_code}')
        print(resp.url)


def cardsearch():
    # The search terminology is the same as on Scryfall! See: https://scryfall.com/docs/syntax
    print('Input your search.')
    search_term = input()
    res = scryfall_search(search_term)
    for card in res['data']:
        print(card)


if __name__ == '__main__':
    cardsearch()
