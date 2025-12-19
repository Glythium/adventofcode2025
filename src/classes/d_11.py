"""
Class file containing the solution to Day Eleven's puzzles
"""

try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D11(Day):
    """
    Class containing the solution to Day 11
    """

    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.cable_map = dict()
        self.paths = 0

    def traverse_cable_map(self, key):
        """
        Recursively jumps through the self.cable_map

        :param key: The key in the self.cable_map to recurse through
        """
        count = 0
        if key == "out":
            return 1
        for value in self.cable_map[key]:
            count += self.traverse_cable_map(value)
        return count

    def one(self):
        """
        Count how many paths there are from "you" to "out"
        """
        self.cable_map = dict()
        lines = self.input.splitlines()
        for line in lines:
            key, values = line.split(":")
            self.cable_map[key] = values.split()
        if self.debug:
            print(self.cable_map)
        self.paths = self.traverse_cable_map("you")
        print(f"Paths from 'you' to 'out': {self.paths}")

    def two(self):
        """ 
        """
        pass


if __name__ == "__main__":
    print("[!] This is just a class definition!")
