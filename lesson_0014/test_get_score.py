import unittest

from bowling import BowlingScore


class BowlingScoreTest (unittest.TestCase):

    def setUp(self):
        self.bowling_score = BowlingScore()

    def test_get_score_normal(self):
        self.bowling_score.get_score("555555")
        self.assertEqual(self.bowling_score.result, 30)

    def test_get_score_strike(self):
        self.bowling_score.get_score("XXX")
        self.assertEqual(self.bowling_score.result, 60)

    def test_get_score_spare(self):
        self.bowling_score.get_score("5/5/5/")
        self.assertEqual(self.bowling_score.result, 45)

    def test_check_frame_normal(self):
        result = self.bowling_score._check_frame('555555')
        self.assertEqual(result, True)

    def test_check_frame_lage_error(self):
        result = self.bowling_score._check_frame('5555555')
        self.assertEqual(result, False)

    def test_check_frame_small_error(self):
        result = self.bowling_score._check_frame('5555')
        self.assertFalse(result)

    def test_check_input_data_normal(self):
        self.assertRaises(Exception, self.bowling_score._check_input_data, '4//555')


if __name__ == '__main__':
    unittest.main()