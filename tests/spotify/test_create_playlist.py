import pytest
from unittest.mock import MagicMock
from spotipy import Spotify
from app.spotify.create_playlist import SpotifyPlaylistManager


@pytest.fixture
def mock_spotify():
    return MagicMock(Spotify)

@pytest.fixture
def playlist_manager(mock_spotify):
    return SpotifyPlaylistManager(mock_spotify, "dummy_user_id")



def test_create_empty_playlist(playlist_manager, mock_spotify):

    # Arrange

    mock_spotify.user_playlist_create.return_value = {"id": "dummy_playlist_id"}

    # Act

    playlist_id = playlist_manager.create_empty_playlist(
        artist= "Test Artist",
        user= "dummy_user")
    
    # Assert

    assert playlist_id == "dummy_playlist_id"

    mock_spotify.user_playlist_create.assert_called_once_with(
        user = "dummy_user",
        name = "Test Artist Setlist",
        public = False,
        description = "Most Recent Setlist for Test Artist"
    )


def test_add_songs_to_playlist(playlist_manager, mock_spotify):
    # Arrange
    mock_spotify.search.return_value = {
        "tracks": {
            "items": [{"uri": "dummy_track_uri"}]
        }
    }

    # Act
    playlist_manager.add_songs_to_playlist(
        playlist_id="dummy_playlist_id",
        spotify_setlist=["Test Song 1", "Test Song 2"],
        artist="Test Artist"
    )

    # Assert
    mock_spotify.search.assert_any_call(
        q='track:Test Song 1 artist:"Test Artist"', type="track", limit=1
    )
    mock_spotify.search.assert_any_call(
        q='track:Test Song 2 artist:"Test Artist"', type="track", limit=1
    )
    mock_spotify.playlist_add_items.assert_called_with(
        playlist_id="dummy_playlist_id", items=["dummy_track_uri"]
    )

def test_add_songs_to_playlist_no_tracks_found(playlist_manager, mock_spotify):

    # Arrange

    mock_spotify.search.return_value = {"tracks": {"items": []}}

    # Act

    playlist_manager.add_songs_to_playlist(
        playlist_id = "dummy_playlist_id",
        spotify_setlist = ["Test Song"],
        artist = "Test Artist"
    )

    # Assert

    mock_spotify.search.assert_called_once_with(
        q='track:Test Song artist:"Test Artist"', type="track", limit=1
    )
    mock_spotify.playlist_add_items.assert_not_called()