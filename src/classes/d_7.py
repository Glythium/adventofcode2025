"""
Class file containing the solution to Day Seven's puzzles
"""

import functools

try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D7(Day):
    """
    Class containing the solution to Day 7
    """

    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.matrix = list()
        self.splits = 0
        self.paths = 0

    def one(self):
        """
        Count the number of times a beam is split in our tachyon
        manifold.
        """
        self.splits = 0
        self.matrix = self.create_matrix()
        for y_coord, line in enumerate(self.matrix):
            if y_coord == 0:
                continue
            for x_coord, character in enumerate(line):
                up = self.matrix[y_coord - 1][x_coord]
                if up == "S" or up == "|":
                    if character == "^":
                        try:
                            self.matrix[y_coord][x_coord - 1] = "|"
                        except IndexError:
                            pass
                        try:
                            self.matrix[y_coord][x_coord + 1] = "|"
                        except IndexError:
                            pass
                        self.splits += 1
                    elif character != "|":
                        self.matrix[y_coord][x_coord] = "|"
        if self.debug:
            self.print_matrix()
        print(f"Splits: {self.splits}")

    # def chart_quantum_paths(self, start_coords):
    #     """
    #     Recursively counts every path for a single tachyon particle.

    #     DANGER: This was my first try at this solution, it ran overnight
    #     so I'm pivoting to a way more optimized solution for this part.

    #     :param start_coords: (x,y) coordinates where a split occurred
    #     """
    #     x_coord = start_coords[0]
    #     y_coord = start_coords[1]
    #     if y_coord == len(self.matrix) - 1:
    #         # Base case, we've reached the end of the grid
    #         self.paths += 1
    #         if self.paths % 50000000 == 0:
    #             print(f"Running: paths just hit {self.paths}")
    #         return
    #     # Split here
    #     if self.matrix[y_coord + 1][x_coord] == "^":
    #         # Go left, then right
    #         left = (x_coord - 1, y_coord + 1)
    #         right = (x_coord + 1, y_coord + 1)
    #         self.chart_quantum_paths(left)
    #         self.chart_quantum_paths(right)
    #     else:
    #         # Go down
    #         self.chart_quantum_paths((x_coord, y_coord + 1))

    @functools.lru_cache
    def chart_quantum_paths(self, start_coords):
        """
        Recursively counts every path for a single tachyon particle.

        Source: https://www.reddit.com/r/adventofcode/comments/1pg9w66/comment/nty8ykh/

        :param start_coords: (x,y) coordinates where a split occurred
        """
        x_coord = start_coords[0]
        y_coord = start_coords[1]
        if y_coord == len(self.matrix) - 1:
            return 1
        if self.matrix[y_coord + 1][x_coord] == ".":
            return self.chart_quantum_paths((x_coord, y_coord + 1))
        if self.matrix[y_coord + 1][x_coord] == "^":
            return self.chart_quantum_paths(
                (x_coord - 1, y_coord)
            ) + self.chart_quantum_paths((x_coord + 1, y_coord))

    def two(self):
        """
        Trace the particle through the quantum tachyon manifold.
        """
        self.matrix = self.create_matrix()
        start_x = self.matrix[0].index("S")
        self.paths = self.chart_quantum_paths((start_x, 0))
        print(f"Paths: {self.paths}")


if __name__ == "__main__":
    print("[!] This is just a class definition!")
