import pyglet
import glob


class MusicPLayer:

    def __init__(self, path):
        self.path = path
        self.player = pyglet.media.Player()

    def add_all_songs_to_player(self):
        for song in glob.glob("{}/*.mp3".format(self.path)):
            audio = pyglet.media.load(song, streaming=False)
            self.player.queue(audio)

    def play(self):
        self.player.play()

    def next(self):
        self.player.next_source()
