from mock import patch, MagicMock
from app.setlist.connect import ConnectAndSearchArtistSetlist

BASE_URL = "base_url"
API_KEY = "12345key"


@patch("app.setlist.connect.requests")
def test_connect_to_api(mock_requests: MagicMock):

    # Setting up values
    artist = "musician"
    connect_and_search_artist_setlist = ConnectAndSearchArtistSetlist(
        BASE_URL, API_KEY
    )

    # Mocking responses
    expected_result = "return_value"

    class MockResponse:
        def json(self):
            return expected_result

    mock_requests.get.return_value = MockResponse()

    # Execute function
    result = connect_and_search_artist_setlist.connect_to_api(artist)

    # Assert expected results
    ## We are getting the expected response
    assert result == expected_result 
    ## We are calling the get method correctly
    mock_requests.get.assert_called_once_with(
        BASE_URL,
        params={"artistName": artist},
        headers={"Accept": "application/json", "x-api-key": API_KEY}
    )
