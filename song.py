import urllib.request as ureq
from bs4 import BeautifulSoup as soup
import pandas as pd

songs_list = []
artists_list = []
df = pd.read_csv('Data.csv')


def get_artists_song_links(url_link):
    u_client = ureq.urlopen(url_link)
    pg_html = u_client.read()
    u_client.close()
    pg_soup = soup(pg_html, "html.parser")
    ctn = pg_soup.findAll('a', {'target': '_blank'})
    for tag in ctn:
        songs_list.append(tag.get('href'))
        artists_list.append(url_link)


for i in range(1, 106):
    get_artists_song_links(df['Links'][i])

data = {'Artist_list': artists_list, 'Songs_list': songs_list}
df = pd.DataFrame(data)
df.to_csv("Final_Song_List.csv")

