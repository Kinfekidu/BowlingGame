import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def testGutterGame(self):
        for i in range(20):
            self.game.rolls.append(0)  #Append 0 to the rolls list
        assert self.game.score()==0
    def testAllOnes(self):
        self.rollMany(1, 20) # Roll 1 for each of the20 rolls
        assert self.game.score()==20
        def rollMany(self, pins, rolls):
            for 1 in range(rolls):
                self.game.rolls.append(pins)  #Append pins to thevrolls list
    def testOneSpare(self):
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0,17)
        assert self.game.score()==16
    def testOneStrike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0,16)
        assert  self.game.score()==24
    def testPerfectGame(self):
        self.rollMany(10,12)
        assert self.game.score()==300
    def testOneSpare(self):
        self.rollMany(5,21)
        assert self.game.score()==150
    def rollMany(self, pins,rolls):
        for i in range(rolls):
            self.game.rolls(pins)
