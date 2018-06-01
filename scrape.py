import urllib.request as ureq
from bs4 import BeautifulSoup as soup
import lyricsgenius as genius

my_url = "https://en.wikipedia.org/wiki/List_of_best-selling_music_artists"

uclient = ureq.urlopen(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup (page_html, "html.parser")
containers = page_soup.findAll("th", {"scope":"row"})
artists = []

for i in range(len(containers)-17):
    artists.append(containers[i].a.text)


artists.remove("B'z")
artists.remove("Ayumi Hamasaki")
artists.remove("Julio Iglesias")
artists.remove("Johnny Hallyday")
artists[38] = "Beyonce"
artists[67] = "Beach Boys"
artists[89] = "Black Eyed Peas"
artists[96] = "2pac"

client_access_token = 'dF8LN5u4DZhEd6S1W-IxQ8HIYnBNdP054JcEKl5NVVAFyFFJhYRtiGB3n'
api = genius.Genius(client_access_token)


def artist_search(name):
    artist = api.search_artist(name, max_songs=2000)
    artist.save_lyrics()


artist_search(artists[2])