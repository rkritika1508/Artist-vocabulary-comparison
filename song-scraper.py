import urllib.request as ureq
import pandas as pd
import json

data = pd.read_csv('artist_data.csv')

music_api = '18cae4bcb1d5f9b76d8ac7c0e20d1d20'
artists_album_details = []


def artist_album_link(artist_id):
    api_key = music_api
    url = 'https://api.musixmatch.com/ws/1.1/artist.albums.get?artist_id=' + str(artist_id) + '&page_size=100&page='
    for i in range(1,15):
        final_url = url + str(i) + '&apikey=' + api_key
        json_obj = ureq.urlopen(final_url)
        data_obj = json.load(json_obj)
        for lst in data_obj['message']['body']['album_list']:
            artists_album_details.append([artist_id, lst['album']['album_id'], lst['album']['album_name'],
                                          lst['album']['album_release_date'], lst['album']['album_release_type'],
                                          lst['album']['primary_genres']['music_genre_list']])
        print(artists_album_details)


# for id in data['artist_id']:
#    artist_album_link(id)


artist_album_link(158)

album_df = pd.DataFrame(artists_album_details, columns=['artist_id', 'album_id', 'album_name',
                                                        'album_release_date', 'album_release_type', 'album_genres'])
# album_df.to_csv('album_data.csv')
print(album_df)