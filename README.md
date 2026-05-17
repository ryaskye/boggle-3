Boggle Solver
A Python implementation of a Boggle board solver using depth-first search (DFS). Given a grid of letter tiles and a dictionary of words, the solver finds every valid word that can be traced through adjacent tiles.
Supports the standard Boggle variant that uses QU and ST as combined two-character tiles.

How It Works
The solver performs a DFS from every cell in the grid for each word in the dictionary. It tracks visited cells so no tile is reused within a single word path. Words under 3 characters are ignored, matching standard Boggle rules.
Special tile handling:

A QU tile counts as two characters and only matches the sequence "QU" in a word.
An ST tile works the same way, matching only "ST".
Grids containing standalone Q or S tiles are treated as invalid under these rules.

