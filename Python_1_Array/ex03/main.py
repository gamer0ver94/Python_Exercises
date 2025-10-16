from zoom import ft_zoom
from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def main() -> np.ndarray:
    image = ft_load("animal.jpeg")
    print(image)
    scale = 1.92
    zoomed_img = ft_zoom(image, scale)
    print(zoomed_img)
    plt.imshow(zoomed_img, cmap="gray")
    plt.show()


if __name__ == "__main__":
    main()
