from mutagen.id3 import ID3
import glob


class MusicCrawler:
    def __init__(self, path):
        self.path = path

    def generate_playlist(self):
        files = glob.glob("{}/*.mp3".format(self.path))
        dic = {}
        playlist = []
        for f in files:
            audio = ID3(f)
            dic['artist'] = audio["TPE1"].text[0]
            dic['title'] = audio["TIT2"].text[0]
            dic['album'] = audio["TALB"].text[0]
            #dic['length'] = audio["TLEN"].text[0]
            playlist.append(dic)

        return playlist
