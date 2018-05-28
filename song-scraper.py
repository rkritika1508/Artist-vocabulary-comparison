import urllib.request as ureq
from bs4 import BeautifulSoup as soup
import pandas as pd

data = pd.read_csv('music-data.csv')
my_url = data['Links'][0]
uclient = ureq.urlopen(my_url)
page_html = uclient.read()
uclient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("a", {"target":"_blank"})
for container in containers:
    print(container.get('href'))
