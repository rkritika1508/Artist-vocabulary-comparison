import urllib.request as ureq
import pandas as pd
import json

data = pd.read_csv('artist_data.csv')

music_api = '18cae4bcb1d5f9b76d8ac7c0e20d1d20'
artists_album_details = {}


def artist_album_link(artist_id):
    api_key = music_api
    url = 'https://api.musixmatch.com/ws/1.1/artist.albums.get?artist_id=' + str(artist_id) + '&page_size=100&page='
    for i in range(1, 10):
        final_url = url + str(i) + '&apikey=' + api_key
        json_obj = ureq.urlopen(final_url)
        data_obj = json.load(json_obj)
        for lst in data_obj['message']['body']['album_list']:
            album_id = lst['album']['album_id']
            artists_album_details[album_id] = {"artist_id": artist_id,
                                               'album_name': lst['album']['album_name'],
                                               'album_release_date': lst['album']['album_release_date'],
                                               'album_release_type': lst['album']['album_release_type'],
                                               'album_genre': lst['album']['primary_genres']['music_genre_list']}
        print(artists_album_details)


for id_art in data['artist_id']:
    artist_album_link(id_art)


album_df = pd.DataFrame.from_dict(artists_album_details, orient='index')
album_df.to_csv('album_data.csv')
print(album_df)