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
    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.dial_number = 50
        self.number_of_zeroes = 0
        self.passed_by_zero = 0
        self.dial_min = 0
        self.dial_max = 99


    def parse_instruction(self, line):
        """
        Parses the instruction line to separate the direction from the clicks

        Returns a tuple containing the chr(direction), int(clicks)
        """
        direction = line[0]
        clicks = int(line[1:])
        return (direction, clicks)

    
    def turn_dial_left(self, clicks):
        """
        Turn the dial to the left some number of clicks. If the dial crosses
        zero, set the dial_number to dial_max and increment self.passed_by_zero 
        """
        starting_on_zero = (self.dial_number == 0)
        if self.debug:
            print(f"Dial starting position: {self.dial_number}")
        while clicks > 0:
            clicks -= 1
            self.dial_number -= 1
            if self.dial_number < self.dial_min:
                if not starting_on_zero:
                    self.passed_by_zero += 1
                    if self.debug:
                        print(f"Passed by Zero: {self.passed_by_zero}")
                starting_on_zero = False
                self.dial_number = self.dial_max
        return


    def turn_dial_right(self, clicks):
        """
        Turn the dial to the right some number of clicks. If the dial crosses
        dial_max, set the dial_number to dial_min 
        """
        starting_on_zero = (self.dial_number == 0)
        if self.debug:
            print(f"Dial starting position: {self.dial_number}")
        while clicks > 0:
            clicks -= 1
            self.dial_number += 1
            if self.dial_number == 1 and not starting_on_zero:
                self.passed_by_zero += 1
                if self.debug:
                    print(f"Passed by Zero: {self.passed_by_zero}")
            if self.dial_number > self.dial_max:
                starting_on_zero = False
                self.dial_number = self.dial_min
        return


    def solve(self):
        self.dial_number = 50
        self.number_of_zeroes = 0
        self.passed_by_zero = 0
        for line in self.input.splitlines():
            if self.debug:
                print(f"Line: {line}")
            direction, clicks = self.parse_instruction(line)
            if self.debug:
                print(f"Direction: {direction} -- Clicks: {clicks}")
            if direction.upper() == "L":
                self.turn_dial_left(clicks)
            elif direction.upper() == "R":
                self.turn_dial_right(clicks)
            if self.dial_number == 0:
                print("Landed on zero!")
                self.number_of_zeroes += 1
            if self.debug:
                print(f"Dial ending position: {self.dial_number}")
                print(f"Landed on Zeroes: {self.number_of_zeroes}\n")


    def one(self):
        """
        Given a safe dial with numbers 0-99, starting on 50, make a series of
        turns based on the input file and count the number of times it lands
        on zero
        """
        self.solve()
        print(f"Landed on Zeroes: {self.number_of_zeroes}\n")


    def two(self):
        """
        Given a safe dial with numbers 0-99, starting on 50, make a series of
        turns based on the input file and count the number of times it passes
        or lands on zero
        """
        self.solve()
        print(f"Touched Zero: {self.number_of_zeroes + self.passed_by_zero}\n")

if __name__ == '__main__':
    print("[!] This is just a class definition!")
