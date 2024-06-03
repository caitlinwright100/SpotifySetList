from app.spotify.create_playlist import SpotifyPlaylistManager


def generate_playlist(spotify_connection, user, artist_name, spotify_setlist):

    playlist_manager = SpotifyPlaylistManager(spotify_connection, user)
    playlist_id = playlist_manager.create_empty_playlist(artist_name, user)
    playlist_manager.add_songs_to_playlist(
        playlist_id, spotify_setlist, artist_name
    )
    playlist_url = f"https://open.spotify.com/playlist/{playlist_id}"
    return playlist_url
