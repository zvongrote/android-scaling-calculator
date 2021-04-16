import argparse

# Parse input
parser = argparse.ArgumentParser(
    "Calculates dimensions of a bitmap for different pixel densities.")

parser.add_argument("width",
                    type=float,
                    help="Width to scale")
parser.add_argument("height",
                    type=float,
                    help="Height to scale")
parser.add_argument("-d", "--density",
                    choices=["l", "m", "h", "xh", "xxh", "xxxh"],
                    default="m",
                    help="Starting pixel density")
parser.add_argument("-r", "--rounding-mode",
                    choices=["up", "down", "regular", "none"],
                    default="regular",
                    help="How to round the results")

args = parser.parse_args()
