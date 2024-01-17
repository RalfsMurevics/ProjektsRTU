import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_player_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.find('table', {'id': 'last5'}).find('tbody').find_all('tr')

    player_data = []

    for row in rows:
        dic = {}
        dic['pts'] = row.find_all('td')[23].text
        dic['reb'] = row.find_all('td')[17].text
        dic['ast'] = row.find_all('td')[18].text
        dic['blk'] = row.find_all('td')[20].text
        dic['stl'] = row.find_all('td')[19].text
        dic['3PM'] = row.find_all('td')[9].text
        dic['FG%'] = row.find_all('td')[8].text
        dic['FT%'] = row.find_all('td')[14].text
        player_data.append(dic)

    return pd.DataFrame(player_data)


players = {
    'Shai Gilgeous-Alexander': 'https://www.basketball-reference.com/players/g/gilgesh01.html',
    'Karl-Anthony Towns': 'https://www.basketball-reference.com/players/t/townska01.html',
    'Cam Thomas': 'https://www.basketball-reference.com/players/t/thomaca02.html',
    'Kristaps Porzingis': 'https://www.basketball-reference.com/players/p/porzikr01.html',
    'Coby White': 'https://www.basketball-reference.com/players/w/whiteco01.html',
    'RJ Barrett': 'https://www.basketball-reference.com/players/b/barrerj01.html',
    'Desmond Bane': 'https://www.basketball-reference.com/players/b/banede01.html',
    'Jonas Valančiūnas': 'https://www.basketball-reference.com/players/v/valanjo01.html',
    'Tobias Harris': 'https://www.basketball-reference.com/players/h/harrito02.html',
    'Tyrese Maxey': 'https://www.basketball-reference.com/players/m/maxeyty01.html',
    'Jalen Williams': 'https://www.basketball-reference.com/players/w/willija06.html',
    'Keyonte George': 'https://www.basketball-reference.com/players/g/georgke01.html'
}


with pd.ExcelWriter('FantasyLeaguePlayerStats.xlsx', engine='xlsxwriter') as writer:
    for player, url in players.items():
        player_data = get_player_data(url)
        player_data.to_excel(writer, index=False, sheet_name=player)
