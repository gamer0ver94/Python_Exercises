from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray | None:
    """Load a image from a path
        Args:
            path(str): Where the image is located
        Returns:
            Return an array(numpy) of the image or
                none if the image does not load"""
    img_array = None
    try:
        img = Image.open(path)
        img_array = np.array(img)
        print(f"The shape of image is: {img_array.shape}")
    except Exception as e:
        print(f"Cant load image with current path : {e}")
    return img_array
