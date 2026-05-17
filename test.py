import unittest
from boggle_solver import Boggle


class TestGridValidation(unittest.TestCase):
    """Tests for grid validation logic."""

    def test_empty_grid_is_invalid(self):
        game = Boggle([[]], ["hello"])
        self.assertEqual(game.getSolution(), [])

    def test_non_square_grid_is_invalid(self):
        grid = [["A", "B", "C"], ["D", "E"]]
        game = Boggle(grid, ["abc"])
        self.assertEqual(game.getSolution(), [])

    def test_standalone_q_tile_is_invalid(self):
        grid = [["Q", "A"], ["B", "C"]]
        game = Boggle(grid, ["qab"])
        self.assertEqual(game.getSolution(), [])

    def test_standalone_s_tile_is_invalid(self):
        grid = [["S", "A"], ["B", "C"]]
        game = Boggle(grid, ["sab"])
        self.assertEqual(game.getSolution(), [])


class TestBasicSolving(unittest.TestCase):
    """Standard grid word-finding tests."""

    def test_3x3_finds_valid_words(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        game = Boggle(grid, dictionary)
        result = [w.upper() for w in game.getSolution()]
        # abc, abdhi, cfi, and dea are all reachable via adjacent cells
        self.assertIn("ABC", result)
        self.assertIn("ABDHI", result)
        self.assertIn("CFI", result)
        self.assertIn("DEA", result)
        self.assertNotIn("ABI", result)   # A -> B -> I skips rows

    def test_1x1_grid_finds_nothing(self):
        """Words must be 3+ letters; a 1x1 grid cannot produce any."""
        game = Boggle([["A"]], ["a", "b", "abc"])
        self.assertEqual(game.getSolution(), [])

    def test_words_shorter_than_3_not_returned(self):
        grid = [["A", "B"], ["C", "D"]]
        game = Boggle(grid, ["ab", "abc", "ad"])
        result = game.getSolution()
        self.assertNotIn("AB", result)
        self.assertNotIn("AD", result)

    def test_word_requires_adjacent_cells(self):
        """ACE skips B so it should not be found; ABC travels adjacently and should."""
        grid = [["A", "B", "Z"],
                ["Z", "Z", "C"],
                ["Z", "Z", "E"]]
        game = Boggle(grid, ["ace", "abc"])
        result = [w.upper() for w in game.getSolution()]
        self.assertNotIn("ACE", result)   # A and C are not adjacent
        self.assertIn("ABC", result)

    def test_cell_cannot_be_reused(self):
        grid = [["A", "B"], ["C", "D"]]
        game = Boggle(grid, ["aaa", "aba"])
        result = game.getSolution()
        self.assertNotIn("AAA", result)


class TestSpecialTiles(unittest.TestCase):
    """Tests for QU and ST two-character tiles."""

    def test_qu_tile_matches_qu_in_word(self):
        grid = [["QU", "A", "R"], ["T", "Z", "B"], ["C", "D", "E"]]
        game = Boggle(grid, ["qua", "quart", "rat"])
        result = [w.upper() for w in game.getSolution()]
        self.assertIn("QUA", result)

    def test_st_tile_matches_st_in_word(self):
        grid = [["ST", "A", "R"], ["E", "B", "C"], ["D", "F", "G"]]
        game = Boggle(grid, ["star", "stab", "ear"])
        result = [w.upper() for w in game.getSolution()]
        self.assertIn("STAR", result)
        self.assertIn("STAB", result)

    def test_qu_tile_does_not_match_single_q(self):
        """A QU tile should not match a word that only needs Q."""
        grid = [["QU", "A", "B"], ["C", "D", "E"], ["F", "G", "H"]]
        game = Boggle(grid, ["qab"])
        result = game.getSolution()
        self.assertNotIn("QAB", result)

    def test_mixed_qu_and_st_tiles(self):
        grid = [
            ["A",  "B",  "Y",  "R"],
            ["E",  "N",  "P",  "H"],
            ["G",  "Z",  "QU", "R"],
            ["I",  "L",  "O",  "ST"],
        ]
        game = Boggle(grid, ["quartz", "pry", "not", "quar"])
        result = [w.upper() for w in game.getSolution()]
        self.assertIn("PRY", result)


if __name__ == "__main__":
    unittest.main()
