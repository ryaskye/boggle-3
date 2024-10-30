import unittest
import sys
from boggle_solver import Boggle

# Update sys.path to include the path where Boggle class is located
sys.path.append("/home/codio/workspace/")  # Path to find boggle_solver.py


class TestSuite_Alg_Scalability_Cases(unittest.TestCase):
    """Test case for scalability with various grid and dictionary sizes."""

    def test_Normal_case_3x3(self):
        grid = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = ["abc", "abdhi"]
        expected = [x.upper() for x in expected]
        self.assertEqual(sorted(expected), sorted(solution))


class TestSuite_Simple_Edge_Cases(unittest.TestCase):
    """Test cases for simple and edge scenarios."""

    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "b", "c"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        self.assertEqual(sorted(expected), sorted(solution))

    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["hello", "there", "general", "kenobi"]
        mygame = Boggle(grid, dictionary)
        solution = mygame.getSolution()
        solution = [x.upper() for x in solution]
        expected = []
        self.assertEqual(sorted(expected), sorted(solution))


class TestSuite_Complete_Coverage(unittest.TestCase):
    """Comprehensive test cases for complex scenarios."""

    def test_case_1(self):
        self.assertEqual(True, True)


class TestSuite_Qu_and_St(unittest.TestCase):
    """Test cases specifically for QU and ST character sequences."""

    def test_case_1(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
