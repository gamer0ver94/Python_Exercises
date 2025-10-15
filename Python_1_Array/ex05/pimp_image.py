import numpy as np


def ft_invert(array) -> np.ndarray:
    img = array.copy()
    r = 255 - img[:, :, 0]
    g = 255 - img[:, :, 1]
    b = 255 - img[:, :, 2]
    img[:, :, 0] = r
    img[:, :, 1] = g
    img[:, :, 2] = b
    return img


def ft_red(array) -> np.ndarray:
    img = array.copy()

    img[:, :, 1] = 0
    img[:, :, 2] = 0
    return img


def ft_green(array) -> np.ndarray:
    img = array.copy()

    img[:, :, 0] = 0
    img[:, :, 2] = 0
    return img


def ft_blue(array) -> np.ndarray:
    img = array.copy()

    img[:, :, 0] = 0
    img[:, :, 1] = 0
    return img


def ft_grey(array) -> np.ndarray:
    img = array.copy()
    gray = 0.299 * img[:, :, 0] + 0.587 * img[:, :, 1] + 0.114 * img[:, :, 2]
    img[:, :, 0] = gray
    img[:, :, 1] = gray
    img[:, :, 2] = gray
    return img
