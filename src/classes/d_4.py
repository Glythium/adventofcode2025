"""
Class file containing the solution to Day Four's puzzles
"""

try:
    from .day import Day
except ModuleNotFoundError:
    print("[!] Run src/main.py from the src directory")


class D4(Day):
    """
    Class containing the solution to Day 4
    """

    def __init__(self, input_file, debug=False):
        super().__init__(input_file, debug=debug)
        self.grid = list()
        self.accessible_rolls = 0
        self.surrounding_rolls = 0
        self.removed_coords = list()

    def parse_grid(self):
        """
        Create a two-dimensional array out of a given grid as input
        """
        for line in self.input.splitlines():
            characters = list()
            for character in line:
                characters.append(character)
            self.grid.append(characters)
        if self.debug:
            for line in self.grid:
                print(f"{line}")
            print()

    def is_target_character(self, x_coord, y_coord):
        """
        Increments surrounding_rolls count if our target character is
        at a given x,y coordinate in the grid

        :param x_coord: Index of the character within a line to check
        :param y_coord: Index of the line in within a grid to check
        """
        if self.grid[y_coord][x_coord] == "@":
            self.surrounding_rolls += 1
        return

    def get_surrounding_nodes(self, x_coord, y_coord):
        """
        Given an x and y coordinate, increment the accessible_rolls
        count if there are less than 4 paper rolls in the eight
        possible surrounding positions

        :param x_coord: Index of the character within a line to check
        :param y_coord: Index of the line in within a grid to check
        """
        has_up = y_coord > 0
        has_down = y_coord < len(self.grid) - 1
        has_left = x_coord > 0
        has_right = x_coord < len(self.grid[0]) - 1
        self.surrounding_rolls = 0
        if has_left:
            # Directly to the left
            self.is_target_character(x_coord - 1, y_coord)
        if has_right:
            # Directly to the right
            self.is_target_character(x_coord + 1, y_coord)
        if has_up:
            # Directly up
            self.is_target_character(x_coord, y_coord - 1)
            if has_left:
                # Diagonal up and to the left
                self.is_target_character(x_coord - 1, y_coord - 1)
            if has_right:
                # Diagonal up and to the right
                self.is_target_character(x_coord + 1, y_coord - 1)
        if has_down:
            # Directly down
            self.is_target_character(x_coord, y_coord + 1)
            if has_left:
                # Diagonal down and to the left
                self.is_target_character(x_coord - 1, y_coord + 1)
            if has_right:
                # Diagonal down and to the right
                self.is_target_character(x_coord + 1, y_coord + 1)
        if self.surrounding_rolls < 4:
            self.accessible_rolls += 1
            self.removed_coords.append([x_coord, y_coord])

    def remove_rolls(self):
        """
        Sweep through the grid and remove rolls of paper "@". Replace
        them with an "x" in the grid.
        """
        self.removed_coords = list()
        for y_coord, line in enumerate(self.grid):
            for x_coord, character in enumerate(line):
                if character == "@":
                    self.get_surrounding_nodes(x_coord, y_coord)
        for removed_coord in self.removed_coords:
            self.grid[removed_coord[1]][removed_coord[0]] = "x"
        for line in self.grid:
            print(f"{line}")
        print()

    def one(self):
        """
        Count how many rolls of paper "@" have fewer than four rolls
        of paper in the eight adjacent positions surrounding them.
        """
        self.parse_grid()
        self.remove_rolls()
        print(f"Accessible rolls: {self.accessible_rolls}")

    def two(self):
        """
        Count how many rolls of paper "@" have fewer than four rolls
        of paper in the eight adjacent positions surrounding them.
        Remove them and repeat this process until there are not more
        accessible rools of paper.
        """
        self.parse_grid()
        # Basically a do/while here
        snapshot_removed_rolls = self.accessible_rolls
        self.remove_rolls()
        while snapshot_removed_rolls != self.accessible_rolls:
            snapshot_removed_rolls = self.accessible_rolls
            self.remove_rolls()
        print(f"Accessible rolls: {self.accessible_rolls}")


if __name__ == "__main__":
    print("[!] This is just a class definition!")
