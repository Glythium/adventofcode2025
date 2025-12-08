"""
Class file containing the solution to Day Three's puzzles
"""

try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D3(Day):
    """
    Class containing the solution to Day 3
    """

    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.maximum_total_joltage = 0

    def determine_max_joltage(self, joltages):
        """
        Picks the highest joltage from a set of joltages

        :param joltages: Set containing possible joltage values
        """
        max_joltage = 0
        for joltage in joltages:
            if joltage > max_joltage:
                max_joltage = joltage
        self.maximum_total_joltage += max_joltage

    def one(self):
        """
        Selects highest joltage from a bank of batteries. The joltage
        consists of two batteries in the bank.
        """
        self.maximum_total_joltage = 0
        for bank in self.input.splitlines():
            if self.debug:
                print(f"Bank: {bank}")
            joltages = set()
            left_index = 0
            right_index = 1
            while left_index < len(bank) - 1:
                while right_index < len(bank):
                    joltage = int(bank[left_index] + bank[right_index])
                    joltages.add(joltage)
                    right_index += 1
                left_index += 1
                right_index = left_index + 1
            if self.debug:
                print(f"Joltages: {joltages}")
            self.determine_max_joltage(joltages)
            if self.debug:
                print(f"Max joltage: {max}")
        print(f"Total Voltage: {self.maximum_total_joltage}")

    def two(self):
        """ """
        pass


if __name__ == "__main__":
    print("[!] This is just a class definition!")
