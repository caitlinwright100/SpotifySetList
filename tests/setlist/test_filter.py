import pytest
from collections import Counter
from app.setlist.filter import SetListFilter

# Sample data for testing
setlistfm_data = {
    "setlist": [
        {"eventDate": "2024-01-01", "sets": {"set": [{"song": [{"name": "Song A"}, {"name": "Song B"}, {"name": "Song C"}]}]}},
        {"eventDate": "2024-01-02", "sets": {"set": [{"song": [{"name": "Song A"}, {"name": "Song D"}, {"name": "Song C"}]}]}},
        {"eventDate": "2024-01-03", "sets": {"set": [{"song": [{"name": "Song E"}, {"name": "Song B"}, {"name": "Song C"}]}]}},
        {"eventDate": "2024-01-04", "sets": {"set": [{"song": [{"name": "Song A"}, {"name": "Song B"}, {"name": "Song F"}]}]}},
        {"eventDate": "2024-01-05", "sets": {"set": [{"song": [{"name": "Song A"}, {"name": "Song G"}, {"name": "Song C"}]}]}}
    ]
}

setlist_dictionary = {
    "2024-01-01": ["Song A", "Song B", "Song C"],
    "2024-01-02": ["Song A", "Song D", "Song C"],
    "2024-01-03": ["Song E", "Song B", "Song C"],
    "2024-01-04": ["Song A", "Song B", "Song F"],
    "2024-01-05": ["Song A", "Song G", "Song C"],
}





@pytest.fixture
def setlist_filter():
    return SetListFilter(setlistfm_data)


def test_process_setlist(setlist_filter):
    assert setlist_filter.setlist_dictionary == setlist_dictionary

def test_process_setlists_empty_data():
    setlist_processor = SetListFilter({"setlist": []})
    assert setlist_processor.setlist_dictionary == {}


def test_get_first_five_setlists(setlist_filter):
    first_five_setlists, most_recent_setlist = setlist_filter.get_first_five_setlists()
    assert len(first_five_setlists) == 15
    assert most_recent_setlist == ["Song A", "Song B", "Song C"]


def test_select_all_songs_and_order(setlist_filter):
    first_five_setlists, _ = setlist_filter.get_first_five_setlists()
    selected_songs = setlist_filter.select_all_songs_and_order(first_five_setlists)
    assert selected_songs == [
        "Song A",
        "Song C",
        "Song B",
        "Song D",
        "Song E",
        "Song F",
        "Song G",
    ]


def test_update_setlist(setlist_filter):
    most_recent_setlist = ["Song A", "Song B", "Song C"]
    selected_songs = ["Song D", "Song E"]
    spotify_setlist = setlist_filter.update_setlist(most_recent_setlist, selected_songs)
    assert spotify_setlist == ["Song A", "Song B", "Song C", "Song D", "Song E"]


def test_produce_setlist_all_songs(setlist_filter):
    playlist_flag = "y"
    spotify_setlist = setlist_filter.produce_setlist(playlist_flag)
    assert spotify_setlist == [
        "Song A",
        "Song C",
        "Song B",
        "Song D",
        "Song E",
        "Song F",
        "Song G",
    ]


def test_produce_setlist_songs_over_threshold(setlist_filter):
    playlist_flag = "n"
    spotify_setlist = setlist_filter.produce_setlist(playlist_flag)
    assert spotify_setlist == ["Song A", "Song B", "Song C"]

