"""
File containing the abstract base class for each Day
"""


class Day:
    """
    Abstract base class for each Day's solutions
    """

    def __init__(self, input_file, debug=False):
        self.debug = debug
        self.total = 0
        self.input = self.read_input(input_file)
        self.matrix = list()

    def read_input(self, input_file):
        """
        Reads in text in a given input file, returns the input as a string
        """
        try:
            with open(input_file, "r", encoding="utf-8") as fp:
                return fp.read()
        except FileNotFoundError:
            if self.debug:
                print(f"[!] FileNotFound '{input_file}'")
            return None

    def create_matrix(self):
        """
        Creates a two-dimensional array out of the input
        """
        matrix = []
        for line in self.input.splitlines():
            this_line = []
            for character in line:
                this_line.append(character)
            matrix.append(this_line)
        return matrix

    def print_matrix(self):
        """
        Prints the matrix in its current state
        """
        for line in self.matrix:
            print(line)

    def one(self):
        """
        Override this in your child class
        """
        pass

    def two(self):
        """
        Override this in your child class
        """
        pass


if __name__ == "__main__":
    print("[!] This is just the abstract base class!")
