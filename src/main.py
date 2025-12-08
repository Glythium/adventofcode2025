"""
The main driver for AoC 2025. Run this from the src directory
"""

try:
    from classes.d_3 import D3
except ModuleNotFoundError:
    print("[!] Could not find modules!")


def main():
    """
    Generates a solution for a day's puzzles
    """
    d3 = D3("../input/d3.txt", debug=True)
    print(d3.one())
    # print(d3.two())


if __name__ == "__main__":
    main()
