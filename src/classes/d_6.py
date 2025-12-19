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

    def build_empty_problem_list(self, num_problems):
        """
        Seed the problems list with placeholders to fill in
        """
        for i in range(num_problems):
            self.math_problems.append(list())

    def parse_math_problems(self):
        """
        Parses the list of math problems and creates a list of
        integers and an operator. Each element in the list looks like:
        [ 1, 2, 3, "+"]
        """
        for line in self.input.splitlines():
            for idx, element in enumerate(line.split()):
                if element.isdigit():
                    element = int(element)
                self.math_problems[idx].append(element)

    def one(self):
        """
        Determine the grand total found by adding together all of the
        answers to the individual math problems
        """
        num_problems = len(self.input.splitlines()[0].split())
        self.build_empty_problem_list(num_problems)
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
        Cephalopods math is written right-to-left in columns. Determine
        the grand total found by adding together all of the new answers
        to the individual math problems
        """
        # Reverse the lines
        lines = self.input.split("\n")
        for i, line in enumerate(lines):
            lines[i] = line[-1::-1]
        if self.debug:
            for line in lines:
                print(line)
        # Every column is a new math problem
        num_problems = len(lines[0]) + 1
        self.build_empty_problem_list(num_problems)
        # Begin combing vertically through the grid
        for x_coord in range(len(lines[0])):
            y_coord = 0
            # Do not concern ourselves with the last line for now
            while y_coord < len(lines) - 1:
                if self.debug:
                    print(
                        f"Idx: {x_coord, y_coord} == Char: '{lines[y_coord][x_coord]}'"
                    )
                # Ignore all spaces
                if lines[y_coord][x_coord] != " ":
                    self.math_problems[x_coord].append(lines[y_coord][x_coord])
                # Go to the next line
                y_coord += 1
        # Convert the strings to digits
        for idx, column in enumerate(self.math_problems):
            number = ""
            for character in column:
                number += character
            if number == "":
                continue
            self.math_problems[idx] = int(number)
        # Insert the operator
        operators = lines[-1].split()
        for operator in operators:
            for idx, number in enumerate(self.math_problems):
                if number == []:
                    self.math_problems[idx] = operator
                    break
        print(self.math_problems)
        # Bring it all together now
        start_idx = 0
        # Arrays are zero-indexed, thus the offset
        while start_idx < len(self.math_problems) - 1:
            # Create a lookahead cursor for the next operator
            for end_idx, element in enumerate(self.math_problems):
                if element in ["+", "*"]:
                    # Not messing with setting the answer to the
                    # first index because we're moving that around
                    if element == "*":
                        answer = 1
                    else:
                        answer = 0
                    if self.debug:
                        print(
                            f"Index: {start_idx, end_idx} < {len(self.math_problems)}"
                        )
                        print(f"Element: {element}")
                    # Play catch-up to the lookahead cursor
                    while start_idx < end_idx:
                        # Adding or multiplying numbers along the way
                        if isinstance(self.math_problems[start_idx], int):
                            if element == "+":
                                answer += self.math_problems[start_idx]
                            elif element == "*":
                                answer *= self.math_problems[start_idx]
                        start_idx += 1
                    if self.debug:
                        print(f"Column = {answer}")
                    self.grand_total += answer
        print(self.grand_total)


if __name__ == "__main__":
    print("[!] This is just a class definition!")
