# from run_things import setlist_dictionary
from collections import Counter

# from run_things import setlist_dictionary, playlist_flag


class SetListFilter:
    def __init__(self, setlistfm_data):
        self.setlist_dictionary = self.process_setlist(setlistfm_data)
        
    
    def process_setlist(self, setlistfm_data):
        dictionary_of_setlists = {}

        for setlist in setlistfm_data["setlist"]:
            event_date = setlist["eventDate"]
            # print(event_date)
            for sets in setlist.get("sets", {}).get("set", []):
                for song in sets.get("song", []):
                    song_name = song["name"]
                    dictionary_of_setlists.setdefault(event_date, 
                                                      []).append(song_name)
        
        return dictionary_of_setlists
        

    def get_first_five_setlists(self, n=5):
        first_five_keys = list(self.setlist_dictionary.keys())[:n]
        # print(first_five_keys)
        first_five_setlists = [self.setlist_dictionary[key] for key in first_five_keys]
        # print(first_five_setlists)
        most_recent_setlist = first_five_setlists[0]
        # print(most_recent_setlist)
        first_five_setlists = [
            item for sublist in first_five_setlists for item in sublist
        ]

        return first_five_setlists, most_recent_setlist

    def select_all_songs_and_order(self, first_five_setlists):

        count_song_appearance = Counter(first_five_setlists)
        selected_songs = [item for item, count in count_song_appearance.most_common()]

        return selected_songs

    def select_songs_over_eighty_percent(self, first_five_setlists, threshold=3):
        count_song_appearance = Counter(first_five_setlists)

        selected_songs = [
            item for item, count in count_song_appearance.items() if count > 3
        ]

        return selected_songs

    def update_setlist(self, most_recent_setlist, selected_songs):
        spotify_setlist = most_recent_setlist + [
            song for song in selected_songs if song not in most_recent_setlist
        ]
        return spotify_setlist

    def produce_setlist(self, playlist_flag):

        first_five_setlists, most_recent_setlist = self.get_first_five_setlists()

        if playlist_flag[0] in "yY":

            spotify_setlist = self.select_all_songs_and_order(first_five_setlists)

        else:

            selected_songs = self.select_songs_over_eighty_percent(first_five_setlists)
            spotify_setlist = self.update_setlist(most_recent_setlist, selected_songs)

        return spotify_setlist
