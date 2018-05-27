import urllib.request as ureq
import wikipedia
from bs4 import BeautifulSoup as soup
import re

my_url = "https://en.wikipedia.org/wiki/List_of_best-selling_music_artists"

uclient = ureq.urlopen(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup (page_html, "html.parser")
#containers = page_soup.findAll("div", {"class":""})
containers = page_soup.findAll("th",{"scope":"row"})
artists = []
artists_links = []

for container in containers:
    artists.append(container.a.text)
    #artists.append(container)
#    num = num+1
print(artists)
    
#for artist in artists:
#    artist_search = artist.replace(" ", "+")
#    lyrics_url = "https://search.azlyrics.com/search.php?q=" + artist_search
#    x = ureq.urlopen(lyrics_url)
#    x_html = x.read()
#    x.close()
#    x_soup = soup(x_html, "html.parser")
#    cts = x_soup.td.a["href"]
    #artists_links.append(cts)
#    print(cts, artist)

