from main import ReversiGame
import unittest
from examples import testboard


class TestReversi(unittest.TestCase):
    r = ReversiGame()

    def test_is_black_turn_1(self):
        self.assertEqual(self.r.is_black_turn(0), True)

    def test_is_black_turn_2(self):
        self.assertEqual(self.r.is_black_turn(1), False)
