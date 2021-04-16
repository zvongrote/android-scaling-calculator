from __future__ import annotations
import argparse
from typing import Callable
from math import ceil, floor


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

def calculate_scaled_dimensions(base_dimension: Dimension, base_density: str, densities: dict[str, int], rounding_function: Callable[[float], float]) -> dict[str, Dimension]:
    return {target_density: scale_dimension(base_dimension, base_density, target_density, densities, rounding_function) for target_density in densities}

# Python's built in rounding function uses "bankers' rounding" which rounds halfs to the nearest even number.
# For example: 2.5 rounds to 2 instead of 3.
# This function always rounds half values up.
def default_round(f: float) -> float:
    if f - floor(f) < 0.5:
        return floor(f)
    else:
        return ceil(f)


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
    base_dimension = Dimension(int(args.width), int(args.height))

    # Map containing the name and scaling ratio for each density
    densities = {"l": 3, "m": 4, "h": 6, "xh": 8, "xxh": 12, "xxxh": 16}

    # Set the rounding mode
    rounding_function: Callable[[float], float] = default_round
    rounding_mode = args.rounding_mode

    if rounding_mode == "up":
        rounding_function = ceil
    elif rounding_mode == "down":
        rounding_function = floor
    elif rounding_mode == "none":
        rounding_function = lambda x: x

    # Calculate and print new dimensions for each density
    scaled_dimensions = calculate_scaled_dimensions(base_dimension, args.density, densities, rounding_function)

    for density, dimension in scaled_dimensions.items():
        # print with the form:
        # density:
        #   w=
        #   h=
        print(density + "dpi:")
        print(f"  w={dimension.width}")
        print(f"  h={dimension.height}")