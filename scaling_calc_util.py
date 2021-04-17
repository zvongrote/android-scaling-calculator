from math import ceil, floor


# Python's built in rounding function uses "bankers' rounding" which rounds halfs to the nearest even number.
# For example: 2.5 rounds to 2 instead of 3.
# This function always rounds half values up.
def half_round_up(f: float) -> float:
    if f - floor(f) < 0.5:
        return floor(f)
    else:
        return ceil(f)
