import urllib.request as ureq
from bs4 import BeautifulSoup as soup
import pandas as pd

my_url = "https://en.wikipedia.org/wiki/List_of_best-selling_music_artists"

uclient = ureq.urlopen(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup (page_html, "html.parser")
containers = page_soup.findAll("th",{"scope":"row"})
artists = []
artists_links = []
num=0

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

for artist in artists:
    artist_search = artist.replace(" ", "+")
    lyrics_url = "https://search.azlyrics.com/search.php?q=" + artist_search
    x = ureq.urlopen(lyrics_url)
    x_html = x.read()
    x.close()
    x_soup = soup(x_html, "html.parser")
    link = x_soup.td.a["href"]
    artists_links.append(link)
print(artists_links)

d = {'Artists':artists, 'Links':artists_links}
df = pd.DataFrame(data=d)
df.to_csv("music-data.csv")
