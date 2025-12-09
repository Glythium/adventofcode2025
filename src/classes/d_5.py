"""
Class file containing the solution to Day Five's puzzles
"""

try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D5(Day):
    """
    Class containing the solution to Day 5
    """

    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.ingredient_id_ranges = list()
        self.ingredient_ids = list()
        self.fresh_ingredients = 0

    def parse_ingredient_db(self):
        """
        Creates a list of ingredient ID ranges and another of
        available ingredient IDs
        """
        is_id_range = True
        for line in self.input.splitlines():
            # splitlines() makes the separating line an empty string
            if line == "":
                is_id_range = False
                continue
            if is_id_range:
                low, high = line.split("-")
                # Add one to the hig end because the ranges are meant
                # to be inclusive
                self.ingredient_id_ranges.append(range(int(low), int(high) + 1))
            else:
                self.ingredient_ids.append(int(line))
        if self.debug:
            print(f"Ranges: {self.ingredient_id_ranges}")
            print(f"IDs: {self.ingredient_ids}")

    def one(self):
        """
        Determine which of the available ingredient IDs are fresh when
        given a list of ingredient IDs and ingredients.
        """
        self.fresh_ingredients = 0
        self.parse_ingredient_db()
        for i in self.ingredient_ids:
            for id_range in self.ingredient_id_ranges:
                if i in id_range:
                    self.fresh_ingredients += 1
                    if self.debug:
                        print(f"{i} is in {id_range}")
                    break
        print(f"Fresh ingredients: {self.fresh_ingredients}")

    def two(self):
        """
        Determine how many fresh ingredients are possible given some
        ranges.
        """
        pass


if __name__ == "__main__":
    print("[!] This is just a class definition!")
