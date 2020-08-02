import unittest
import os

from game_main import Game


class TestMain(unittest.TestCase):
    """
    def test_words(self):
        self.assertEqual(os.path.isfile(
            os.path.join(os.getcwd(), 'words',
                         'verbs_list.csv')), True)

    def test_main(self):
        new_game = Game()
        self.assertIsNotNone(new_game)
        self.assertIn(new_game.ison, [0,1])
        self.assertNotEqual(new_game.secret, "")

    def test_wordlist(self):
        new_game = Game()
        new_game.getwords()
        self.assertNotEqual(new_game.wordlist, [])

    def test_randomword(self):
        new_game = Game()
        self.assertNotEqual(new_game.randomword(), "")
        self.assertNotEqual(new_game.wordlist, [])

    def test_wordslice(self):
        new_game = Game()
        self.assertIsNotNone(new_game.sliceword())
        self.assertNotEqual(new_game.secret, "")

    def test_slicerand(self):
        new_game = Game()
        self.assertIsNotNone(new_game.slicerand())
        self.assertNotEqual(new_game.secret, "")

    def test_guess(self):
        new_game = Game()
        self.assertIsNotNone(new_game.guessword())
    """
    def test_randguess(self):
        new_game = Game()
        self.assertIsNotNone(new_game.randguess())
    """
    def test_record(self):
        new_game = Game()
        self.assertIsNotNone(new_game.set_score('monter', 1, 0))
    """

if __name__ == '__main__':
    unittest.main()