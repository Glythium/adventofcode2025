"""
The main driver for AoC 2024. Run this from the src directory
"""

try:
    from classes.d_1 import D1
except ModuleNotFoundError:
    print("[!] Could not find modules!")

def main():
    """
    Generates a solution for a day's puzzles
    """
    d1 = D1("../input/d1.txt", debug=True)
    # print(d1.one())
    # print(d1.two())


if __name__ == '__main__':
    main()
