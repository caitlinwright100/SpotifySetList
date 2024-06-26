import requests
import unittest
from unittest.mock import patch, Mock

from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


class SpotifyAuth:
    def __init__(self, client_id, client_secret):
        self.auth = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri="http://127.0.0.1:9090/callback",
            scope="playlist-modify-private",
            show_dialog=True,
        )

    def connect_to_spotify(self) -> Spotify:
        return Spotify(auth_manager=self.auth)



if __name__ == '__main__':
    unittest.main()


