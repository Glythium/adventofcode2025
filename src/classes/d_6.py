"""
Class file containing the solution to Day Six's puzzles
"""

try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D6(Day):
    """
    Class containing the solution to Day 6
    """

    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.math_problems = list()
        self.grand_total = 0

    def parse_math_problems(self):
        """
        Parses the list of math problems and creates a list of 
        integers and an operator. Each element in the list looks like:
        [ 1, 2, 3, "+"]
        """
        num_problems = len(self.input.splitlines()[0].split())
        for i in range(num_problems):
            # Seed the problems list with placeholders to fill in next
            self.math_problems.append(list())
        for line in self.input.splitlines():
            for idx,element in enumerate(line.split()):
                if element.isdigit():
                    element = int(element)
                self.math_problems[idx].append(element)

    def one(self):
        """
        Determine the grand total found by adding together all of the
        answers to the individual math problems?
        """
        self.parse_math_problems()
        for problem in self.math_problems:
            # Start with the first element in the list instead of zero
            # to avoid multiplying by zero
            total = problem[0]
            # Iterate through the remaining numbers in the problem
            for number in problem[1:-1]:
                if problem[-1] == "+":
                    total += number
                elif problem[-1] == "*":
                    total *= number
            self.grand_total += total
        print(f"Grand total: {self.grand_total}")

    def two(self):
        """
        """
        pass


if __name__ == "__main__":
    print("[!] This is just a class definition!")
