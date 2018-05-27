import urllib.request as ureq
from bs4 import BeautifulSoup as soup
import re

my_url = "https://www.imdb.com/list/ls051517906/"

uclient = ureq.urlopen(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup (page_html, "html.parser")
containers = page_soup.findAll("h3", {"class":"lister-item-header"})
artists = []
artists_links = []
num = 0
for container in containers:
    container = container.a.text.replace("\n", "")[1:]
    artists.append(container)
    num = num+1
artists[11] = "Beach Boys"
artists[39] = "Simon Garfunkel"
artists[47] = "Run DMC"
artists[53] = "Howlin Wolf"
artists[96] = "R E M"
#Bo Diddley doesn't have any song in the AZ lyrics collection.
#So, he will have to be removed from the artists list.
artists.remove('Bo Diddley')

#Booker T and the MGs were an instrumental group.
#So, they must b removed too.
artists.remove("Booker T. & the M.G.s")

regex = re.compile('[^a-zA-Z0-9]')
    
for artist in artists:
    artist_search = artist.replace(" ", "+")
    lyrics_url = "https://search.azlyrics.com/search.php?q=" + artist_search
    x = ureq.urlopen(lyrics_url)
    x_html = x.read()
    x.close()
    x_soup = soup(x_html, "html.parser")
    cts = x_soup.td.a["href"]
    #artists_links.append(cts)
    print(cts, artist)

