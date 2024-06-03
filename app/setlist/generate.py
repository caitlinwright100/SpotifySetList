from app.setlist.connect import ConnectAndSearchArtistSetlist
from app.setlist.filter import SetListFilter


def generate_setlist(
        connector: ConnectAndSearchArtistSetlist,
        artist_name,
        playlist_flag
):
    setlistfm_data = connector.connect_to_api(artist_name)
    

    # Filter setlists for Spotify playlist
    filter = SetListFilter(setlistfm_data)
    spotify_setlist = filter.produce_setlist(playlist_flag)


    return spotify_setlist






# def generate_setlist(base_url, api_key, artist_name, playlist_flag):

#     connector = ConnectAndSearchArtistSetlist(base_url, api_key)
#     setlistfm_data = connector.connect_to_api(artist_name)

#     # Filter setlists for Spotify playlist
#     filter = SetListFilter(setlistfm_data)
#     spotify_setlist = filter.produce_setlist(setlistfm_data, playlist_flag)

#     return spotify_setlist
