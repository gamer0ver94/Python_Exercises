import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """Slice a list from index start to end
    Args:
        family(list): List to be sliced.
        start(int): start index for the slice.
        end(int): end index for the slice.
    Returns: Return a sliced list from start to end"""

    family_row_size = len(family[0])
    assert all(family_row_size == len(value) for value in family), \
        "List not the same size."
    assert isinstance(family, list), "Not a list"
    sliced_lst = family[start:end]
    current_shape = np.shape(family)
    new_shape = np.shape(sliced_lst)

    print(f"My shape is : {current_shape}")
    print(f"My shape is : {new_shape}")
    return sliced_lst
