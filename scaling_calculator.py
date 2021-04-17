from __future__ import annotations
import argparse
from math import ceil, floor


# Python's built in rounding function uses "bankers' rounding" which rounds halfs to the nearest even number.
# For example: 2.5 rounds to 2 instead of 3.
# This function always rounds half values up.
def half_round_up(f: float) -> float:
    if f - floor(f) < 0.5:
        return floor(f)
    else:
        return ceil(f)

class Dimension:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def scale(self, ratio: float) -> Dimension:
        # Scale the width by the given ratio, then scale the height according to the original aspect ratio:
        # original height / original width = new height / new width -> new height = new width * (original height / original width)
        scaled_width = half_round_up(self.width * ratio)
        scaled_height = half_round_up(scaled_width * ( self.height / self.width))

        return Dimension(scaled_width, scaled_height)


def scale_dimension(dimension: Dimension, base_density: str, target_density: str, densities: dict[str, int]) -> Dimension:
    scaling_ratio = densities[target_density] / densities[base_density]

    scaled_dimension = dimension.scale(scaling_ratio)

    return scaled_dimension


def calculate_scaled_dimensions(base_dimension: Dimension, base_density: str, densities: dict[str, int]) -> dict[str, Dimension]:
    return {target_density: scale_dimension(base_dimension, base_density, target_density, densities) for target_density in densities}


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

    args = parser.parse_args()

    # Create the base dimension
    base_dimension = Dimension(float(args.width), float(args.height))

    # Map containing the name and scaling ratio for each density
    densities = {"l": 3, "m": 4, "h": 6, "xh": 8, "xxh": 12, "xxxh": 16}

    # Calculate and print new dimensions for each density
    scaled_dimensions = calculate_scaled_dimensions(
        base_dimension, args.density, densities)

    for density, dimension in scaled_dimensions.items():
        # print with the form:
        # density:
        #   w=
        #   h=
        print(density + "dpi:")
        print(f"  w={dimension.width}")
        print(f"  h={dimension.height}")
