import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(20):
            self.game.roll(0)  # Use roll method instead of directly accessing rolls attribute
        assert self.game.score() == 0

    def testAllOnes(self):
        self.rollMany(1, 20)  # Roll 1 for each of the 20 rolls
        assert self.game.score() == 20

    def testOneSpare(self):
        self.game.roll(5)  # Use roll method instead of directly accessing rolls attribute
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        assert self.game.score() == 16

    def testOneStrike(self):
        self.game.roll(10)  # Use roll method instead of directly accessing rolls attribute
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        assert self.game.score() == 24

    def testPerfectGame(self):
        self.rollMany(10, 12)
        assert self.game.score() == 300

    def testMultipleSpares(self):  # Renamed to avoid duplicate test name
        self.rollMany(5, 21)  # Adjusted to 21 rolls to simulate multiple spares
        assert self.game.score() == 150

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)  # Use roll method instead of directly accessing rolls attribute

if __name__ == '__main__':
    unittest.main()