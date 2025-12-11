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
                self.ingredient_id_ranges.append([int(low), int(high)])
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
        for idx, id_range in enumerate(self.ingredient_id_ranges):
            # Add one to the high end because the ranges are meant
            # to be inclusive
            self.ingredient_id_ranges[idx] = range(id_range[0], id_range[1] + 1)
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
        self.fresh_ingredients = 0
        self.parse_ingredient_db()
        is_not_deduplicated = True
        while is_not_deduplicated:
            is_not_deduplicated = False
            if self.debug:
                print(f"Processing ranges: {self.ingredient_id_ranges}")
            for idx_one,id_range in enumerate(self.ingredient_id_ranges):
                for idx_two,comp in enumerate(self.ingredient_id_ranges):
                    # Don't compare the same ranges
                    if idx_one == idx_two:
                        continue
                    # Our min is higher than the comparator's min
                    if id_range[0] >= comp[0]:
                        # Our max is lower than the comparator's max
                        if id_range[1] <= comp[1]:
                            is_not_deduplicated = True
                            if self.debug:
                                print(f"{id_range} entirely within {comp}")
                            self.ingredient_id_ranges.pop(idx_one)
                            break
                        # Our min is within comparator's range
                        elif id_range[0] <= comp[1]:
                            is_not_deduplicated = True
                            if self.debug:
                                print(f"{id_range} extends {comp}")
                            new_range = [comp[0], id_range[1]]
                            self.ingredient_id_ranges[idx_one] = new_range
                            self.ingredient_id_ranges.pop(idx_two)
                            break
                    # Our max is less than the comparator's max
                    elif id_range[1] <= comp[1]:
                        # Our max is within the comparator's range
                        if id_range[1] >= comp[0]:
                            is_not_deduplicated = True
                            if self.debug:
                                print(f"{id_range} prepends {comp}")
                            new_range = [id_range[0], comp[1]]
                            self.ingredient_id_ranges[idx_one] = new_range
                            self.ingredient_id_ranges.pop(idx_two)
                            break
                if is_not_deduplicated:
                    # Reset the search to see if the new range
                    # now includes other, earlier ranges
                    break
            if self.debug:
                print(f"Processed ranges: {self.ingredient_id_ranges}")
        for id_range in self.ingredient_id_ranges:
            # Add one to the max to make it inclusive
            ingredients = id_range[1] + 1 - id_range[0]
            self.fresh_ingredients += ingredients
        print(f"Fresh ingredients: {self.fresh_ingredients}")


if __name__ == "__main__":
    print("[!] This is just a class definition!")
