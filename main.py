import requests


def scryfall_search(cardname):
    resp = requests.get('https://api.scryfall.com/cards/search', params={'q': cardname})
    if resp.status_code == 200:
        card = resp.json()
        print(f'Name: {card["name"]}, Coloridentity: {card["color_identity"]}, Cmc: {card["cmc"]}, '
              f'Oracletext: {card["oracle_text"]}')
    else:
        print(f'Something went wrong when trying to communicate with the API: {resp.status_code}')
        print(resp.url)


def cardsearch():
    print('What card are you looking for?')
    cardname = input()
    scryfall_search(cardname)


if __name__ == '__main__':
    cardsearch()
