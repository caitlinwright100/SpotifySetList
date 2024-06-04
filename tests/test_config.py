import os
import pytest
from unittest.mock import patch
from app.spotify.connect import SpotifyAuth
from app.config import ConfigEnv, SETLIST_BASE_URL, SETLIST_API_KEY, SPOTIFY_USER, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, REDIRECT_URI

# Mock environment variables

mock_env_vars = {SETLIST_BASE_URL: "http://example.com",
                SETLIST_API_KEY: "test-api-key",
                SPOTIFY_USER: "test_user", 
                SPOTIFY_CLIENT_ID: "test_client_id",
                SPOTIFY_CLIENT_SECRET: "test_client_secret",
                REDIRECT_URI: "test_redirect_uri"
}

@pytest.fixture
def set_mock_env():
    with patch.dict(os.environ, mock_env_vars):
        yield

@pytest.fixture
def config(set_mock_env):
    return ConfigEnv()


def test_api_base_url(config):
    assert config.api_base_url() == "http://example.com"

def test_api_key(config):
    assert config.api_key() == "test-api-key"

def test_spotify_user(config):
    assert config.spotify_user() == "test_user"

def test_spotify_client_id(config):
    assert config.spotify_client_id() == "test_client_id"

def test_spotify_client_secret(config):
    assert config.spotify_client_secret() == "test_client_secret"

def test_redirect_uri(config):
    assert config.spotify_redirect_uri() == "test_redirect_uri"

def test_check_env_vars(config):
    for var in mock_env_vars:
        print(var)
        assert os.environ[var] == mock_env_vars[var]

def test_spotify_auth(config):
    spot_auth = config.spotify_auth()
    assert isinstance(spot_auth, SpotifyAuth)
    assert spot_auth.client_id == "test_client_id"
    assert spot_auth.client_secret == "test_client_secret"
   
if __name__ == "__main__":
    pytest.main()






