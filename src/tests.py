import unittest
from determine_func import get_score, NotFoundMessage, ValueErrorMessage, TypeErrorMessage
from random import randint
from main import generate_game, TIMESTAMPS_COUNT, OFFSET_MAX_STEP


class TestGetScoreFunction(unittest.TestCase):
    def setUp(self):
        self.game_stamps = generate_game()

        self.random_pos = randint(1, TIMESTAMPS_COUNT)
        self.truth_offset = self.game_stamps[self.random_pos]["offset"]
        self.false_offset = TIMESTAMPS_COUNT * OFFSET_MAX_STEP

        self.incorrect_string_offset = "@!#"
        self.incorrect_object_offset = {"offset": 2134124}

    def test_truth_offset(self):
        self.result = get_score(self.game_stamps, self.truth_offset)
        self.assertIsInstance(self.result, tuple)
        self.assertEqual(len(self.result), 2)
        self.assertIsInstance(self.result[0], int)
        self.assertIsInstance(self.result[1], int)

    def test_false_offset(self):
        self.result = get_score(self.game_stamps, self.false_offset)
        self.assertIsInstance(self.result, str)
        self.assertEqual(self.result, NotFoundMessage)

    def test_incorrect_string_offset(self):
        self.result = get_score(self.game_stamps, self.incorrect_string_offset)
        self.assertIsInstance(self.result, str)
        self.assertEqual(self.result, ValueErrorMessage.format(offset=self.incorrect_string_offset))

    def test_incorrect_object_offset(self):
        self.result = get_score(self.game_stamps, self.incorrect_object_offset)
        self.assertIsInstance(self.result, str)
        self.assertEqual(self.result, TypeErrorMessage)
