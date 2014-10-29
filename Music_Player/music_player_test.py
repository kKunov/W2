import unittest
from music_player import Song
from music_player import PlayList


class TestSong(unittest.TestCase):

    def setUp(self):
        self.new_song = Song("How Come", "D12", "D12 World", 225, 320)

    def test_init(self):
        self.assertEqual(self.new_song.title, "How Come")
        self.assertEqual(self.new_song.artist, "D12")
        self.assertEqual(self.new_song.album, "D12 World")
        self.assertEqual(self.new_song.le, 225)
        self.assertEqual(self.new_song.bitrate, 320)
        self.assertEqual(self.new_song.rating, 0)

    def test_rate(self):
        self.new_song.rate(3)
        self.assertEqual(self.new_song.rating, 3)
        with self.assertRaises(ValueError):
            self.new_song.rate(6)
        with self.assertRaises(ValueError):
            self.new_song.rate(-1)

    def test_str(self):
        self.assertEqual(str(self.new_song), "D12 - How Come  3:45")


class TestPlayList(unittest.TestCase):

    def setUp(self):
        self.new_song = Song("How Come", "D12", "D12 World", 225, 320, 4)
        self.new_song2 = Song("Berserk", "Eminem", "MMLP2", 200, 120, 5)
        self.new_pl = PlayList("PL1")

    def test_init(self):
        self.assertEqual(self.new_pl.name, "PL1")

    def test_add_song_and_remove_song(self):
        self.new_pl.add_song(self.new_song)
        self.assertTrue(self.new_song in self.new_pl.playlist)
        self.new_pl.add_song(self.new_song2)
        self.assertTrue(self.new_song2 in self.new_pl.playlist)
        self.new_pl.remove_song("Berserk")
        self.assertFalse(self.new_song2 in self.new_pl.playlist)

    def test_total_length(self):
        self.new_pl.add_song(self.new_song)
        self.assertEqual(self.new_pl.total_length(), 225)
        self.new_pl.add_song(self.new_song2)
        self.assertEqual(self.new_pl.total_length(), 425)

    def test_remove_disrated(self):
        self.new_pl.add_song(self.new_song)
        self.new_pl.add_song(self.new_song2)
        self.new_pl.remove_disrated(4)
        self.assertFalse(self.new_song in self.new_pl.playlist)
        self.assertTrue(self.new_song2 in self.new_pl.playlist)

    def test_remuve_bad_quality(self):
        self.new_pl.add_song(self.new_song)
        self.new_pl.add_song(self.new_song2)
        self.new_pl.remove_bad_quality()
        self.assertFalse(self.new_song2 in self.new_pl.playlist)

    def test_show_artist(self):
        self.new_pl.add_song(self.new_song)
        self.new_pl.add_song(self.new_song2)
        new_song3 = Song("Legacy", "Eminem", "MMLP2", 376, 320, 5)
        self.new_pl.add_song(new_song3)
        self.assertTrue('Eminem' and 'D12' in self.new_pl.show_artist())


if __name__ == '__main__':
    unittest.main()
