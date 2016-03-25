from song import Song
from datetime import timedelta
from prettytable import PrettyTable
import json
import random


class Playlist:

    def __init__(self, name, repeat, shuffle):
        self.name = name
        self.repeat = False
        self.shuffle = False
        self.list = []
        self.song_index = 0

    def dasherize_name(self):
        name = self.name.replace(" ", "-")
        return name

    def add_songs(self, songs):
        if isinstance(songs, Song):
            self.list.append(songs)
        elif isinstance(songs, list):
            for song in songs:
                self.add_songs(song)
        else:
            raise TypeError

    def remove_song(self, song):
        if song in self.list:
            self.list.remove(song)
        else:
            return "There is no such song in the playlist."

    def total_length(self):
        total = 0
        for song in self.list:
            total += song.length("seconds")
        return str(timedelta(seconds=total))

    def songs_of_artist(self, artist):
        total = 0
        for song in self.list:
            if song.artist == artist:
                total += 1
        return total

    def artists(self):
        artists_dict = {}
        for song in self.list:
            artists_dict[song.artist] = self.songs_of_artist(song.artist)
        return artists_dict

    def next_song(self):
        played_songs = set()

        song = self.list[self.song_index]

        if song not in played_songs:
            self.song_index += 1

            if self.song_index >= len(self.list) and self.repeat:
                self.song_index = 0
                played_songs.add(song)

            if self.shuffle:
                song = random.choice(self.list)
                played_songs.add(song)

        return song

    def pprint_playlist(self):
        table = PrettyTable(['Artist', 'Song', 'Length'])
        for song in self.list:
            table.add_row([song.artist, song.title, song.length()])

        return table

    def name_to_json(self):
        for blank_space in self.name:
            if blank_space == " ":
                blank_space = "-"
            return "{}.json".format(self.dasherize_name())

    def path(self):
        return "/home/martin056/Desktop/playlist-data/{}".format(self.name_to_json())

    def make_json(self):
        try:
            with open(self.path(), "x+") as f:
                json.dump({}, f, indent=4)
        except:
            raise FileExistsError("This playlist already exists.")

    def save_playlist(self):
        songs = []

        for song in self.list:
            songs.append(song.song_to_dict())

        dumper = {
            "name": self.name,
            "repeat": self.repeat,
            "shuffle": self.shuffle,
            "songs": songs,
        }

        with open(self.path(), "w") as f:
            json.dump(str(dumper), f, indent=4)

    def load_playlist(self):
        with open(self.path(), "r") as f:
            data = json.load(f)

        return data

playlist = Playlist("bal sam mu maikata", False, False)
song = Song("Bout Me", "Wiz Khalifa", "Cabin Fever", "3:30")
song1 = Song("Bout Meee", "Wwwwiz Khalifa", "Cabin Ffever", "4:30")
playlist.add_songs([song, song1])
playlist.save_playlist()
print(playlist.load_playlist())
