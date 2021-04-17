"""
Calculate dimensions at different pixel densities.

To provide the best user experience on Android for different screen sizes and pixel densities 
it's common to export the same asset scaled up or down. This script calculates the scaled 
width and height of an asset at various pixel densities based on the recommended scaling factors
suggested by the Android documentation.

Usage:
    python3 scaling_calculator.py width height [options]

Arguments:
width               The starting width
height              The starting height

Options:
    -d --density    The prefix of the pixel density for the starting width and height. Can be from the set: {l,m,h,xh,xxh,xxxh}

Example:
    If an asset is designed at medium (1x) density with width=30 and height=45, the other densities can be calculated by:
    
    python3 scaling_calculator.py 30 45 -d m

    If designed at a different density, simply change the -d option to the corresponding density prefix (e.g l for ldpi, xh for xhdpi, etc.).
"""

import argparse
from dimension import Dimension


def scale_dimension(dimension: Dimension, base_density: str, target_density: str, densities: dict[str, int]) -> Dimension:
    """
    Scales a Dimension from a given base density to the target density

    Parameters
    ---------- 
    dimension: Dimension
        The Dimension to scale
    base_density: str
        The starting pixel density of the dimension
    target_density: str
        The desired pixel density
    densities: dict[str, int]
        A dictionary containing a label and scaling ratio for each density. For example, if the scaling
        factor from low to medium density is 3:4 then the dictionary could be:
        {"l": 3, "m": 4}

    Returns
    -------
    Dimension
        A new Dimension scaled to the target density, with the width and height rounded
    """

    scaling_ratio = densities[target_density] / densities[base_density]

    scaled_dimension = dimension.scale(scaling_ratio)

    return scaled_dimension


def calculate_scaled_dimensions(base_dimension: Dimension, base_density: str, densities: dict[str, int]) -> dict[str, Dimension]:
    """
    Calculates the dimensions for each provided pixel density from a base pixel density

    Parameters
    ----------
    base_dimension: Dimension
        The Dimension to scale
    base_density: str
        The starting pixel density of the base_dimension
    densities: dict[str, int]
        A dictionary containing a label and scaling ratio for each density. For example, if the scaling
        factor from low to medium density is 3:4 then the dictionary could be:
        {"l": 3, "m": 4}

    Returns
    -------
    dict[str, Dimension]
        A dictionary of the pixel density labels mapped to Dimension objects with the scaled dimensions
    """
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
