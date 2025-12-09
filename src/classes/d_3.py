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
        if self.debug:
            print(f"Max joltage: {max_joltage}\n")
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
        print(f"Total Voltage: {self.maximum_total_joltage}")

    def two(self):
        """
        Selects highest joltage from a bank of batteries. The joltage
        consists of twelve batteries in the bank.
        """
        self.maximum_total_joltage = 0
        for bank in self.input.splitlines():
            if self.debug:
                print(f"Bank: {bank}")
            # Empty string to build the 12-digit joltage
            joltage = str()
            # Maximum offset from the bank from which we can
            # still build a 12-digit joltage
            offset = 11
            # While we have digits to append
            while offset >= 0:
                # Reset the highest number tracker
                highest_num = 0
                # Calculate how deep we can search the bank
                max_start_index = len(bank) - offset
                # Search through until the last feasible index
                if self.debug:
                    print(f"Offset: {offset} - Max Start Index: {max_start_index}")
                    print(f"Searching through: {bank[:max_start_index]}")
                for battery in bank[:max_start_index]:
                    # If the battery joltage is higher
                    if int(battery) > highest_num:
                        # Then it becomes the highest number
                        highest_num = int(battery)
                # Calculate the new starting position
                start_pos = bank.index(str(highest_num)) + 1
                # Chop off the parts preceding parts of the bank
                bank = bank[start_pos:]
                if self.debug:
                    print(f"Remaining Bank: {bank}")
                # Append the highest joltage to the string
                joltage += str(highest_num)
                # Decrement the offset and move on
                offset -= 1
            if self.debug:
                print(f"Joltage: {joltage}\n")
            self.maximum_total_joltage += int(joltage)
        print(f"Maximum total joltage: {self.maximum_total_joltage}")


if __name__ == "__main__":
    print("[!] This is just a class definition!")
