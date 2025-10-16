from load_image import ft_load
from rotate import ft_rotate
import matplotlib.pyplot as plt
from zoom import ft_zoom


def main():
    image = ft_load("animal.jpeg")
    print(image)
    image = ft_zoom(image, 1.92)
    print(image)
    rotated_img = ft_rotate(image)
    if rotated_img is not None:
        plt.imshow(rotated_img, cmap="gray")
        plt.show()


if __name__ == "__main__":
    main()
