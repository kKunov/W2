import json
from mutagen.mp3 import MP3
import glob
from pygame import mixer


class Song:

    def __init__(self, title, artist, album, le, bitrate, phat, rating=0):
        self.title = title
        self.artist = artist
        self.album = album
        self.rating = rating
        self.le = le
        self.bitrate = bitrate
        self.path = phat

    def rate(self, rating):
        if rating < 0 or rating > 5:
            print("Error: The rating must be between 0 and 5!!! Dumbass!!!")
            raise ValueError
        else:
            self.rating = rating

    def __str__(self):
        return "%s - %s  %s:%s" % (self.artist, self.title, self.le // 60, self.le % 60)


class PlayList:

    def __init__(self, name):
        self.name = name
        self.playlist = []

    def add_song(self, song):
        self.playlist.append(song)

    def remove_song(self, title):
        for index, song in enumerate(self.playlist):
            if song.title == title:
                del self.playlist[index]

    def total_length(self):
        total_le = 0
        for song in self.playlist:
            total_le += song.le
        return total_le

    def remove_disrated(self, rating):
        for index, song in enumerate(self.playlist):
            if song.rating <= rating:
                del self.playlist[index]

    def remove_bad_quality(self):
        for index, song in enumerate(self.playlist):
            if song.bitrate <= 128:
                del self.playlist[index]

    def show_artist(self):
        artists = []
        for song in self.playlist:
            artists.append(song.artist)
        return set(artists)

    def save(self):
        songs = []
        for song in self.playlist:
            songs.append({"title": song.title,
                          "artist": song.artist,
                          "album": song.album,
                          "le": song.le,
                          "bitrate": song.bitrate,
                          "path": song.path,
                          "rating": song.rating})
        pl_dict = {"name": self.name, "songs": songs}
        file = open(self.name, "w")
        file.write(json.dumps(pl_dict))
        file.close()

    @staticmethod
    def load_playlist(name):
        file = open(name, "r")
        pl_dict = json.loads(file.read())
        loaded_pl = PlayList(pl_dict["name"])
        for song in pl_dict["songs"]:
            loaded_pl.add_song(song)
        return loaded_pl


class MusicCrawler:

    def __init__(self, phat):
        self.phat = phat

    def generate_playlist(self, name):
        mp3_files = glob.glob("%s/*.mp3" % self.phat)
        pl = PlayList("My_pl")
        for song in mp3_files:
            audio = MP3(song)
            audio.pprint()
            cur_song = Song(audio["TIT2"],
                            audio["TPE1"],
                            audio["TALB"],
                            audio.info.length,
                            audio.info.bitrate,
                            song, 0)
            pl.add_song(cur_song)
        return pl


def new_pl():
    print("\nPleace enter folder path:")
    chose = raw_input()
    gen = MusicCrawler(chose)
    print("\nPleace enter playlist name:")
    chose = raw_input()
    pl = gen.generate_playlist(chose)
    return pl


def load_pl():
    print("Pleace tipe playlist name:")
    chose = raw_input()
    return PlayList.load_playlist(chose)


def play():
    print("Pleace tipe the song path to play it:")
    chose = raw_input()
    mixer.init()
    mixer.music.load(chose)
    mixer.music.play()


def choseing():
    print("This is Kokal's music player!")
    print("\nPleace chose comand:\n\n1.For making playlist, tipe 'new'")
    print("2.For loading play list type 'load'")
    print("3. For saveing tipe 'save'")
    print("4.For seeing your playlist tipe 'list'")
    print("5.For playing song tipe 'play'")
    print("6. For exit tipe 'exit'")
    chose = raw_input("What you want to do?:")
    if chose == "new":
        pl = new_pl()
    elif chose == "load":
        pl = load_pl()
    elif chose == "save":
        pl.save()
    elif chose == "list":
        for song in pl.playlist:
            print("%s - %s" % (song.artist, song.title))
    elif chose == "play":
        play()
    elif chose == exit:
        return True
    else:
        "Bad input, Try again!"
    return False


def main():
    exit = False
    while exit is False:
        exit = choseing()


if __name__ == '__main__':
    main()
