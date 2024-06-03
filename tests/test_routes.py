import pytest
from fastapi.testclient import TestClient
from app.routes import create_app
from app.config import ConfigEnv

class MockConfigEnv(ConfigEnv):

    def api_base_url(self):
        return "http://mock-api"

    def api_key(self):
        return "mock-api-key"

    def spotify_user(self):
        return "mock-spotify-user"

    def spotify_client_id(self):
        return "mock-spotify-client-id"

    def spotify_client_secret(self):
        return "mock-spotify-client-secret"

    def spotify_auth(self):
        class MockSpotifyAuth:
            def get_authorize_url(self):
                return "http://mock-auth-url"
            
            def get_authorize_token(self, code):
                return {"access_token": "mock-access-token"}
            
            def get_spotify_client(self, token_info):
                return "mock-spotify-client"
            
        return MockSpotifyAuth()

@pytest.fixture
def client():
    config = MockConfigEnv()
    app = create_app(config)
    client = TestClient(app)
    return client

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]

def test_display_setlist(client, mocker):
    mocker.patch("app.routes.generate_setlist", 
                 return_value = ["song1", "song2"])
    response = client.post("/create-playlist", 
                           data = {"artist_name": 
                                   "test_artist", 
                                   "playlist_flag": 
                                   "test_flag"})
    
    
