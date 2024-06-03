from spotipy import Spotify


class SpotifyPlaylistManager:
    def __init__(self, spotify_connection: Spotify, user_id):
        self.spotify_connection = spotify_connection
        self.user_id = user_id

    def create_empty_playlist(self, artist, user, public=False):

        playlist_name = f"{artist} Setlist"
        playlist_description = f"Most Recent Setlist for {artist}"

        playlist = self.spotify_connection.user_playlist_create(
            user=user,
            name=playlist_name,
            public=public,
            description=playlist_description,
        )

        playlist_id = playlist["id"]

        return playlist_id

    def add_songs_to_playlist(self, playlist_id, spotify_setlist, artist):
       
        for song in spotify_setlist:
            track_uri = self.spotify_connection.search(
                q=f'track:{song} artist:"{artist}"', type="track", limit=1
            )
            # Check if the track is found, go to next if not
            if not track_uri:
                
                continue
            else:

                try:
                    track = track_uri["tracks"]["items"][0]["uri"]
                    self.spotify_connection.playlist_add_items(
                        playlist_id=playlist_id, items=[track]
                    )
                except IndexError:
                    pass
