import urllib.request as ureq
from bs4 import BeautifulSoup as soup
import pandas as pd
import re

my_url = "https://en.wikipedia.org/wiki/List_of_best-selling_music_artists"

uclient = ureq.urlopen(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup (page_html, "html.parser")
containers = page_soup.findAll("th", {"scope":"row"})
artists = []
artist_links = []

for i in range(len(containers)-17):
    name_artist = containers[i].a.text
    name_artist = name_artist.replace("/", " ")
    name_artist = name_artist.replace(".", " ")
    name_artist = name_artist.replace("-", " ")
    artists.append(name_artist)

artists.remove("B'z")
artists.remove("Ayumi Hamasaki")
artists.remove("Julio Iglesias")
artists.remove("Johnny Hallyday")
artists[38] = "Beyonce"
artists[67] = "Beach Boys"
artists[89] = "Black Eyed Peas"
artists[96] = "2pac"


def get_artists_links(name):
    url = 'https://search.azlyrics.com/search.php?q=' + name.lower().replace(" ", "+")
    u_client = ureq.urlopen(url)
    pg_html = u_client.read()
    u_client.close()
    pg_soup = soup(pg_html, "html.parser")
    ctn = pg_soup.find('a', {'target': '_blank'})
    return ctn.get('href')


for artist in artists:
    artist_links.append(get_artists_links(artist))

data = pd.DataFrame(
    {'Name': artists,
     'Links': artist_links
    })
data.to_csv("Data.csv")