"""
The main driver for AoC 2025. Run this from the src directory
"""

try:
    from classes.d_11 import D11
except ModuleNotFoundError:
    print("[!] Could not find modules!")


def main():
    """
    Generates a solution for a day's puzzles
    """
    d11 = D11("../input/d11.txt", debug=True)
    print(d11.one())
    # print(d11.two())


if __name__ == "__main__":
    main()
