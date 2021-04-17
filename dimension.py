from __future__ import annotations
from scaling_calc_util import half_round_up


class Dimension:
    """
    Used to represent the dimensions of an object that can be scaled.

    Attributes
    ----------
    width: float
        The width component
    height: float
        The height component

    Methods
    -------
    scale(ratio: float)
        Returns a new Dimension scaled by the ratio while maintaining the original aspect ratio.
    """

    def __init__(self, width: float, height: float) -> None:
        """
        Parameters
        ----------
        width: float
            The width component
        height: float
            The height component
        """

        self.width = width
        self.height = height

    def scale(self, ratio: float) -> Dimension:
        """
        Parameters
        ----------
        ratio: float
            The ratio to scale by. For example: to double the size pass in 2; to halve the size pass in 0.5

        Returns
        -------
        A new Dimension scaled by the ratio where the width and height are rounded
        """

        # Scale the width by the given ratio, then scale the height according to the original aspect ratio:
        # original height / original width = new height / new width -> new height = new width * (original height / original width)
        scaled_width = half_round_up(self.width * ratio)
        scaled_height = half_round_up(
            scaled_width * (self.height / self.width))

        return Dimension(scaled_width, scaled_height)
