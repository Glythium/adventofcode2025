"""
The main driver for AoC 2025. Run this from the src directory
"""

try:
    from classes.d_2 import D2
except ModuleNotFoundError:
    print("[!] Could not find modules!")


def main():
    """
    Generates a solution for a day's puzzles
    """
    d2 = D2("../input/d2.txt", debug=True)
    # print(d2.one())
    print(d2.two())


if __name__ == "__main__":
    main()
