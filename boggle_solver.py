class Boggle:
    """
    Boggle solver using depth-first search.

    Supports standard letter tiles as well as the special
    two-character tiles 'QU' and 'ST' used in some Boggle variants.
    Grids containing standalone 'Q' or 'S' tiles are considered invalid
    under these rules — those letters must appear as 'QU' or 'ST'.
    """

    DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),           (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]

    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = set(word.upper() for word in dictionary)
        self.solutions = set()
        self.rows = len(grid)
        self.cols = len(grid[0]) if grid and grid[0] else 0

    def is_valid_grid(self):
        """
        Return True only if the grid is non-empty, square, and contains
        no standalone 'Q' or 'S' tiles (they must appear as 'QU' / 'ST').
        """
        if not self.grid or not self.grid[0]:
            return False
        if len(self.grid) != len(self.grid[0]):
            return False
        for row in self.grid:
            for tile in row:
                upper = tile.upper()
                if upper in ("Q", "S"):
                    return False
        return True

    def _dfs(self, word, i, j, visited, index):
        """Depth-first search from cell (i, j) trying to match word[index:]."""
        if index >= len(word):
            return
        if not (0 <= i < self.rows and 0 <= j < self.cols):
            return
        if (i, j) in visited:
            return

        tile = self.grid[i][j].upper()

        # Two-character tile: QU
        if tile == "QU":
            if word[index:index + 2] == "QU":
                visited.add((i, j))
                if index + 2 == len(word):
                    self.solutions.add(word)
                else:
                    self._search_neighbors(word, i, j, visited, index + 2)
                visited.remove((i, j))
            return

        # Two-character tile: ST
        if tile == "ST":
            if word[index:index + 2] == "ST":
                visited.add((i, j))
                if index + 2 == len(word):
                    self.solutions.add(word)
                else:
                    self._search_neighbors(word, i, j, visited, index + 2)
                visited.remove((i, j))
            return

        # Single character tile must match the current character in the word
        if tile != word[index]:
            return

        visited.add((i, j))
        if index + 1 == len(word):
            self.solutions.add(word)
        else:
            self._search_neighbors(word, i, j, visited, index + 1)
        visited.remove((i, j))

    def _search_neighbors(self, word, i, j, visited, index):
        """Explore all 8 adjacent cells from (i, j)."""
        for di, dj in self.DIRECTIONS:
            self._dfs(word, i + di, j + dj, visited, index)

    def getSolution(self):
        """
        Return a sorted list of all dictionary words (3+ letters)
        that can be found in the grid.
        """
        if not self.is_valid_grid():
            return []
        for word in self.dictionary:
            if len(word) >= 3:
                for i in range(self.rows):
                    for j in range(self.cols):
                        self._dfs(word, i, j, set(), 0)
        return sorted(self.solutions)


def main():
    grid = [
        ["A", "B", "Y", "R"],
        ["E", "N", "P", "H"],
        ["G", "Z", "QU", "R"],
        ["I", "L", "O", "ST"],
    ]
    dictionary = [
        "art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry",
        "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet",
        "arty", "not", "quar",
    ]
    game = Boggle(grid, dictionary)
    print("Words found:", game.getSolution())


if __name__ == "__main__":
    main()
