from __future__ import annotations
import argparse
from typing import Callable


class Dimension:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def scale(self, ratio: float) -> Dimension:
        scaled_width = self.width * ratio
        scaled_height = self.height * ratio

        return Dimension(scaled_width, scaled_height)


def scale_dimension(dimension: Dimension, base_density: str, target_density: str, densities: dict[str, int], round: Callable[[float], float]) -> Dimension:
    scaling_ratio = densities[target_density] / densities[base_density]

    scaled_dimension = dimension.scale(scaling_ratio)

    scaled_dimension.width = round(scaled_dimension.width)
    scaled_dimension.height = round(scaled_dimension.height)

    return scaled_dimension


if __name__ == "__main__":
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

    # Create the base dimension
    base_dimensions = Dimension(int(args.width), int(args.height))

    # Map containing the name and scaling ratio for each density
    densities = {"l": 3, "m": 4, "h": 6, "xh": 8, "xxh": 12, "xxxh": 16}
