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
        self.invalid_id_total = 0

    def parse_instruction(self, line):
        """
        Parses the instruction line to create a list of tuples
        containing the ID ranges

        Returns a list containing the ID ranges [(id_min, id_max), ...]
        """
        id_ranges = list()
        for product_id_range in line.split(","):
            id_ranges.append(product_id_range.split("-"))
        return id_ranges

    def one(self):
        """
        Given a range of product IDs, find invalid IDs. They are defined
        as any ID that is made only of some sequence of digits repeated
        twice.
        """
        self.invalid_id_total = 0
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
                        self.invalid_id_total += i
        print(f"Total: {self.invalid_id_total}")

    def two(self):
        """
        Given a range of product IDs, find invalid IDs. They are defined
        as any ID that is made only of some sequence of digits repeated
        at least twice.
        """
        self.invalid_id_total = 0
        id_ranges = self.parse_instruction(self.input)
        for low, high in id_ranges:
            if self.debug:
                print(f"Range: {low} - {high}")
            for i in range(int(low), int(high) + 1):
                parseable = str(i)
                comp_size = 1
                id_len = len(parseable)
                # While we can get at least two substrings out of a number
                while comp_size <= int(id_len / 2):
                    # Assume it's invalid, will save checking for validity
                    is_invalid_id = True
                    # This is the substring we're searching for
                    comparator = parseable[0:comp_size]
                    for substring_start in range(comp_size, id_len, comp_size):
                        substring_end = substring_start + comp_size
                        # This is the next substring of equivalent size
                        substring = parseable[substring_start:substring_end]
                        if comparator != substring:
                            # Break on the first non-match to speed this up
                            is_invalid_id = False
                            break
                    if is_invalid_id:
                        # Break on matching substring patterns
                        self.invalid_id_total += i
                        if self.debug:
                            print(f"Invalid ID: {i}")
                        break
                    # Otherwise, increase the comparison window size
                    comp_size += 1
            if self.debug:
                print()
        print(f"Total: {self.invalid_id_total}")


if __name__ == "__main__":
    print("[!] This is just a class definition!")
