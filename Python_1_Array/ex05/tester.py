
from load_image import ft_load
import matplotlib.pyplot as plt
from pimp_image import ft_red, ft_green, \
    ft_blue, ft_grey, ft_invert


def main():
    image = ft_load("landscape.jpg")
    fig, axes = plt.subplots(1, 6, figsize=(10, 4))
    imgs = [image, ft_invert(image), ft_red(image), ft_green(image),
            ft_blue(image), ft_grey(image)]

    for i in range(6):
        axes[i].imshow(imgs[i])
        axes[i].set_title(f"Image {i + 1}")
        plt.imshow(imgs[i], cmap="gray")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
