"""
Class file containing the solution to Day One's puzzles
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

    def one(self):
        """
        Find the maximum joltage provided by a bank of batteries
        """
        maximum_total_joltage = 0
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
            max = 0
            for joltage in joltages:
                if joltage > max:
                    max = joltage
            maximum_total_joltage += max
            if self.debug:
                print(f"Max joltage: {max}")
        print(f"Total Voltage: {maximum_total_joltage}")


    def two(self):
        """
        
        """
        pass


if __name__ == "__main__":
    print("[!] This is just a class definition!")
