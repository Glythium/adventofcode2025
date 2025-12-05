"""
Class file containing the solution to Day One's puzzles
"""

try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D2(Day):
    """
    Class containing the solution to Day 2
    """
    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.invalid_ids = 0
        self.invalid_id_total = 0


    def parse_instruction(self, line):
        """
        Parses the instruction line to create a list of tuples
        containing the ID ranges

        Returns a list containing the ID ranges [(id_min, id_max), ...]
        """
        id_ranges = list()
        for product_id_range in line.split(','):
            id_ranges.append(product_id_range.split('-'))
        return id_ranges


    def one(self):
        """
        Given a range of product IDs, find invalid IDs. They are defined
        as any ID that is made only of some sequence of digits repeated
        twice.
        """
        id_ranges = self.parse_instruction(self.input)
        for low, high in id_ranges:
            for i in range(int(low), int(high) + 1):
                parseable = str(i)
                if len(parseable) % 2 == 0:
                    halfway = int(len(parseable) / 2)
                    left = parseable[0:halfway]
                    right = parseable[halfway:]
                    if left == right:
                        if self.debug:
                            print(f"Invalid ID: {parseable}")
                        self.invalid_ids += 1
                        self.invalid_id_total += i
            print(f"{low}-{high}: {self.invalid_ids}\n")
            self.invalid_ids = 0
        print(f"Total: {self.invalid_id_total}")


    def two(self):
        """
        
        """
        pass

if __name__ == '__main__':
    print("[!] This is just a class definition!")
