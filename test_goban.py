import unittest

from goban import Goban


class GobanTest(unittest.TestCase):
    def test_empty_slot_cannot_be_taken(self):
        goban = Goban(['o'])

        self.assertFalse(goban.is_taken(0, 0))

    def test_alone_piece_cannot_be_taken(self):
        goban = Goban(['#.'])

        self.assertFalse(goban.is_taken(0, 0))

    def test_two_different_piece_can_be_taken(self):
        goban = Goban(['#o'])

        self.assertTrue(goban.is_taken(0, 0))

    def test_liberty_down_cannot_be_taken(self):
        goban = Goban([
            '#o',
            '..'
        ])

        self.assertFalse(goban.is_taken(0, 0))

    def test_cornered_piece_can_be_taken(self):
        goban = Goban([
            '#o',
            'o.'
        ])

        self.assertTrue(goban.is_taken(0, 0))

    def test_left_liberty_cannot_be_taken(self):
        goban = Goban([
            '.#o',
            '.o.'
        ])

        self.assertFalse(goban.is_taken(1, 0))

    def test_up_piece_can_be_taken(self):
        goban = Goban([
            'o#o',
            '.o.'
        ])

        self.assertTrue(goban.is_taken(1, 0))

    def test_up_liberty_cannot_be_taken(self):
        goban = Goban([
            '.o.',
            'o#o',
            '.o.'
        ])

        self.assertTrue(goban.is_taken(1, 1))

    def test_rounded_line_can_be_taken(self):
        goban = Goban([
            '.oo.',
            'o##o',
            '.oo.'
        ])

        self.assertTrue(goban.is_taken(1, 1))
        self.assertTrue(goban.is_taken(2, 1))

    def test_open_rounded_line_can_not_be_taken(self):
        goban = Goban([
            '.oo.',
            'o##.',
            '.oo.'
        ])

        self.assertFalse(goban.is_taken(1, 1))
        self.assertFalse(goban.is_taken(2, 1))

    def test_l_shape_can_be_taken(self):
        goban = Goban([
            '.oo.',
            'o#o.',
            'o#oo',
            'o###o',
            '.ooo'
        ])

        self.assertTrue(goban.is_taken(2, 3))

    def test_square_shape_can_be_taken(self):
        goban = Goban([
            'oo.',
            '##o',
            '##o',
            'oo.',
        ])

        self.assertTrue(goban.is_taken(0, 1))
        self.assertTrue(goban.is_taken(0, 2))
        self.assertTrue(goban.is_taken(1, 1))
        self.assertTrue(goban.is_taken(1, 2))
