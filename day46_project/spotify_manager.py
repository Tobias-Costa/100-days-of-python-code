import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

class SpotifyManager:

    def __init__(self):
        self._client_id = os.environ["SPOTIFY_CLIENT_ID"]
        self._client_secret = os.environ["SPOTIFY_CLIENT_SECRET"]
        self._username = os.environ["SPOTIFY_USERNAME"]
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-private",
                redirect_uri="https://example.com",
                client_id=self._client_id,
                client_secret=self._client_secret,
                show_dialog=True,
                cache_path="token.txt",
                username=self._username, 
            )
        )
        self._user_id = self.sp.current_user()["id"]

    def create_playlist(self, date):
        result = self.sp.user_playlist_create(user=self._user_id, name=f"{date} Billboard 100", public=False)
        return result["id"]

    def get_song_id(self, song, year):
        result = self.sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
        return result
        
    def add_songs_to_playlist(self, playlist_id, songs_uris):
        self.sp.playlist_add_items(playlist_id, songs_uris)
        print("Songs added!")