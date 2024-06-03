import requests


class ConnectAndSearchArtistSetlist:

    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def connect_to_api(self, artist_name):
        headers = {"Accept": "application/json", "x-api-key": self.api_key}
        query_params = {"artistName": artist_name}

        response = requests.get(
            self.base_url,
            params=query_params,
            headers=headers
        )

        return response.json()
