"""
Class file containing the solution to Day One's puzzles
"""

try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D1(Day):
    """
    Class containing the solution to Day 1
    """
    def __init__(self, debug=False):
        super().__init__(debug=debug)

    def one(self, input_file):
        """
        """
        pass

    def two(self, input_file):
        """
        """
        pass

if __name__ == '__main__':
    print("[!] This is just a class definition!")
