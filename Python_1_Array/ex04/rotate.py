import numpy as np


def ft_rotate(image: np.ndarray):
    if image is not None:
        height, width, channel = image.shape
        img = np.zeros((width, height, 3), dtype=image.dtype)
    else:
        print("no Image provided")
        return -1
    for y in range(height):
        for x in range(width):
            img[x, y] = image[y, x]

    return img
