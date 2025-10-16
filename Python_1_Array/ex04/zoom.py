import numpy as np


def ft_zoom(image: np.ndarray, scale: float) -> None:
    """Slice the photo to get the center of the image with some offset
    and create a one channel array
    Args:
        image(np.darray): The actuall image matrix
        scale: A float scale for the zoom
    Returns: Return a new image sliced from the previous."""
    height, width, channels = image.shape
    new_width = int(height / scale)
    new_height = int(height / scale)
    _y_start = int(height - new_height) // 2 - 80
    _x_start = int(width - new_width) // 2 + 140
    _y_end = _y_start + new_height
    _x_end = _x_start + new_width
    zoomed_img = image[_y_start:_y_end, _x_start:_x_end, 0:1]
    size = (new_height, new_width)
    print(f"New shape after slicing:{zoomed_img.shape} or {size}")
    return zoomed_img
