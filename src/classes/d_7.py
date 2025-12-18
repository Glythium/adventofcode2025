"""
Class file containing the solution to Day Seven's puzzles
"""

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

    def one(self):
        """
        Count the number of times a beam is split in our tachyon
        manifold.
        """
        self.splits = 0
        self.matrix = self.create_matrix()
        for y_coord,line in enumerate(self.matrix):
            if y_coord == 0:
                continue
            for x_coord,character in enumerate(line):
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

    def two(self):
        """
        """
        pass

if __name__ == "__main__":
    print("[!] This is just a class definition!")
