import requests
from bs4 import BeautifulSoup
from spotify_manager import SpotifyManager

date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

# Web scrapping top 100 songs of the choosen date
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
url = f"https://www.billboard.com/charts/hot-100/{date_input}"

response = requests.get(url=url, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")
songs_tags = soup.select("li ul li h3")
songs_names_list = [song.getText().strip() for song in songs_tags]

spotify_manager = SpotifyManager()

#Finding song's uris
year = date_input.split("-")[0]
song_uris = []

for song in songs_names_list:
    result = spotify_manager.get_song_id(song, year)
    try:
        song_uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(song_uri)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped!")

# Creating playlist in spotify
playlist_id = spotify_manager.create_playlist(date=date_input)

# Addings songs to the created playlist
spotify_manager.add_songs_to_playlist(playlist_id, song_uris)