import urllib.request as ureq
from bs4 import BeautifulSoup as soup
import pandas as pd
import json

music_api = '18cae4bcb1d5f9b76d8ac7c0e20d1d20'
my_url = "https://en.wikipedia.org/wiki/List_of_best-selling_music_artists"

uclient = ureq.urlopen(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup (page_html, "html.parser")
containers = page_soup.findAll("th",{"scope":"row"})
artists = []
artists_details = {}

for i in range(len(containers)-17):
    artists.append(containers[i].a.text)

artists.remove("B'z")
artists.remove("Ayumi Hamasaki")
artists.remove("Julio Iglesias")
artists[52] = "Simon Garfunkel"
artists[38] = "Beyonce"
artists[67] = "Beach Boys"
artists[90] = "Black Eyed Peas"
artists[97] = "Tupac"
artists.remove("Johnny Hallyday")

def artist_link(artist):
    api_key = music_api
    q_artist = artist.lower().replace(" ", "%20")
    url = 'https://api.musixmatch.com/ws/1.1/artist.search?q_artist='
    final_url = url + q_artist + '&apikey=' + api_key
    json_obj = ureq.urlopen(final_url)
    data = json.load(json_obj)
    artists_details[artist] = {'artist_id': data['message']['body']['artist_list'][0]['artist']['artist_id']}

for artist in artists:
    artist_link(artist)

data = pd.DataFrame.from_dict(artists_details, orient='index')
data.to_csv('artist_data.csv')