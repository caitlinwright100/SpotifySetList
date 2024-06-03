from unittest.mock import patch, MagicMock
import pytest
from app.spotify.create_playlist import SpotifyPlaylistManager
from app.spotify.generate import generate_playlist

@patch("app.spotify.generate.SpotifyPlaylistManager")
def test_generate_playlist(mock_spotify_playlist_manager):
    # Set Dependencies
    spotify_connection = MagicMock()
    user = "test_user"
    artist_name = "test_artist"
    spotify_setlist = ["song1", "song2", "song3"]

    # Create a mock instance of SpotifyPlaylistManager and configure its methods

    mock_playlist_manager_instance = MagicMock(spec=SpotifyPlaylistManager)
    mock_spotify_playlist_manager.return_value = mock_playlist_manager_instance

    playlist_id = "test_playlist_id"
    mock_playlist_manager_instance.create_empty_playlist.return_value = playlist_id

    # Run function

    result_playlist_url = generate_playlist(spotify_connection, 
                                            user, artist_name, spotify_setlist)


    # Assert expected behaviour

    mock_spotify_playlist_manager.assert_called_once_with(spotify_connection, user)
    mock_playlist_manager_instance.create_empty_playlist.assert_called_once_with(
        artist_name, user)
    mock_playlist_manager_instance.add_songs_to_playlist.assert_called_once_with(
        playlist_id, spotify_setlist, artist_name)

    expected_playlist_url = f"https://open.spotify.com/playlist/{playlist_id}"
    assert result_playlist_url == expected_playlist_url