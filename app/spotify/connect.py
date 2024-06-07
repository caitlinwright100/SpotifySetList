
from spotipy import Spotify
from spotipy.oauth2 import SpotifyOAuth


class SpotifyAuth:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.auth = SpotifyOAuth(
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=f"{redirect_uri}/callback",
            scope="playlist-modify-private",
            show_dialog=True,
        )
        

    def connect_to_spotify(self) -> Spotify:
        return Spotify(auth_manager=self.auth)

    def get_authorize_url(self, code=None):
        """
        Get the Spotify authorization URL.
        """
        if code:
            # If code is provided, include it in the URL
            return self.auth.get_authorize_url(code)
        else:
            # If code is not provided, generate URL without it
            return self.auth.get_authorize_url()

    def get_authorize_token(self, code):
        token_info = self.auth.get_access_token(code)
        return token_info

    def get_spotify_client(self, token_info):
        access_token = token_info["access_token"]
        return Spotify(auth=access_token)


