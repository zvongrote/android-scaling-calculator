from __future__ import annotations
from scaling_calc_util import half_round_up


class Dimension:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def scale(self, ratio: float) -> Dimension:
        # Scale the width by the given ratio, then scale the height according to the original aspect ratio:
        # original height / original width = new height / new width -> new height = new width * (original height / original width)
        scaled_width = half_round_up(self.width * ratio)
        scaled_height = half_round_up(
            scaled_width * (self.height / self.width))

        return Dimension(scaled_width, scaled_height)
