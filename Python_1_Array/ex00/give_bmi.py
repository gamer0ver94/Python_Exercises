import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
 -> list[int | float]:
    """This function calculate the bmi.
    Args:
        height: List of heights.
        weight: List of weights.
    Returns:
        Return a list of bmi value of each element index."""
    assert len(height) == len(weight), "Lists are not from the same size."
    assert all(isinstance(value, (int, float)) for value in height), \
        "values are not float or int."
    assert all(isinstance(value, (int, float)) for value in weight), \
        "values are not float or int."
    return list(np.array(weight) / (np.array(height) ** 2))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """"This function check if bmi of each element is bigger then the limit
    Args:
        bmi(list[int]): List of bmi values.
        limit(int): Limite value of a bmi.
    Returns:
        Return a list of booleans depending if it is above or not the limit."""
    return [True if value > limit else False for value in bmi]
