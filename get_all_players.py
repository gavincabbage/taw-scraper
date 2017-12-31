from bs4 import BeautifulSoup
from requests import get

TAW_BASE_URL = 'http://taw-server.de/'
TAW_STATS_BASE_URL = 'http://taw-server.de/stats.php?page='


def get_player_links_for_page(number):
    response = get(TAW_STATS_BASE_URL + str(number))
    parsed = BeautifulSoup(response.text, 'html.parser')
    return [tag['href'] for tag in parsed.find_all('a') if 'pilot' in tag['href']]


def write_player_links_to_file(links, filename):
    with open(filename, 'w') as f:
        for link in links:
            f.write(TAW_BASE_URL + link + '\n')


def get_all_player_links():
    links, page_number = [], 1
    current_player_links = get_player_links_for_page(0)
    while len(current_player_links) > 0:
        links += current_player_links
        current_player_links = get_player_links_for_page(page_number)
        page_number += 1
    return links


all_player_links = get_all_player_links()
write_player_links_to_file(all_player_links, 'player_links.txt')
print('Wrote {} links to file'.format(len(all_player_links)))
