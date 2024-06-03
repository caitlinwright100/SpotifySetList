from unittest.mock import patch, MagicMock
from app.setlist.connect import ConnectAndSearchArtistSetlist
from app.setlist.filter import SetListFilter
from app.setlist.generate import generate_setlist 

@patch("app.setlist.generate.SetListFilter")
def test_generate_setlist(mock_setlist_filter):
    # Set dependencies
    artist_name = "test_123"
    playlist_flag = "flag"
    connector = MagicMock(spec=ConnectAndSearchArtistSetlist)
    setlistfm_data = {"setlist": ['song1']}
    expected_setlist = ['song1']

    connector.connect_to_api.return_value = setlistfm_data

    # Mock the filter instance and its method
    mock_filter_instance = MagicMock(spec=SetListFilter)
    mock_filter_instance.produce_setlist.return_value = expected_setlist
    mock_setlist_filter.return_value = mock_filter_instance

    # Run function
    result_setlist = generate_setlist(connector, artist_name, playlist_flag)

    # Assert expected behaviour
    connector.connect_to_api.assert_called_once_with(artist_name)
    mock_setlist_filter.assert_called_once_with(setlistfm_data)
    mock_filter_instance.produce_setlist.assert_called_once_with(playlist_flag)
    assert result_setlist == expected_setlist


