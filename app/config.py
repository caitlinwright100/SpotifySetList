import os
from app.spotify.connect import SpotifyAuth
from app.setlist.connect import ConnectAndSearchArtistSetlist


SETLIST_BASE_URL = "SETLIST_BASE_URL"
SETLIST_API_KEY = "SETLIST_API_KEY"

SPOTIFY_USER = "SPOTIFY_USER"
SPOTIFY_CLIENT_ID = "SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "SPOTIFY_CLIENT_SECRET"

env_vars = [
    SETLIST_BASE_URL,
    SETLIST_API_KEY,
    SPOTIFY_USER,
    SPOTIFY_CLIENT_ID,
    SPOTIFY_CLIENT_SECRET,
]


class ConfigEnv:

    def __init__(self):
        self.check_env_vars()

    def api_base_url(self):
        return os.environ[SETLIST_BASE_URL]

    def api_key(self):
        return os.environ[SETLIST_API_KEY]

    def spotify_user(self):
        return os.environ[SPOTIFY_USER]

    def spotify_client_id(self):
        return os.environ[SPOTIFY_CLIENT_ID]

    def spotify_client_secret(self):
        return os.environ[SPOTIFY_CLIENT_SECRET]

    def check_env_vars(self):
        for var in env_vars:
            os.environ[var]

    def spotify_auth(self):
        return SpotifyAuth(
            self.spotify_client_id(),
            self.spotify_client_secret()
        )
    
    def setlist_connector(self) -> ConnectAndSearchArtistSetlist:
        return ConnectAndSearchArtistSetlist(
            self.api_base_url(),
            self.api_key()
        )
